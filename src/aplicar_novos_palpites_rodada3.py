import sys
import os
import math
import numpy as np

# Adiciona o diretório atual ao path para importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS

QGS = {
    "México": (19.3030, -99.1506),
    "África do Sul": (20.1010, -98.7591),
    "Coreia do Sul": (20.6790, -103.3933),
    "Tchéquia": (32.5632, -97.1417),
    "Canadá": (49.2827, -123.1207),
    "Bósnia e Herzegovina": (40.6180, -111.8882),
    "Catar": (34.4208, -119.6982),
    "Suíça": (33.0210, -117.1897),
    "Brasil": (40.7968, -74.4815),
    "Marrocos": (40.7062, -74.5493),
    "Haiti": (39.4633, -74.5670),
    "Escócia": (35.2271, -80.8431),
    "EUA": (33.6846, -117.8265),
    "Paraguai": (37.3382, -121.8863),
    "Austrália": (37.7652, -122.2417),
    "Turquia": (33.4152, -111.8315),
    "Alemanha": (36.0999, -80.2442),
    "Curaçao": (26.3683, -80.1289),
    "Costa do Marfim": (39.8496, -75.3565),
    "Equador": (40.0125, -82.9861),
    "Holanda": (39.0997, -94.5786),
    "Japão": (36.1627, -86.7816),
    "Suécia": (32.7767, -96.7970),
    "Tunísia": (25.6866, -100.3161),
    "Bélgica": (47.4829, -122.2170),
    "Egito": (47.6588, -117.4260),
    "Irã": (32.5149, -117.0382),
    "Nova Zelândia": (32.7157, -117.1611),
    "Espanha": (35.0456, -85.3097),
    "Cabo Verde": (27.9506, -82.4572),
    "Arábia Saudita": (30.2672, -97.7431),
    "Uruguai": (20.6296, -87.0739),
    "França": (42.3601, -71.0589),
    "Senegal": (40.4862, -74.4518),
    "Iraque": (37.7926, -80.4452),
    "Noruega": (36.0726, -79.7920),
    "Argentina": (39.0997, -94.5786),
    "Argélia": (38.9717, -95.2353),
    "Áustria": (34.4208, -119.6982),
    "Jordânia": (45.5152, -122.6784),
    "Portugal": (26.7153, -80.0534),
    "RD Congo": (29.7604, -95.3698),
    "Uzbequistão": (33.7490, -84.3880),
    "Colômbia": (20.6790, -103.3933),
    "Inglaterra": (39.0997, -94.5786),
    "Croácia": (38.8048, -77.0469),
    "Gana": (41.9220, -71.5489),
    "Panamá": (43.6532, -79.3832)
}

ESTADIOS = {
    "Mexico City Stadium": (19.3030, -99.1506),
    "Guadalajara Stadium": (20.6811, -103.4628),
    "Toronto Stadium": (43.6332, -79.4186),
    "San Francisco Bay Stadium": (37.4033, -121.9702),
    "New York New Jersey Stadium": (40.8135, -74.0744),
    "Boston Stadium": (42.0909, -71.2643),
    "Los Angeles Stadium": (33.9535, -118.3390),
    "Vancouver Stadium": (49.2767, -123.1120),
    "Houston Stadium": (29.6847, -95.4082),
    "Philadelphia Stadium": (39.9008, -75.1675),
    "Dallas Stadium": (32.7473, -97.0841),
    "Monterrey Stadium": (25.6692, -100.2443),
    "Seattle Stadium": (47.5952, -122.3316),
    "Atlanta Stadium": (33.7573, -84.4010),
    "Miami Stadium": (25.9580, -80.2389),
    "Kansas City Stadium": (39.0489, -94.4839)
}

