import sys
import os
import numpy as np
import math

sys.path.append("/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/scratch")
from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS

QGS = {
    "Costa do Marfim": (39.8496, -75.3565),
    "Equador": (40.0125, -82.9861),
    "Suécia": (32.7767, -96.7970),
    "Tunísia": (25.6866, -100.3161),
    "Bélgica": (47.4829, -122.2170),
    "Egito": (47.6588, -117.4260),
    "Irã": (32.5149, -117.0382),
    "Nova Zelândia": (32.7157, -117.1611),
    "Espanha": (35.0456, -85.3097),
    "Cabo Verde": (27.9506, -82.4572),
    "Uruguai": (20.6296, -87.0739),
    "Arábia Saudita": (30.2672, -97.7431),
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
    "Philadelphia Stadium": (39.9008, -75.1675),
    "Monterrey Stadium": (25.6692, -100.2443),
    "Seattle Stadium": (47.5952, -122.3316),
    "Los Angeles Stadium": (33.9535, -118.3390),
    "Atlanta Stadium": (33.7573, -84.4010),
    "Miami Stadium": (25.9580, -80.2389),
    "New York New Jersey Stadium": (40.8135, -74.0744),
    "Boston Stadium": (42.0909, -71.2643),
    "Kansas City Stadium": (39.0489, -94.4839),
    "Dallas Stadium": (32.7473, -97.0841),
    "Houston Stadium": (29.6847, -95.4082),
    "Toronto Stadium": (43.6332, -79.4186),
    "Mexico City Stadium": (19.3030, -99.1506)
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
    # Regras do Bolão
    if xp == xr and yp == yr:
        return 30
    
    # Empate correto mas placar diferente
    if xp == yp and xr == yr:
        return 15
        
    # Vencedor A correto
    if xp > yp and xr > yr:
        if xp == xr:
            return 20
        else:
            return 15
            
    # Vencedor B correto
    if xp < yp and xr < yr:
        if yp == yr:
            return 20
        else:
            return 15
            
    return 0

jogos_restantes = [
    ("França", "Senegal", "New York New Jersey Stadium", 22),
    ("Iraque", "Noruega", "Boston Stadium", 20),
    ("Argentina", "Argélia", "Kansas City Stadium", 24),
    ("Áustria", "Jordânia", "Dallas Stadium", 26),
    ("Portugal", "RD Congo", "Houston Stadium", 28),
    ("Uzbequistão", "Colômbia", "Mexico City Stadium", 20),
    ("Inglaterra", "Croácia", "Dallas Stadium", 26),
    ("Gana", "Panamá", "Toronto Stadium", 18)
]

model = DixonColesModel(phi=0.0019, reg_lambda=5.0, shrink_lambda=0.1)
model.fit(JOGOS_CONCLUIDOS)

print("| Jogo | Top Placar Exato | Placar Otimizado Bolão | EV Esperado (Pts) |")
print("| :--- | :---: | :---: | :---: |")

for t_a, t_b, stadium, temp in jogos_restantes:
    lat_s, lon_s = ESTADIOS[stadium]
    lat_a, lon_a = QGS[t_a]
    lat_b, lon_b = QGS[t_b]
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    P, la, lb = model.predict_probabilities(
        t_a, t_b, 
        distancia_a=dist_a, rest_a=4, temp=temp,
        distancia_b=dist_b, rest_b=4
    )
    
    # Acha o placar exato de maior probabilidade
    max_p = -1
    best_exato = (0, 0)
    for x in range(6):
        for y in range(6):
            if P[x, y] > max_p:
                max_p = P[x, y]
                best_exato = (x, y)
                
    # Otimização por Valor Esperado (EV)
    best_ev = -1
    best_placar_ev = (0, 0)
    
    for xp in range(4): # Limita previsões plausíveis de 0 a 3 gols
        for yp in range(4):
            ev = 0.0
            for xr in range(6):
                for yr in range(6):
                    ev += P[xr, yr] * calcular_pontos(xp, yp, xr, yr)
            if ev > best_ev:
                best_ev = ev
                best_placar_ev = (xp, yp)
                
    print(f"| {t_a} vs. {t_b} | **{best_exato[0]} x {best_exato[1]}** ({max_p*100:.1f}%) | **{best_placar_ev[0]} x {best_placar_ev[1]}** | {best_ev:.2f} pts |")
