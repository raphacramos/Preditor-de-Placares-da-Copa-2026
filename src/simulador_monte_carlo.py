import sys
import os
import numpy as np
import math

# Adiciona o diretório scratch ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS

# Dicionário de QGs e Sedes para busca automática de parâmetros logísticos
QGS = {
    "Costa do Marfim": (39.8496, -75.3565), # Chester, PA
    "Equador": (40.0125, -82.9861), # Columbus, OH
    "Suécia": (32.7767, -96.7970), # Dallas, TX
    "Tunísia": (25.6866, -100.3161), # Monterrey, Mexico
    "Bélgica": (47.4829, -122.2170), # Renton, WA
    "Egito": (47.6588, -117.4260), # Spokane, WA
    "Espanha": (35.0456, -85.3097), # Chattanooga, TN
    "Cabo Verde": (27.9506, -82.4572), # Tampa, FL
    "Uruguai": (20.6296, -87.0739), # Playa del Carmen, Mexico
    "Arábia Saudita": (30.2672, -97.7431) # Austin, TX
}

ESTADIOS = {
    "Philadelphia Stadium": (39.9008, -75.1675),
    "Monterrey Stadium": (25.6692, -100.2443),
    "Seattle Stadium": (47.5952, -122.3316),
    "Atlanta Stadium": (33.7573, -84.4010),
    "Miami Stadium": (25.9580, -80.2389)
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

def rodar_simulacao_monte_carlo(time_a, time_b, estadio, temp=22, n_simulacoes=50000):
    # 1. Instanciar e ajustar o modelo Dixon-Coles
    model = DixonColesModel(phi=0.0019, reg_lambda=5.0, shrink_lambda=0.1)
    model.fit(JOGOS_CONCLUIDOS)
    
    # 2. Calcular distâncias e fadiga
    lat_s, lon_s = ESTADIOS.get(estadio, (39.0, -94.0)) # default central
    
    lat_a, lon_a = QGS.get(time_a, (39.0, -94.0))
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    
    lat_b, lon_b = QGS.get(time_b, (39.0, -94.0))
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    # Supor descanso padrão de 4 dias se não especificado
    rest_a = 5 if time_a == "Costa do Marfim" else 4
    rest_b = 4
    
    # 3. Obter matriz de probabilidades e médias de gols (lambdas) ajustados
    P_matrix, lambda_a, lambda_b = model.predict_probabilities(
        time_a, time_b, 
        odds_mercado=None, 
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b
    )
    
    # Flatten da matriz de probabilidade de 6x6 para 36 elementos
    P_flat = P_matrix.flatten()
    
    # 4. Rodar simulações de Monte Carlo
    # Semente aleatória para reprodutibilidade
    np.random.seed(42)
    
    indices_sorteados = np.random.choice(36, p=P_flat, size=n_simulacoes)
    
    # Mapear os índices 1D de volta para (gols_a, gols_b)
    gols_a_simulados = indices_sorteados // 6
    gols_b_simulados = indices_sorteados % 6
    
    # 5. Analisar resultados das simulações
    vitorias_a = np.sum(gols_a_simulados > gols_b_simulados)
    empates = np.sum(gols_a_simulados == gols_b_simulados)
    vitorias_b = np.sum(gols_a_simulados < gols_b_simulados)
    
    p_vitoria_a = (vitorias_a / n_simulacoes) * 100
    p_empate = (empates / n_simulacoes) * 100
    p_vitoria_b = (vitorias_b / n_simulacoes) * 100
    
    # Contagem de placares exatos
    placares_counts = {}
    for ga, gb in zip(gols_a_simulados, gols_b_simulados):
        placar = (ga, gb)
        placares_counts[placar] = placares_counts.get(placar, 0) + 1
        
    placares_ordenados = sorted(placares_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Apresentar resultados
    print("=" * 70)
    print(f" SIMULAÇÃO MONTE CARLO ({n_simulacoes:,} Ensaios) ")
    print(f" Confronto: {time_a} vs. {time_b}")
    print(f" Sede/Estádio: {estadio} (Temp: {temp}°C)")
    print(f" Distâncias de Viagem: {time_a} ({dist_a:.0f} km) | {time_b} ({dist_b:.0f} km)")
    print(f" Gols Esperados (Lambdas Ajustados): {time_a} ({lambda_a:.3f}) | {time_b} ({lambda_b:.3f})")
    print("=" * 70)
    print("PROBABILIDADES DOS RESULTADOS:")
    print(f" -> Vitória do(a) {time_a}: {p_vitoria_a:.2f}% ({vitorias_a:,} simulações)")
    print(f" -> Empate: {p_empate:.2f}% ({empates:,} simulações)")
    print(f" -> Vitória do(a) {time_b}: {p_vitoria_b:.2f}% ({vitorias_b:,} simulações)")
    print("-" * 70)
    print("TOP 5 PLACARES EXATOS MAIS FREQUENTES:")
    for i, (placar, count) in enumerate(placares_ordenados[:5], 1):
        prob = (count / n_simulacoes) * 100
        print(f" {i}. Placar: {placar[0]} x {placar[1]} | Frequência: {prob:.2f}% ({count:,} vezes)")
    print("-" * 70)
    print(f"Média de Gols Simulada: {np.mean(gols_a_simulados):.3f} vs. {np.mean(gols_b_simulados):.3f}")
    print("=" * 70)

if __name__ == "__main__":
    # Executa simulações para os próximos confrontos
    # 1. Costa do Marfim vs. Equador
    rodar_simulacao_monte_carlo("Costa do Marfim", "Equador", "Philadelphia Stadium", temp=28)
    
    # 2. Suécia vs. Tunísia
    rodar_simulacao_monte_carlo("Suécia", "Tunísia", "Monterrey Stadium", temp=30)