# Dia da última partida de cada seleção na Rodada 2
ULTIMO_JOGO = {
    "Tchéquia": 18, "África do Sul": 18, "México": 18, "Coreia do Sul": 18,
    "Suíça": 18, "Bósnia e Herzegovina": 18, "Canadá": 18, "Catar": 18,
    "Escócia": 19, "Marrocos": 19, "Brasil": 19, "Haiti": 19,
    "EUA": 19, "Austrália": 19, "Turquia": 19, "Paraguai": 19,
    "Alemanha": 20, "Costa do Marfim": 20, "Equador": 20, "Curaçao": 20,
    "Holanda": 20, "Suécia": 20, "Tunísia": 20, "Japão": 20,
    "Bélgica": 21, "Irã": 21, "Nova Zelândia": 21, "Egito": 21,
    "Espanha": 21, "Arábia Saudita": 21, "Uruguai": 21, "Cabo Verde": 21,
    "França": 22, "Iraque": 22, "Noruega": 22, "Senegal": 22,
    "Argentina": 22, "Áustria": 22, "Jordânia": 22, "Argélia": 22,
    "Portugal": 23, "Uzbequistão": 23, "Colômbia": 23, "RD Congo": 23,
    "Inglaterra": 23, "Gana": 23, "Panamá": 23, "Croácia": 23
}

# Odds de mercado para a 3ª Rodada
ODDS_MERCADO = {
    ("Suíça", "Canadá"): {"vitoria_a": 2.30, "empate": 3.40, "vitoria_b": 3.35},
    ("Bósnia e Herzegovina", "Catar"): {"vitoria_a": 1.40, "empate": 4.50, "vitoria_b": 7.00},
    ("Escócia", "Brasil"): {"vitoria_a": 10.00, "empate": 5.20, "vitoria_b": 1.34},
    ("Marrocos", "Haiti"): {"vitoria_a": 1.20, "empate": 6.00, "vitoria_b": 17.00},
    ("Tchéquia", "México"): {"vitoria_a": 3.70, "empate": 3.50, "vitoria_b": 1.90},
    ("África do Sul", "Coreia do Sul"): {"vitoria_a": 5.50, "empate": 3.80, "vitoria_b": 1.66},
    ("Equador", "Alemanha"): {"vitoria_a": 4.00, "empate": 4.10, "vitoria_b": 1.88},
    ("Curaçao", "Costa do Marfim"): {"vitoria_a": 20.00, "empate": 8.60, "vitoria_b": 1.16},
    ("Japão", "Suécia"): {"vitoria_a": 1.90, "empate": 3.60, "vitoria_b": 4.45},
    ("Tunísia", "Holanda"): {"vitoria_a": 26.00, "empate": 9.25, "vitoria_b": 1.13},
    ("Turquia", "EUA"): {"vitoria_a": 3.70, "empate": 4.10, "vitoria_b": 1.95},
    ("Paraguai", "Austrália"): {"vitoria_a": 2.95, "empate": 2.26, "vitoria_b": 4.00},
    ("Noruega", "França"): {"vitoria_a": 3.80, "empate": 3.10, "vitoria_b": 2.10},
    ("Senegal", "Iraque"): {"vitoria_a": 1.80, "empate": 3.40, "vitoria_b": 4.80},
    ("Cabo Verde", "Arábia Saudita"): {"vitoria_a": 2.50, "empate": 3.10, "vitoria_b": 3.00},
    ("Uruguai", "Espanha"): {"vitoria_a": 4.00, "empate": 3.40, "vitoria_b": 1.95},
    ("Egito", "Irã"): {"vitoria_a": 1.90, "empate": 3.25, "vitoria_b": 4.40},
    ("Nova Zelândia", "Bélgica"): {"vitoria_a": 9.00, "empate": 4.80, "vitoria_b": 1.35},
    ("Panamá", "Inglaterra"): {"vitoria_a": 11.50, "empate": 5.80, "vitoria_b": 1.25},
    ("Croácia", "Gana"): {"vitoria_a": 1.85, "empate": 3.40, "vitoria_b": 4.50},
    ("Colômbia", "Portugal"): {"vitoria_a": 3.65, "empate": 3.20, "vitoria_b": 2.10},
    ("RD Congo", "Uzbequistão"): {"vitoria_a": 2.15, "empate": 3.25, "vitoria_b": 3.50},
    ("Argélia", "Áustria"): {"vitoria_a": 2.45, "empate": 3.20, "vitoria_b": 3.00},
    ("Jordânia", "Argentina"): {"vitoria_a": 10.00, "empate": 5.20, "vitoria_b": 1.30}
}

