import sys
import os
import math
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS

QGS = {
    "Tchéquia": (32.5632, -97.1417),
    "África do Sul": (20.1010, -98.7591),
    "Suíça": (33.0210, -117.1897),
    "Bósnia e Herzegovina": (40.6180, -111.8882),
    "Canadá": (49.2827, -123.1207),
    "Catar": (34.4208, -119.6982),
    "México": (19.3030, -99.1506),
    "Coreia do Sul": (20.6790, -103.3933)
}

ESTADIOS = {
    "Atlanta Stadium": (33.7573, -84.4010),
    "Los Angeles Stadium": (33.9535, -118.3390),
    "Vancouver Stadium": (49.2767, -123.1120),
    "Mexico City Stadium": (19.3030, -99.1506)
}

ULTIMO_JOGO = {
    "Tchéquia": 12, "África do Sul": 11,
    "Suíça": 13, "Bósnia e Herzegovina": 12,
    "Canadá": 12, "Catar": 13,
    "México": 11, "Coreia do Sul": 12
}

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

# Inicializa e sintoniza o modelo preditivo
model = DixonColesModel(phi=0.0019, reg_lambda=1.5, shrink_lambda=0.1)
model.fit(JOGOS_CONCLUIDOS)

# Jogos de hoje com odds reais de mercado
jogos_hoje = [
    {
        "grupo": "A", "time_a": "Tchéquia", "time_b": "África do Sul", "stadium": "Atlanta Stadium",
        "temp": 24, "dia": 18, "placar_anterior": "2 x 0",
        "odds": {"vitoria_a": 1.75, "empate": 2.80, "vitoria_b": 3.80}
    },
    {
        "grupo": "B", "time_a": "Suíça", "time_b": "Bósnia e Herzegovina", "stadium": "Los Angeles Stadium",
        "temp": 22, "dia": 18, "placar_anterior": "2 x 0",
        "odds": {"vitoria_a": 1.65, "empate": 3.10, "vitoria_b": 4.75}
    },
    {
        "grupo": "B", "time_a": "Canadá", "time_b": "Catar", "stadium": "Vancouver Stadium",
        "temp": 18, "dia": 18, "placar_anterior": "2 x 1",
        "odds": {"vitoria_a": 1.28, "empate": 5.70, "vitoria_b": 11.00}
    },
    {
        "grupo": "A", "time_a": "México", "time_b": "Coreia do Sul", "stadium": "Mexico City Stadium",
        "temp": 20, "dia": 18, "placar_anterior": "2 x 1",
        "odds": {"vitoria_a": 2.00, "empate": 3.20, "vitoria_b": 3.80}
    }
]

print("=" * 80)
print(" COMPARATIVO DE PALPITES: MODELO PURO vs. MODELO MESCLADO COM ODDS REAIS ")
print("=" * 80)

for j in jogos_hoje:
    t_a, t_b = j["time_a"], j["time_b"]
    lat_s, lon_s = ESTADIOS[j["stadium"]]
    lat_a, lon_a = QGS[t_a]
    lat_b, lon_b = QGS[t_b]
    
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    rest_a = j["dia"] - ULTIMO_JOGO[t_a]
    rest_b = j["dia"] - ULTIMO_JOGO[t_b]
    
    # 1. Probabilidade pura (Sem Odds)
    P_pura, _, _ = model.predict_probabilities(
        t_a, t_b, odds_mercado=None,
        distancia_a=dist_a, rest_a=rest_a, temp=j["temp"],
        distancia_b=dist_b, rest_b=rest_b
    )
    
    # 2. Probabilidade mesclada (Com Odds reais)
    P_blend, _, _ = model.predict_probabilities(
        t_a, t_b, odds_mercado=j["odds"], w_modelo=0.60,
        distancia_a=dist_a, rest_a=rest_a, temp=j["temp"],
        distancia_b=dist_b, rest_b=rest_b
    )
    
    # Otimização por EV - Pura
    best_ev_pura = -1
    best_placar_pura = (0, 0)
    for xp in range(5):
        for yp in range(5):
            ev = sum(P_pura[xr, yr] * calcular_pontos(xp, yp, xr, yr) for xr in range(6) for yr in range(6))
            if ev > best_ev_pura:
                best_ev_pura = ev
                best_placar_pura = (xp, yp)
                
    # Otimização por EV - Mesclada
    best_ev_blend = -1
    best_placar_blend = (0, 0)
    for xp in range(5):
        for yp in range(5):
            ev = sum(P_blend[xr, yr] * calcular_pontos(xp, yp, xr, yr) for xr in range(6) for yr in range(6))
            if ev > best_ev_blend:
                best_ev_blend = ev
                best_placar_blend = (xp, yp)
                
    placar_pura_str = f"{best_placar_pura[0]} x {best_placar_pura[1]}"
    placar_blend_str = f"{best_placar_blend[0]} x {best_placar_blend[1]}"
    
    print(f"\n⚽ {t_a} vs. {t_b}")
    print(f"   -> Palpite Puro (Sem Odds):  {placar_pura_str} (EV: {best_ev_pura:.2f} pts)")
    print(f"   -> Palpite Mesclado (Odds):  {placar_blend_str} (EV: {best_ev_blend:.2f} pts)")
    if placar_pura_str == placar_blend_str:
        print("   ✅ RESULTADO: O palpite NÃO muda. Permanece idêntico.")
    else:
        print(f"   🚨 ATENÇÃO: O palpite MUDOU de {placar_pura_str} para {placar_blend_str}!")

print("\n" + "=" * 80)
