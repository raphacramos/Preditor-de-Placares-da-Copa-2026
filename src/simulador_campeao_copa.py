import sys
import os
import numpy as np
import math

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS, CO_HOSTS, poisson_pmf, dixon_coles_tau

# Lista de todos os grupos e seleções da Copa de 2026
GRUPOS = {
    "A": ["México", "África do Sul", "Coreia do Sul", "Tchéquia"],
    "B": ["Canadá", "Bosnia e Herzegovina", "Catar", "Suíça"],
    "C": ["Brasil", "Marrocos", "Haiti", "Escócia"],
    "D": ["EUA", "Paraguai", "Austrália", "Turquia"],
    "E": ["Alemanha", "Curaçao", "Costa do Marfim", "Equador"],
    "F": ["Holanda", "Japão", "Sweden", "Tunisia"], # Ajustando nomes para bater com BASE_PRIORS
    "G": ["Bélgica", "Egito", "Irã", "Nova Zelândia"],
    "H": ["Espanha", "Cabo Verde", "Arábia Saudita", "Uruguai"],
    "I": ["França", "Senegal", "Iraque", "Noruega"],
    "J": ["Argentina", "Argélia", "Áustria", "Jordânia"],
    "K": ["Portugal", "RD Congo", "Uzbequistão", "Colômbia"],
    "L": ["Inglaterra", "Croácia", "Gana", "Panamá"]
}

# Mapear grafias corretas
GRAFIA_MAP = {
    "Bosnia e Herzegovina": "Bósnia e Herzegovina",
    "Sweden": "Suécia",
    "Tunisia": "Tunísia",
    "Turquia": "Turquia", # Já está certo ou "Turquia" -> "Turquia"
}

# Inicializa o modelo Dixon-Coles sintonizado
model = DixonColesModel(phi=0.0019, reg_lambda=1.5, shrink_lambda=0.1)
model.fit(JOGOS_CONCLUIDOS)

# Função para simular uma única partida
def simular_partida(time_a, time_b):
    # Traduz nomes se necessário
    t_a = GRAFIA_MAP.get(time_a, time_a)
    t_b = GRAFIA_MAP.get(time_b, time_b)
    
    idx_a = model.team_to_idx.get(t_a)
    idx_b = model.team_to_idx.get(t_b)
    
    if idx_a is None or idx_b is None:
        # Fallback caso haja erro de grafia
        return 1, 1, 0.5, 0.5
        
    factor_a = model.gamma if t_a in CO_HOSTS else 1.0
    factor_b = model.gamma if t_b in CO_HOSTS else 1.0
    
    lambda_a = model.mu * model.alphas[idx_a] * model.betas[idx_b] * factor_a
    lambda_b = model.mu * model.alphas[idx_b] * model.betas[idx_a] * factor_b
    
    # Coeficiente de Disparidade de Elenco (Disparity Boost) - limitado a 1.5 para estabilidade
    ratio = lambda_a / lambda_b if lambda_a > lambda_b else lambda_b / lambda_a
    if ratio > 1.8:
        boost = min(1.0 + 0.18 * (ratio - 1.8), 1.5)
        if lambda_a > lambda_b:
            lambda_a *= boost
            lambda_b *= 0.90
        else:
            lambda_b *= boost
            lambda_a *= 0.90
            
    # Matriz Dixon-Coles
    P = np.zeros((6, 6))
    for x in range(6):
        for y in range(6):
            p_a = poisson_pmf(lambda_a, x)
            p_b = poisson_pmf(lambda_b, y)
            tau = dixon_coles_tau(x, y, lambda_a, lambda_b, model.rho)
            P[x, y] = max(tau * p_a * p_b, 0.0)
            
    P /= np.sum(P)
    
    # Sorteio do placar
    idx = np.random.choice(36, p=P.flatten())
    gols_a = idx // 6
    gols_b = idx % 6
    
    # Calcula probabilidades de vitória para critério de desempate em mata-mata
    p_win_a = 0.0
    p_win_b = 0.0
    for x in range(6):
        for y in range(6):
            if x > y:
                p_win_a += P[x, y]
            elif x < y:
                p_win_b += P[x, y]
                
    return gols_a, gols_b, p_win_a, p_win_b

# Função para simular o grupo
def simular_grupo(times):
    # Roda todos contra todos no grupo (6 jogos)
    pontos = {t: 0 for t in times}
    gols_pro = {t: 0 for t in times}
    gols_contra = {t: 0 for t in times}
    
    confrontos = [
        (times[0], times[1]), (times[2], times[3]),
        (times[0], times[2]), (times[1], times[3]),
        (times[0], times[3]), (times[1], times[2])
    ]
    
    for ta, tb in confrontos:
        ga, gb, _, _ = simular_partida(ta, tb)
        gols_pro[ta] += ga
        gols_contra[ta] += gb
        gols_pro[tb] += gb
        gols_contra[tb] += ga
        
        if ga > gb:
            pontos[ta] += 3
        elif ga < gb:
            pontos[tb] += 3
        else:
            pontos[ta] += 1
            pontos[tb] += 1
            
    # Classificação
    # Critérios: Pontos, Saldo de Gols, Gols Pró
    ranking = sorted(times, key=lambda t: (
        pontos[t], 
        gols_pro[t] - gols_contra[t], 
        gols_pro[t]
    ), reverse=True)
    
    return ranking, pontos, gols_pro, gols_contra