# 24 Confrontos da 3ª Rodada
jogos_rodada3 = [
    # 24 de Junho
    ("B", "Suíça", "Canadá", "Vancouver Stadium", 24, 18),
    ("B", "Bósnia e Herzegovina", "Catar", "Seattle Stadium", 24, 18),
    ("C", "Escócia", "Brasil", "Miami Stadium", 24, 28),
    ("C", "Marrocos", "Haiti", "Atlanta Stadium", 24, 24),
    ("A", "Tchéquia", "México", "Mexico City Stadium", 24, 20),
    ("A", "África do Sul", "Coreia do Sul", "Monterrey Stadium", 24, 30),
    # 25 de Junho
    ("E", "Equador", "Alemanha", "New York New Jersey Stadium", 25, 22),
    ("E", "Curaçao", "Costa do Marfim", "Philadelphia Stadium", 25, 24),
    ("F", "Japão", "Suécia", "Dallas Stadium", 25, 26),
    ("F", "Tunísia", "Holanda", "Kansas City Stadium", 25, 24),
    ("D", "Turquia", "EUA", "Los Angeles Stadium", 25, 22),
    ("D", "Paraguai", "Austrália", "San Francisco Bay Stadium", 25, 22),
    # 26 de Junho
    ("I", "Noruega", "França", "Boston Stadium", 26, 20),
    ("I", "Senegal", "Iraque", "Toronto Stadium", 26, 18),
    ("H", "Cabo Verde", "Arábia Saudita", "Houston Stadium", 26, 28),
    ("H", "Uruguai", "Espanha", "Guadalajara Stadium", 26, 24),
    # 27 de Junho
    ("G", "Egito", "Irã", "Seattle Stadium", 27, 18),
    ("G", "Nova Zelândia", "Bélgica", "Vancouver Stadium", 27, 18),
    ("L", "Panamá", "Inglaterra", "New York New Jersey Stadium", 27, 22),
    ("L", "Croácia", "Gana", "Philadelphia Stadium", 27, 24),
    ("K", "Colômbia", "Portugal", "Miami Stadium", 27, 28),
    ("K", "RD Congo", "Uzbequistão", "Atlanta Stadium", 27, 24),
    ("J", "Argélia", "Áustria", "Kansas City Stadium", 27, 24),
    ("J", "Jordânia", "Argentina", "Dallas Stadium", 27, 26)
]

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lon / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c

def calcular_pontos(xp, yp, xr, yr):
    if xp == xr and yp == yr:
        return 30
    if xp == yp and xr == yr:
        return 15
    if xp > yp and xr > yr:
        return 20 if xp == xr else 15
    if xp < yp and xr < yr:
        return 20 if yp == yr else 15
    return 0

QUALIFIED = {"México", "EUA", "Alemanha", "França", "Noruega", "Argentina", "Colômbia"}
ELIMINATED = {"Haiti", "Turquia", "Tunísia", "Senegal", "Iraque", "Uzbequistão", "Panamá"}
DEFENSIVE_UNDERDOGS = {"Irã", "Curaçao", "Gana", "Cabo Verde", "África do Sul"}
DESPERATE_TEAMS = {
    "Tunísia", "Turquia", "Senegal", "Iraque", 
    "Arábia Saudita", "Cabo Verde", "Uruguai", 
    "Irã", "Nova Zelândia", "Bélgica", "Croácia", 
    "RD Congo", "Uzbequistão", "Jordânia"
}

def get_blend_weight(t_a, t_b):
    if t_a in QUALIFIED and t_b in QUALIFIED:
        return 0.45, "Ambas Classificadas (Poupa de Elenco)"
    if t_a in QUALIFIED or t_b in QUALIFIED or t_a in ELIMINATED or t_b in ELIMINATED:
        return 0.40, "Motivação Assimétrica (Misto de Titulares/Reservas)"
    return 0.55, "Duelo Direto Decisivo"

# Treina o modelo inicial
model = DixonColesModel(phi=0.0019, reg_lambda=1.5, shrink_lambda=0.1)
model.fit(JOGOS_CONCLUIDOS)

# Aplica o ajuste de 5% de melhoria defensiva nos sobreditos "Defensive Underdogs"
for team in DEFENSIVE_UNDERDOGS:
    if team in model.team_to_idx:
        idx = model.team_to_idx[team]
        model.betas[idx] *= 0.95  # Redução de 5% na vulnerabilidade defensiva

