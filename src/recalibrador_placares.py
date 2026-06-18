import math
import sys
import os

# Adiciona o diretório atual ao path para importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS, BASE_PRIORS, CO_HOSTS, dixon_coles_tau, poisson_pmf

def recalibrar_confronto(time_a, time_b, base_lambda_a, base_lambda_b, 
                         desfalques_a=0, desfalques_b=0, 
                         postura_a="normal", postura_b="normal",
                         altitude_calor=False, odds_mercado=None, w_modelo=0.60):
    """
    Recalibra o confronto utilizando o modelo de Dixon-Coles treinado
    com jogos concluídos da Copa do Mundo de 2026.
    """
    # 1. Inicializa e treina o modelo Dixon-Coles com os jogos reais concluídos
    model = DixonColesModel(phi=0.0019, reg_lambda=5.0, shrink_lambda=0.1)
    model.fit(JOGOS_CONCLUIDOS)
    
    # 2. Resgata as forças de ataque e defesa ajustadas (ou usa priors como fallback)
    idx_a = model.team_to_idx.get(time_a)
    idx_b = model.team_to_idx.get(time_b)
    
    alpha_a = model.alphas[idx_a] if idx_a is not None else base_lambda_a
    beta_a = model.betas[idx_a] if idx_a is not None else 1.0
    alpha_b = model.alphas[idx_b] if idx_b is not None else base_lambda_b
    beta_b = model.betas[idx_b] if idx_b is not None else 1.0
    
    # Se a equipe não estiver nos priors (caso improvável), usa os lambdas base fornecidos
    if idx_a is None or idx_b is None:
        lambda_a = base_lambda_a
        lambda_b = base_lambda_b
    else:
        # Fator casa (se for co-host e jogar em casa)
        factor_a = model.gamma if time_a in CO_HOSTS else 1.0
        factor_b = model.gamma if time_b in CO_HOSTS else 1.0
        lambda_a = model.mu * alpha_a * beta_b * factor_a
        lambda_b = model.mu * alpha_b * beta_a * factor_b

    # 3. Ajuste de Desfalques
    lambda_a *= math.pow(0.85, desfalques_a)
    lambda_b *= math.pow(1.10, desfalques_a)
    
    lambda_b *= math.pow(0.85, desfalques_b)
    lambda_a *= math.pow(1.10, desfalques_b)
    
    # 4. Ajuste de Postura Tática
    if postura_a == "retranca":
        lambda_a *= 0.80
        lambda_b *= 0.75
    if postura_b == "retranca":
        lambda_b *= 0.80
        lambda_a *= 0.75
        
    # 5. Ajuste de Clima/Altitude
    if altitude_calor:
        lambda_a *= 0.90
        lambda_b *= 0.90

    # 5b. Coeficiente de Disparidade de Elenco (Disparity Boost) - limitado a 1.5 para estabilidade
    ratio = lambda_a / lambda_b if lambda_a > lambda_b else lambda_b / lambda_a
    if ratio > 1.8:
        boost = min(1.0 + 0.18 * (ratio - 1.8), 1.5)
        if lambda_a > lambda_b:
            lambda_a *= boost
            lambda_b *= 0.90
        else:
            lambda_b *= boost
            lambda_a *= 0.90

    # 6. Matriz de probabilidade Dixon-Coles ajustada
    import numpy as np
    P_model = np.zeros((6, 6))
    for x in range(6):
        for y in range(6):
            p_a = poisson_pmf(lambda_a, x)
            p_b = poisson_pmf(lambda_b, y)
            tau = dixon_coles_tau(x, y, lambda_a, lambda_b, model.rho)
            P_model[x, y] = max(tau * p_a * p_b, 0.0)
            
    P_model /= np.sum(P_model)
    
    # 7. Fusão Bayesiana com as Odds de Mercado (se fornecidas)
    if odds_mercado:
        inv_odds = {k: 1.0 / v for k, v in odds_mercado.items()}
        sum_inv = sum(inv_odds.values())
        p_market = {k: v / sum_inv for k, v in inv_odds.items()}
        
        p_model_win_a = 0.0
        p_model_draw = 0.0
        p_model_win_b = 0.0
        for x in range(6):
            for y in range(6):
                if x > y:
                    p_model_win_a += P_model[x, y]
                elif x == y:
                    p_model_draw += P_model[x, y]
                else:
                    p_model_win_b += P_model[x, y]
                    
        p_blend_win_a = w_modelo * p_model_win_a + (1.0 - w_modelo) * p_market["vitoria_a"]
        p_blend_draw = w_modelo * p_model_draw + (1.0 - w_modelo) * p_market["empate"]
        p_blend_win_b = w_modelo * p_model_win_b + (1.0 - w_modelo) * p_market["vitoria_b"]
        
        P_final = np.zeros((6, 6))
        eps = 1e-10
        for x in range(6):
            for y in range(6):
                if x > y:
                    P_final[x, y] = P_model[x, y] * (p_blend_win_a / (p_model_win_a + eps))
                elif x == y:
                    P_final[x, y] = P_model[x, y] * (p_blend_draw / (p_model_draw + eps))
                else:
                    P_final[x, y] = P_model[x, y] * (p_blend_win_b / (p_model_win_b + eps))
        P_final /= np.sum(P_final)
    else:
        P_final = P_model

    # 8. Extração dos Marginais e Ordenação
    prob_vitoria_a = 0.0
    prob_empate = 0.0
    prob_vitoria_b = 0.0
    placares = []
    
    for x in range(6):
        for y in range(6):
            prob = P_final[x, y]
            placares.append(((x, y), prob))
            if x > y:
                prob_vitoria_a += prob
            elif x == y:
                prob_empate += prob
            else:
                prob_vitoria_b += prob
                
    placares_ordenados = sorted(placares, key=lambda val: val[1], reverse=True)
    best_placar, best_prob = placares_ordenados[0]
    
    if best_prob >= 0.16:
        confianca = "Alta"
    elif best_prob >= 0.11:
        confianca = "Média"
    else:
        confianca = "Baixa"
        
    return {
        "confronto": f"{time_a} vs. {time_b}",
        "lambda_ajustado_a": round(lambda_a, 2),
        "lambda_ajustado_b": round(lambda_b, 2),
        "prob_resultado": {
            "vitoria_a": f"{prob_vitoria_a * 100:.1f}%",
            "empate": f"{prob_empate * 100:.1f}%",
            "vitoria_b": f"{prob_vitoria_b * 100:.1f}%"
        },
        "top_3_placares": [
            (f"{p[0][0]} x {p[0][1]}", f"{p[1] * 100:.2f}%") for p in placares_ordenados[:3]
        ],
        "confianca_placar": confianca
    }