def simular_copa_completa():
    # 1. Fase de Grupos
    classificados_1o = []
    classificados_2o = []
    terceiros = []
    
    pontos_terceiros = {}
    saldo_terceiros = {}
    gp_terceiros = {}
    
    for g_id, times in GRUPOS.items():
        ranking, pontos, gp, gc = simular_grupo(times)
        classificados_1o.append(ranking[0])
        classificados_2o.append(ranking[1])
        
        t3 = ranking[2]
        terceiros.append(t3)
        pontos_terceiros[t3] = pontos[t3]
        saldo_terceiros[t3] = gp[t3] - gc[t3]
        gp_terceiros[t3] = gp[t3]
        
    # Selecionar os 8 melhores terceiros colocados
    melhores_terceiros = sorted(terceiros, key=lambda t: (
        pontos_terceiros[t],
        saldo_terceiros[t],
        gp_terceiros[t]
    ), reverse=True)[:8]
    
    # 2. Montar chaveamento do mata-mata (Round of 32)
    # 12 Primeiros + 12 Segundos + 8 Terceiros = 32 times
    todos_classificados = []
    todos_classificados.extend(classificados_1o) # 12 times
    todos_classificados.extend(classificados_2o) # 12 times
    todos_classificados.extend(melhores_terceiros) # 8 times
    
    # Bracket da Rodada de 32 (16 confrontos)
    # Para simplificar, faremos confrontos diretos
    np.random.shuffle(classificados_1o)
    np.random.shuffle(classificados_2o)
    np.random.shuffle(melhores_terceiros)
    
    rodada_32 = []
    # 8 jogos: 1ºs contra os 8 melhores 3ºs
    for i in range(8):
        rodada_32.append((classificados_1o[i], melhores_terceiros[i]))
    # 4 jogos: os outros 4 1ºs contra 2ºs
    for i in range(4):
        rodada_32.append((classificados_1o[8+i], classificados_2o[i]))
    # 8 jogos: os outros 2ºs entre si
    for i in range(4):
        rodada_32.append((classificados_2o[4+i], classificados_2o[8+i]))
        
    # Simula o mata-mata
    def simular_mata_mata(confrontos):
        vencedores = []
        for ta, tb in confrontos:
            ga, gb, p_a, p_b = simular_partida(ta, tb)
            if ga > gb:
                vencedores.append(ta)
            elif ga < gb:
                vencedores.append(tb)
            else:
                # Empate: Critério de desempate baseado na força do time
                p_total = p_a + p_b
                if p_total > 0:
                    prob_prog = p_a / p_total
                else:
                    prob_prog = 0.5
                if np.random.rand() < prob_prog:
                    vencedores.append(ta)
                else:
                    vencedores.append(tb)
        return vencedores

    # R32 -> R16
    vencedores_32 = simular_mata_mata(rodada_32)
    rodada_16 = [(vencedores_32[i], vencedores_32[i+1]) for i in range(0, 16, 2)]
    
    # R16 -> Quartas
    vencedores_16 = simular_mata_mata(rodada_16)
    quartas = [(vencedores_16[i], vencedores_16[i+1]) for i in range(0, 8, 2)]
    
    # Quartas -> Semi
    vencedores_quartas = simular_mata_mata(quartas)
    semis = [(vencedores_quartas[i], vencedores_quartas[i+1]) for i in range(0, 4, 2)]
    
    # Semi -> Final
    finalistas = simular_mata_mata(semis)
    
    # Final
    campeao = simular_mata_mata([(finalistas[0], finalistas[1])])[0]
    
    return campeao, finalistas

def rodar_monte_carlo_campeao(n_simulacoes=10000):
    contagem_campeao = {}
    contagem_finalista = {}
    
    for i in range(n_simulacoes):
        campeao, finalistas = simular_copa_completa()
        contagem_campeao[campeao] = contagem_campeao.get(campeao, 0) + 1
        for f in finalistas:
            contagem_finalista[f] = contagem_finalista.get(f, 0) + 1
            
        if (i+1) % 2000 == 0:
            print(f"Simulados {i+1} torneios...")
            
    print("\n" + "=" * 50)
    print(" RESULTADO FINAL: SIMULAÇÃO MONTE CARLO COPA 2026 ")
    print(f" ({n_simulacoes:,} Copas Completas Simuladas)")
    print("=" * 50)
    print("| Ranking | Seleção | Probabilidade Campeão | Probabilidade Finalista |")
    print("| :--- | :--- | :---: | :---: |")
    
    ranking = sorted(contagem_campeao.items(), key=lambda x: x[1], reverse=True)
    for pos, (time, vitorias) in enumerate(ranking[:10], 1):
        p_camp = (vitorias / n_simulacoes) * 100
        f_count = contagem_finalista.get(time, 0)
        p_fin = (f_count / n_simulacoes) * 100
        print(f"| #{pos} | {time} | **{p_camp:.2f}%** | {p_fin:.2f}% |")
    print("=" * 50)

if __name__ == "__main__":
    # Define a semente aleatória para consistência
    np.random.seed(42)
    rodar_monte_carlo_campeao(10000)