print(f"Modelo Dixon-Coles calibrado com {len(JOGOS_CONCLUIDOS)} jogos.")
print(f"Parâmetro global de gols (mu): {model.mu:.4f}")
print(f"Fator Casa (gamma): {model.gamma:.4f}")
print(f"Dixon-Coles rho: {model.rho:.4f}")

previsoes = []
for grupo, t_a, t_b, stadium, dia_jogo, temp in jogos_rodada3:
    lat_s, lon_s = ESTADIOS[stadium]
    lat_a, lon_a = QGS[t_a]
    lat_b, lon_b = QGS[t_b]
    
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    rest_a = dia_jogo - ULTIMO_JOGO[t_a]
    rest_b = dia_jogo - ULTIMO_JOGO[t_b]
    
    odds = ODDS_MERCADO.get((t_a, t_b))
    
    # Determina o peso de blending de forma dinâmica baseado no status das equipes
    w_modelo, justificativa_peso = get_blend_weight(t_a, t_b)
    
    # Nos jogos da terceira rodada, limitamos o disparity boost a 1.30 e aplicamos o desespero
    P, la, lb = model.predict_probabilities(
        t_a, t_b, odds_mercado=odds, w_modelo=w_modelo,
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b, max_boost=1.30,
        desperate_a=(t_a in DESPERATE_TEAMS), desperate_b=(t_b in DESPERATE_TEAMS)
    )
    
    # Otimização por Valor Esperado (EV) do Bolão
    best_ev = -1
    best_placar = (0, 0)
    for xp in range(5):
        for yp in range(5):
            ev = 0.0
            for xr in range(6):
                for yr in range(6):
                    ev += P[xr, yr] * calcular_pontos(xp, yp, xr, yr)
            if ev > best_ev:
                best_ev = ev
                best_placar = (xp, yp)
                
    res = model.get_top_scores(
        t_a, t_b, odds_mercado=odds, w_modelo=w_modelo,
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b, max_boost=1.30,
        desperate_a=(t_a in DESPERATE_TEAMS), desperate_b=(t_b in DESPERATE_TEAMS)
    )
    
    prob_win_a = sum(P[x, y] for x in range(6) for y in range(6) if x > y)
    prob_draw = sum(P[x, y] for x in range(6) for y in range(6) if x == y)
    prob_win_b = sum(P[x, y] for x in range(6) for y in range(6) if x < y)
    
    previsoes.append({
        "grupo": grupo,
        "time_a": t_a,
        "time_b": t_b,
        "stadium": stadium,
        "dia_jogo": f"{dia_jogo}/Jun",
        "temp": temp,
        "dist_a": round(dist_a),
        "dist_b": round(dist_b),
        "rest_a": rest_a,
        "rest_b": rest_b,
        "lambda_a": la,
        "lambda_b": lb,
        "prob_win_a": prob_win_a,
        "prob_draw": prob_draw,
        "prob_win_b": prob_win_b,
        "best_placar": best_placar,
        "best_ev": best_ev,
        "top_3_placares": res["top_3_placares"],
        "confianca": res["confianca_placar"],
        "justificativa_peso": justificativa_peso,
        "w_modelo": w_modelo
    })

# Escreve o relatório Markdown em ambos os destinos
paths = [
    "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada3.md",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../relatorios/palpites_copa_2026_rodada3.md"))
]

