import math

# Coordenadas aproximadas dos QGs (Base Camps) das seleções
QGS = {
    "México": (19.3030, -99.1506), # Mexico City (CAR)
    "África do Sul": (20.1010, -98.7591), # Pachuca, Mexico
    "Coreia do Sul": (20.6790, -103.3933), # Guadalajara, Mexico
    "Tchéquia": (32.5632, -97.1417), # Mansfield, Texas
    "Canadá": (49.2827, -123.1207), # Vancouver, BC
    "Bósnia e Herzegovina": (40.6180, -111.8882), # Sandy, Utah
    "Catar": (34.4208, -119.6982), # Santa Barbara, CA
    "Suíça": (33.0210, -117.1897), # San Diego, CA (Jewish Academy)
    "Brasil": (40.7968, -74.4815), # Morristown, NJ
    "Marrocos": (40.7062, -74.5493), # Basking Ridge, NJ
    "Haiti": (39.4633, -74.5670), # Galloway, NJ
    "Escócia": (35.2271, -80.8431), # Charlotte, NC
    "EUA": (33.6846, -117.8265), # Irvine, CA
    "Paraguai": (37.3382, -121.8863), # San Jose, CA
    "Austrália": (37.7652, -122.2417), # Alameda, CA
    "Turquia": (33.4152, -111.8315), # Mesa, AZ
    "Alemanha": (36.0999, -80.2442), # Winston-Salem, NC
    "Curaçao": (26.3683, -80.1289), # Boca Raton, FL
    "Costa do Marfim": (39.8496, -75.3565), # Chester, PA
    "Equador": (40.0125, -82.9861), # Columbus, OH
    "Holanda": (39.0997, -94.5786), # Kansas City, MO
    "Japão": (36.1627, -86.7816), # Nashville, TN
    "Suécia": (32.7767, -96.7970), # Dallas, TX
    "Tunísia": (25.6866, -100.3161), # Monterrey, Mexico
    "Bélgica": (47.4829, -122.2170), # Renton, WA
    "Egito": (47.6588, -117.4260), # Spokane, WA
    "Irã": (32.5149, -117.0382), # Tijuana, Mexico
    "Nova Zelândia": (32.7157, -117.1611), # San Diego, CA
    "Espanha": (35.0456, -85.3097), # Chattanooga, TN
    "Cabo Verde": (27.9506, -82.4572), # Tampa, FL
    "Arábia Saudita": (30.2672, -97.7431), # Austin, TX
    "Uruguai": (20.6296, -87.0739), # Playa del Carmen, Mexico
    "França": (42.3601, -71.0589), # Boston, MA
    "Senegal": (40.4862, -74.4518), # New Brunswick, NJ
    "Iraque": (37.7926, -80.4452), # Greenbrier County, WV
    "Noruega": (36.0726, -79.7920), # Greensboro, NC
    "Argentina": (39.0997, -94.5786), # Kansas City, KS
    "Argélia": (38.9717, -95.2353), # Lawrence, KS
    "Áustria": (34.4208, -119.6982), # Santa Barbara, CA
    "Jordânia": (45.5152, -122.6784), # Portland, OR
    "Portugal": (26.7153, -80.0534), # Palm Beach County, FL
    "RD Congo": (29.7604, -95.3698), # Houston, TX
    "Uzbequistão": (33.7490, -84.3880), # Atlanta, Ga
    "Colômbia": (20.6790, -103.3933), # Zapopan, Mexico
    "Inglaterra": (39.0997, -94.5786), # Kansas City, MO
    "Croácia": (38.8048, -77.0469), # Alexandria, VA
    "Gana": (41.9220, -71.5489), # Smithfield, RI
    "Panamá": (43.6532, -79.3832) # Toronto, ON
}

# Coordenadas das cidades-sede / estádios
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

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0 # Raio da Terra em km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    
    a = math.sin(d_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lon / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c

jogos = [
    # Grupo A
    ("México", "África do Sul", "Mexico City Stadium", "11/Jun"),
    ("Coreia do Sul", "Tchéquia", "Guadalajara Stadium", "12/Jun"),
    # Grupo B
    ("Canadá", "Bósnia e Herzegovina", "Toronto Stadium", "12/Jun"),
    ("Catar", "Suíça", "San Francisco Bay Stadium", "13/Jun"),
    # Grupo C
    ("Brasil", "Marrocos", "New York New Jersey Stadium", "13/Jun"),
    ("Haiti", "Escócia", "Boston Stadium", "14/Jun"),
    # Grupo D
    ("EUA", "Paraguai", "Los Angeles Stadium", "12/Jun"),
    ("Austrália", "Turquia", "Vancouver Stadium", "14/Jun"),
    # Grupo E
    ("Alemanha", "Curaçao", "Houston Stadium", "14/Jun"),
    ("Costa do Marfim", "Equador", "Philadelphia Stadium", "14/Jun"),
    # Grupo F
    ("Holanda", "Japão", "Dallas Stadium", "14/Jun"),
    ("Suécia", "Tunísia", "Monterrey Stadium", "15/Jun"),
    # Grupo G
    ("Bélgica", "Egito", "Seattle Stadium", "15/Jun"),
    ("Irã", "Nova Zelândia", "Los Angeles Stadium", "15/Jun"),
    # Grupo H
    ("Espanha", "Cabo Verde", "Atlanta Stadium", "15/Jun"),
    ("Uruguai", "Arábia Saudita", "Miami Stadium", "15/Jun"),
    # Grupo I
    ("França", "Senegal", "New York New Jersey Stadium", "16/Jun"),
    ("Iraque", "Noruega", "Boston Stadium", "16/Jun"),
    # Grupo J
    ("Argentina", "Argélia", "Kansas City Stadium", "16/Jun"),
    ("Áustria", "Jordânia", "Dallas Stadium", "16/Jun"),
    # Grupo K
    ("Portugal", "RD Congo", "Houston Stadium", "17/Jun"),
    ("Uzbequistão", "Colômbia", "Mexico City Stadium", "17/Jun"),
    # Grupo L
    ("Inglaterra", "Croácia", "Dallas Stadium", "17/Jun"),
    ("Gana", "Panamá", "Toronto Stadium", "17/Jun")
]

print("| Confronto | Data | Estádio | Distância A (km) | Distância B (km) |")
print("| :--- | :---: | :--- | :---: | :---: |")
for team_a, team_b, stadium, date in jogos:
    lat_s, lon_s = ESTADIOS[stadium]
    
    # Time A
    lat_a, lon_a = QGS[team_a]
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    
    # Time B
    lat_b, lon_b = QGS[team_b]
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    print(f"| {team_a} vs. {team_b} | {date} | {stadium} | {dist_a:.0f} km | {dist_b:.0f} km |")
