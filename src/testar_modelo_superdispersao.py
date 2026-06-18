import math
import numpy as np

# Copia do modelo atual para teste local com modificações
# Vamos testar o impacto da Binomial Negativa e da Disparidade de Elenco

BASE_PRIORS = {
    "Alemanha": (1.85, 0.80),
    "Curaçao": (0.65, 1.80),
    "Suécia": (1.40, 0.85),
    "Tunísia": (0.90, 1.05),
    "Espanha": (2.05, 0.70),
    "Cabo Verde": (0.95, 1.10)
}

def negative_binomial_pmf(lmbda, k, r=3.0):
    """Calcula a PMF da Binomial Negativa com parâmetro de dispersão r."""
    if lmbda <= 0:
        return 1.0 if k == 0 else 0.0
    p = lmbda / (r + lmbda)
    # Coeficiente binomial para float
    coeff = math.gamma(k + r) / (math.gamma(k + 1) * math.gamma(r))
    return coeff * math.pow(1 - p, r) * math.pow(p, k)

def dixon_coles_tau(x, y, lambda_a, lambda_b, rho):
    if x == 0 and y == 0:
        return 1.0 - lambda_a * lambda_b * rho
    elif x == 0 and y == 1:
        return 1.0 + lambda_a * rho
    elif x == 1 and y == 0:
        return 1.0 + lambda_b * rho
    elif x == 1 and y == 1:
        return 1.0 - rho
    return 1.0

def testar_confronto(time_a, time_b, base_lambda_a, base_lambda_b, usar_superdispersao=True):
    lambda_a = base_lambda_a
    lambda_b = base_lambda_b
    
    # Coeficiente de Disparidade de Elenco (Disparity Boost)
    # Se a diferença de qualidade for alta, aplicamos um boost não-linear no favorito
    ratio = lambda_a / lambda_b if lambda_a > lambda_b else lambda_b / lambda_a
    
    if ratio > 1.8:
        boost = 1.0 + 0.18 * (ratio - 1.8)
        if lambda_a > lambda_b:
            lambda_a *= boost
            # underdog desmorona defensivamente
            lambda_b *= 0.90
        else:
            lambda_b *= boost
            lambda_a *= 0.90
            
    print(f"\n--- {time_a} vs. {time_b} (Ratio: {ratio:.2f}) ---")
    print(f" Lambdas Iniciais: {base_lambda_a:.2f} x {base_lambda_b:.2f}")
    print(f" Lambdas Ajustados (Disparity): {lambda_a:.2f} x {lambda_b:.2f}")
    
    # 1. Matriz de Probabilidade (Poisson vs Binomial Negativa)
    P_poi = np.zeros((6, 6))
    P_nb = np.zeros((6, 6))
    rho = -0.15
    
    for x in range(6):
        for y in range(6):
            # Poisson
            p_a_poi = (math.pow(lambda_a, x) * math.exp(-lambda_a)) / math.factorial(x)
            p_b_poi = (math.pow(lambda_b, y) * math.exp(-lambda_b)) / math.factorial(y)
            tau_poi = dixon_coles_tau(x, y, lambda_a, lambda_b, rho)
            P_poi[x, y] = max(tau_poi * p_a_poi * p_b_poi, 0.0)
            
            # Binomial Negativa
            p_a_nb = negative_binomial_pmf(lambda_a, x, r=3.5)
            p_b_nb = negative_binomial_pmf(lambda_b, y, r=3.5)
            tau_nb = dixon_coles_tau(x, y, lambda_a, lambda_b, rho)
            P_nb[x, y] = max(tau_nb * p_a_nb * p_b_nb, 0.0)
            
    P_poi /= np.sum(P_poi)
    P_nb /= np.sum(P_nb)
    
    # Ordenar e mostrar top 3 placares
    def get_top_3(P):
        placares = []
        for x in range(6):
            for y in range(6):
                placares.append(((x, y), P[x, y]))
        return sorted(placares, key=lambda x: x[1], reverse=True)[:3]
        
    print(" -> POISSON:")
    for placar, prob in get_top_3(P_poi):
        print(f"    Placar: {placar[0]} x {placar[1]} | Probabilidade: {prob*100:.2f}%")
        
    print(" -> BINOMIAL NEGATIVA (Superdispersão):")
    for placar, prob in get_top_3(P_nb):
        print(f"    Placar: {placar[0]} x {placar[1]} | Probabilidade: {prob*100:.2f}%")

# Teste 1: Alemanha vs Curaçao (Prior base: 1.85 * 1.80 = 3.33 vs 0.65 * 0.80 = 0.52)
# Real: 7x1
testar_confronto("Alemanha", "Curaçao", 3.33, 0.52)

# Teste 2: Suécia vs Tunísia (Prior sintonizado: 1.36 vs 0.71)
# Real: 5x1
testar_confronto("Suécia", "Tunísia", 1.36, 0.71)

# Teste 3: Espanha vs Cabo Verde (Prior sintonizado: 1.94 vs 0.57)
testar_confronto("Espanha", "Cabo Verde", 1.94, 0.57)