for report_path in paths:
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# 📊 Relatório Preditivo: 3ª Rodada da Copa do Mundo FIFA 2026\n\n")
        f.write("Este relatório apresenta a análise estatística e tática detalhada para todas as 24 partidas da terceira e última rodada da fase de grupos. A metodologia preditiva foi adaptada especificamente para contornar as anomalias comuns de encerramento de grupo (poupa de titulares de equipes já qualificadas, motivação assimétrica e retrancas desesperadas).\n\n")
        f.write("## 🛠️ Ajustes de Calibração Utilizados:\n")
        f.write("1. **Mesclagem Dinâmica com Odds de Mercado (`w_modelo`):** Para jogos de times qualificados ou eliminados, as odds reais detêm 60% do peso, já que o mercado reage instantaneamente a informações de escalação alternativa. Para jogos de confronto direto, o modelo estatístico mantém a primazia (55% do peso).\n")
        f.write("2. **Underdog Resiliency Buffer:** Incremento de 5% na solidez defensiva (redução do parâmetro `beta`) para seleções com perfil de forte bloco defensivo baixo (Cabo Verde, RD Congo, Irã, Curaçao, África do Sul).\n")
        f.write("3. **Curinga de Disparidade Controlado:** O limitador do *Disparity Boost* foi reduzido de `1.50` para `1.30` para evitar a projeção de goleadas irreais em jogos sem interesse ofensivo de seleções qualificadas.\n")
        f.write("4. **Banco de Dados Completo:** Calibração executada sobre o histórico completo de **48 jogos reais** das rodadas 1 e 2.\n\n")
        f.write("---\n\n")
        f.write("## 📅 Resumo dos Palpites (Tabela Rápida para o Bolão)\n\n")
        f.write("| Grupo | Confronto | Local / Estádio | Status | Palpite Preditivo | Confiança | EV Otimizado | Contexto de Peso |\n")
        f.write("| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |\n")
        
        for p in previsoes:
            match_str = f"{p['time_a']} vs. {p['time_b']}"
            placar_str = f"**{p['best_placar'][0]} x {p['best_placar'][1]}**"
            f.write(f"| **{p['grupo']}** | {match_str} | {p['stadium']} | Preditivo | {placar_str} | **{p['confianca']}** | {p['best_ev']:.2f} pts | {p['justificativa_peso']} (w: {p['w_modelo']:.2f}) |\n")
            
        f.write("\n---\n\n")
        f.write("## 🔍 Análise Detalhada Jogo a Jogo\n\n")
        
        current_group = ""
        for p in previsoes:
            if p["grupo"] != current_group:
                current_group = p["grupo"]
                f.write(f"### **Grupo {current_group}**\n\n")
                
            placar_str = f"{p['best_placar'][0]} x {p['best_placar'][1]}"
            f.write(f"*   **{p['time_a']} {placar_str} {p['time_b']}**\n")
            f.write(f"    *   **Estádio:** {p['stadium']} (Temperatura: {p['temp']}°C)\n")
            f.write(f"    *   **Status:** Preditivo ({p['dia_jogo']})\n")
            
            # Constrói justificativa detalhada baseada em dados
            just = f"Palpite otimizado por Valor Esperado (EV: {p['best_ev']:.2f} pts) para o bolão com blending de {p['w_modelo']*100:.0f}% modelo / {(1-p['w_modelo'])*100:.0f}% odds de mercado ({p['justificativa_peso']}). "
            just += f"Médias de gols projetadas: {p['time_a']} ({p['lambda_a']:.2f}) vs. {p['time_b']} ({p['lambda_b']:.2f}). "
            
            # Fatores físicos
            just += f"Fatores Físicos: {p['time_a']} viajou {p['dist_a']} km com {p['rest_a']} dias de descanso; "
            just += f"{p['time_b']} viajou {p['dist_b']} km com {p['rest_b']} dias de descanso. "
            
            # Tática e resiliência
            if p['time_a'] in DEFENSIVE_UNDERDOGS or p['time_b'] in DEFENSIVE_UNDERDOGS:
                just += "O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. "
            
            f.write(f"    *   **Justificativa:** {just}\n")
            f.write(f"    *   **Probabilidades:** Vitória {p['time_a']}: {p['prob_win_a']*100:.1f}% | Empate: {p['prob_draw']*100:.1f}% | Vitória {p['time_b']}: {p['prob_win_b']*100:.1f}%\n")
            f.write(f"    *   **Top 3 Placares mais Prováveis:** {p['top_3_placares'][0][0]} ({p['top_3_placares'][0][1]}), {p['top_3_placares'][1][0]} ({p['top_3_placares'][1][1]}), {p['top_3_placares'][2][0]} ({p['top_3_placares'][2][1]})\n")
            f.write(f"    *   **Nível de Confiança:** {p['confianca']}\n\n")

    print(f"Relatório preditivo salvo com sucesso em: {report_path}")
