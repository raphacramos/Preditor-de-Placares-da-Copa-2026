import sys
import os
import math
import numpy as np

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

ULTIMO_JOGO = {
    "México": 11, "África do Sul": 11,
    "Coreia do Sul": 12, "Tchéquia": 12, "Canadá": 12, "Bósnia e Herzegovina": 12, "EUA": 12, "Paraguai": 12,
    "Catar": 13, "Suíça": 13, "Brasil": 13, "Marrocos": 13,
    "Haiti": 14, "Escócia": 14, "Austrália": 14, "Turquia": 14, "Alemanha": 14, "Curaçao": 14, "Costa do Marfim": 14, "Equador": 14, "Holanda": 14, "Japão": 14,
    "Suécia": 15, "Tunísia": 15, "Bélgica": 15, "Egito": 15, "Irã": 15, "Nova Zelândia": 15, "Espanha": 15, "Cabo Verde": 15, "Uruguai": 15, "Arábia Saudita": 15,
    "França": 16, "Senegal": 16, "Iraque": 16, "Noruega": 16, "Argentina": 16, "Argélia": 16, "Áustria": 16, "Jordânia": 16,
    "Portugal": 17, "RD Congo": 17, "Uzbequistão": 17, "Colômbia": 17, "Inglaterra": 17, "Croácia": 17, "Gana": 17, "Panamá": 17
}

# 24 Confrontos da 2ª Rodada
jogos_rodada2 = [
    # Grupo A
    ("A", "Tchéquia", "África do Sul", "Atlanta Stadium", 18, 24),
    ("A", "México", "Coreia do Sul", "Mexico City Stadium", 18, 20),
    # Grupo B
    ("B", "Suíça", "Bósnia e Herzegovina", "Los Angeles Stadium", 18, 22),
    ("B", "Canadá", "Catar", "Vancouver Stadium", 18, 18),
    # Grupo C
    ("C", "Escócia", "Marrocos", "Boston Stadium", 19, 20),
    ("C", "Brasil", "Haiti", "Philadelphia Stadium", 19, 24),
    # Grupo D
    ("D", "EUA", "Austrália", "Seattle Stadium", 19, 18),
    ("D", "Turquia", "Paraguai", "San Francisco Bay Stadium", 19, 22),
    # Grupo E
    ("E", "Alemanha", "Costa do Marfim", "Toronto Stadium", 20, 18),
    ("E", "Equador", "Curaçao", "Kansas City Stadium", 20, 24),
    # Grupo F
    ("F", "Holanda", "Suécia", "Houston Stadium", 20, 28),
    ("F", "Tunísia", "Japão", "Monterrey Stadium", 20, 30),
    # Grupo G
    ("G", "Bélgica", "Irã", "Los Angeles Stadium", 21, 22),
    ("G", "Nova Zelândia", "Egito", "Vancouver Stadium", 21, 18),
    # Grupo H
    ("H", "Espanha", "Arábia Saudita", "Atlanta Stadium", 21, 24),
    ("H", "Uruguai", "Cabo Verde", "Miami Stadium", 21, 28),
    # Grupo I
    ("I", "França", "Iraque", "Philadelphia Stadium", 22, 24),
    ("I", "Noruega", "Senegal", "New York New Jersey Stadium", 22, 22),
    # Grupo J
    ("J", "Argentina", "Áustria", "Dallas Stadium", 22, 26),
    ("J", "Jordânia", "Argélia", "San Francisco Bay Stadium", 22, 22),
    # Grupo K
    ("K", "Portugal", "Uzbequistão", "Houston Stadium", 23, 28),
    ("K", "Colômbia", "RD Congo", "Guadalajara Stadium", 23, 24),
    # Grupo L
    ("L", "Inglaterra", "Gana", "Boston Stadium", 23, 20),
    ("L", "Panamá", "Croácia", "Toronto Stadium", 23, 18)
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
    # Novas regras do Bolão:
    # 30 pts: placar exato
    if xp == xr and yp == yr:
        return 30
    # 15 pts: empate correto mas placar diferente
    if xp == yp and xr == yr:
        return 15
    # 20 pts: vencedor correto + gols do vencedor corretos (perdedor gols errou)
    if xp > yp and xr > yr:
        return 20 if xp == xr else 15
    if xp < yp and xr < yr:
        return 20 if yp == yr else 15
    return 0

# Inicializa e sintoniza o modelo preditivo
model = DixonColesModel(phi=0.0019, reg_lambda=1.5, shrink_lambda=0.1)
model.fit(JOGOS_CONCLUIDOS)

print(f"Modelo Dixon-Coles calibrado com {len(JOGOS_CONCLUIDOS)} jogos.")
print(f"Parâmetro global de gols (mu): {model.mu:.4f}")
print(f"Fator Casa (gamma): {model.gamma:.4f}")
print(f"Dixon-Coles rho: {model.rho:.4f}")

# Calcula previsões
previsoes = []
for grupo, t_a, t_b, stadium, dia_jogo, temp in jogos_rodada2:
    lat_s, lon_s = ESTADIOS[stadium]
    lat_a, lon_a = QGS[t_a]
    lat_b, lon_b = QGS[t_b]
    
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    rest_a = dia_jogo - ULTIMO_JOGO[t_a]
    rest_b = dia_jogo - ULTIMO_JOGO[t_b]
    
    P, la, lb = model.predict_probabilities(
        t_a, t_b,
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b
    )
    
    # Otimização por Valor Esperado (EV) do Bolão
    best_ev = -1
    best_placar = (0, 0)
    for xp in range(5): # limita a placares de até 4 gols para permitir goleadas seguras
        for yp in range(5):
            ev = 0.0
            for xr in range(6):
                for yr in range(6):
                    ev += P[xr, yr] * calcular_pontos(xp, yp, xr, yr)
            if ev > best_ev:
                best_ev = ev
                best_placar = (xp, yp)
                
    # Extrai top 3 placares
    placares_sorted = []
    for x in range(6):
        for y in range(6):
            placares_sorted.append(((x, y), P[x, y]))
    placares_sorted = sorted(placares_sorted, key=lambda val: val[1], reverse=True)
    
    res = model.get_top_scores(
        t_a, t_b,
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b
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
        "confianca": res["confianca_placar"]
    })