if __name__ == "__main__":
    # Teste de compatibilidade para garantir que o wrapper funciona como esperado
    print("=" * 60)
    print(" WRAPPER DE COMPATIBILIDADE DO RECALIBRADOR ")
    print("=" * 60)
    
    # Executa com os mesmos parâmetros do script original
    t_a = "Brasil"
    t_b = "Marrocos"
    res = recalibrar_confronto(
        time_a=t_a, time_b=t_b,
        base_lambda_a=1.7, base_lambda_b=1.1,
        desfalques_a=1,
        desfalques_b=0,
        postura_a="normal",
        postura_b="retranca",
        altitude_calor=False
    )
    
    print(f"Jogo: {res['confronto']}")
    print(f"Médias de Gols Ajustadas: {t_a} ({res['lambda_ajustado_a']}) | {t_b} ({res['lambda_ajustado_b']})")
    print(f"Probabilidades de Resultado: Vencer A: {res['prob_resultado']['vitoria_a']} | Empate: {res['prob_resultado']['empate']} | Vencer B: {res['prob_resultado']['vitoria_b']}")
    print("-" * 60)
    print("Top 3 Placares mais Prováveis (Dixon-Coles):")
    for placar, prob in res['top_3_placares']:
        print(f" -> Placar: {placar} | Probabilidade: {prob}")
    print(f"Nível de Confiança no Placar Sugerido: {res['confianca_placar']}")
    print("=" * 60)
