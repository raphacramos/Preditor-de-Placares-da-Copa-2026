import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS

# Instancia e treina o modelo sintonizado
model = DixonColesModel(phi=0.0019, reg_lambda=1.5, shrink_lambda=0.1)
model.fit(JOGOS_CONCLUIDOS)

# Dados geográficos e de descanso para os jogos de hoje (18/Jun)
# Usando dados do script de rodada 2
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
    import math
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lon / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c

# 4 Jogos de hoje com odds de mercado reais coletadas
jogos_hoje = [
    {
        "time_a": "Tchéquia", "time_b": "África do Sul", "stadium": "Atlanta Stadium",
        "temp": 24, "dia": 18,
        "odds": {"vitoria_a": 1.75, "empate": 2.80, "vitoria_b": 3.80}
    },
    {
        "time_a": "Suíça", "time_b": "Bósnia e Herzegovina", "stadium": "Los Angeles Stadium",
        "temp": 22, "dia": 18,
        "odds": {"vitoria_a": 1.65, "empate": 3.10, "vitoria_b": 4.75}
    },
    {
        "time_a": "Canadá", "time_b": "Catar", "stadium": "Vancouver Stadium",
        "temp": 18, "dia": 18,
        "odds": {"vitoria_a": 1.28, "empate": 5.70, "vitoria_b": 11.00}
    },
    {
        "time_a": "México", "time_b": "Coreia do Sul", "stadium": "Mexico City Stadium",
        "temp": 20, "dia": 18,
        "odds": {"vitoria_a": 2.00, "empate": 3.20, "vitoria_b": 3.80}
    }
]

print("=" * 70)
print(" DESAFIO ÀS ODDS DE MERCADO (ANÁLISE DE EXPECTED VALUE - EV) ")
print("=" * 70)

for j in jogos_hoje:
    t_a, t_b = j["time_a"], j["time_b"]
    lat_s, lon_s = ESTADIOS[j["stadium"]]
    lat_a, lon_a = QGS[t_a]
    lat_b, lon_b = QGS[t_b]
    
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    rest_a = j["dia"] - ULTIMO_JOGO[t_a]
    rest_b = j["dia"] - ULTIMO_JOGO[t_b]
    
    # 1. Probabilidade pura do modelo (sem odds)
    P_pura, _, _ = model.predict_probabilities(
        t_a, t_b, odds_mercado=None,
        distancia_a=dist_a, rest_a=rest_a, temp=j["temp"],
        distancia_b=dist_b, rest_b=rest_b
    )
    prob_pura_a = sum(P_pura[x, y] for x in range(6) for y in range(6) if x > y)
    prob_pura_d = sum(P_pura[x, y] for x in range(6) for y in range(6) if x == y)
    prob_pura_b = sum(P_pura[x, y] for x in range(6) for y in range(6) if x < y)
    
    # Odds justas calculadas
    fair_a = 1.0 / prob_pura_a if prob_pura_a > 0 else float('inf')
    fair_d = 1.0 / prob_pura_d if prob_pura_d > 0 else float('inf')
    fair_b = 1.0 / prob_pura_b if prob_pura_b > 0 else float('inf')
    
    # 2. Fusão Bayesiana (com odds de mercado)
    P_blend, _, _ = model.predict_probabilities(
        t_a, t_b, odds_mercado=j["odds"], w_modelo=0.60,
        distancia_a=dist_a, rest_a=rest_a, temp=j["temp"],
        distancia_b=dist_b, rest_b=rest_b
    )
    prob_blend_a = sum(P_blend[x, y] for x in range(6) for y in range(6) if x > y)
    prob_blend_d = sum(P_blend[x, y] for x in range(6) for y in range(6) if x == y)
    prob_blend_b = sum(P_blend[x, y] for x in range(6) for y in range(6) if x < y)
    
    # EVs das apostas
    ev_a = (prob_pura_a * j["odds"]["vitoria_a"]) - 1.0
    ev_d = (prob_pura_d * j["odds"]["empate"]) - 1.0
    ev_b = (prob_pura_b * j["odds"]["vitoria_b"]) - 1.0
    
    print(f"\n⚽ Confronto: {t_a} vs. {t_b}")
    print(f"   -> PROBABILIDADES MODELO:  A: {prob_pura_a*100:.1f}% | Empate: {prob_pura_d*100:.1f}% | B: {prob_pura_b*100:.1f}%")
    print(f"   -> ODDS JUSTAS DO MODELO:  A: {fair_a:.2f} | Empate: {fair_d:.2f} | B: {fair_b:.2f}")
    print(f"   -> ODDS DE MERCADO (REAL): A: {j['odds']['vitoria_a']:.2f} | Empate: {j['odds']['empate']:.2f} | B: {j['odds']['vitoria_b']:.2f}")
    print(f"   -> EXPECTED VALUE (EV):    A: {ev_a*100:+.1f}% | Empate: {ev_d*100:+.1f}% | B: {ev_b*100:+.1f}%")
    
    # Destaca Valor
    valores = []
    if ev_a > 0.05: valores.append(f"Vitória {t_a} ({ev_a*100:+.1f}%)")
    if ev_d > 0.05: valores.append(f"Empate ({ev_d*100:+.1f}%)")
    if ev_b > 0.05: valores.append(f"Vitória {t_b} ({ev_b*100:+.1f}%)")
    
    if valores:
        print(f"   🔥 OPORTUNIDADE DE VALOR ENCONTRADA: {', '.join(valores)}")
    else:
        print("   ❌ Nenhuma aposta com valor positivo claro (margem da casa corrói o EV).")
        
    print(f"   -> PROB. MESCLADA (BAYESIANA): A: {prob_blend_a*100:.1f}% | Empate: {prob_blend_d*100:.1f}% | B: {prob_blend_b*100:.1f}%")

print("=" * 70)