# Escreve o relatório Markdown
report_path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada2.md"

with open(report_path, "w", encoding="utf-8") as f:
    f.write("# 📊 Relatório Preditivo: 2ª Rodada da Copa do Mundo FIFA 2026\n\n")
    f.write(f"Este relatório apresenta uma análise estatística e tática detalhada para todas as 24 partidas da segunda rodada da fase de grupos da Copa do Mundo FIFA 2026. A metodologia preditiva foi calibrada utilizando as 24 partidas concluídas da 1ª rodada (com peso estendido através de regularização mais leve `reg_lambda=1.5` e sintonização do fator global de gols `mu={model.mu:.4f}` para refletir a alta taxa de gols de 3.125 por partida observada na rodada inicial).\n\n")
    f.write("---\n\n")
    f.write("## 📅 Resumo dos Palpites (Tabela Rápida para o Bolão)\n\n")
    f.write("| Grupo | Confronto | Local / Estádio | Status | Palpite Preditivo | Confiança | EV Otimizado |\n")
    f.write("| :---: | :--- | :--- | :---: | :---: | :---: | :---: |\n")
    
    for p in previsoes:
        match_str = f"{p['time_a']} vs. {p['time_b']}"
        placar_str = f"**{p['best_placar'][0]} x {p['best_placar'][1]}**"
        f.write(f"| **{p['grupo']}** | {match_str} | {p['stadium']} | Preditivo | {placar_str} | **{p['confianca']}** | {p['best_ev']:.2f} pts |\n")
        
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
        just = f"Palpite otimizado por Valor Esperado (EV: {p['best_ev']:.2f} pts) para as regras do bolão. "
        just += f"Médias de gols projetadas pelo Dixon-Coles sintonizado: {p['time_a']} ({p['lambda_a']:.2f}) vs. {p['time_b']} ({p['lambda_b']:.2f}). "
        
        # Fadiga / Descanso
        just += f"Fatores Físicos: {p['time_a']} viajou {p['dist_a']} km com {p['rest_a']} dias de descanso; "
        just += f"{p['time_b']} viajou {p['dist_b']} km com {p['rest_b']} dias de descanso. "
        
        # Tendência tática baseada em gols
        ratio = p['lambda_a'] / p['lambda_b'] if p['lambda_a'] > p['lambda_b'] else p['lambda_b'] / p['lambda_a']
        if ratio > 1.8:
            just += "O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. "
        else:
            just += "Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. "
            
        f.write(f"    *   **Justificativa:** {just}\n")
        f.write(f"    *   **Probabilidades:** Vitória {p['time_a']}: {p['prob_win_a']*100:.1f}% | Empate: {p['prob_draw']*100:.1f}% | Vitória {p['time_b']}: {p['prob_win_b']*100:.1f}%\n")
        f.write(f"    *   **Top 3 Placares mais Prováveis:** {p['top_3_placares'][0][0]} ({p['top_3_placares'][0][1]}), {p['top_3_placares'][1][0]} ({p['top_3_placares'][1][1]}), {p['top_3_placares'][2][0]} ({p['top_3_placares'][2][1]})\n")
        f.write(f"    *   **Nível de Confiança:** {p['confianca']}\n\n")

print(f"Novo relatório preditivo salvo com sucesso em: {report_path}")
