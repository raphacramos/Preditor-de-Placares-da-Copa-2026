import math
import numpy as np
import scipy.optimize as opt
import pandas as pd
from datetime import datetime

# Priors de ataque (alpha) e defesa (beta) de linha de base para as 48 seleções
BASE_PRIORS = {
    # Grupo A
    "México": (1.35, 0.85),
    "África do Sul": (0.95, 1.15),
    "Coreia do Sul": (1.25, 0.90),
    "Tchéquia": (1.15, 0.95),
    # Grupo B
    "Canadá": (1.20, 0.95),
    "Bósnia e Herzegovina": (0.95, 1.10),
    "Catar": (0.95, 1.20),
    "Suíça": (1.30, 0.85),
    # Grupo C
    "Brasil": (1.90, 0.85),
    "Marrocos": (1.40, 0.75),
    "Haiti": (0.70, 1.55),
    "Escócia": (1.10, 0.95),
    # Grupo D
    "EUA": (1.40, 0.90),
    "Paraguai": (0.95, 0.85),
    "Austrália": (1.10, 0.90),
    "Turquia": (1.35, 0.95),
    # Grupo E
    "Alemanha": (1.85, 0.80),
    "Curaçao": (0.65, 1.80),
    "Costa do Marfim": (1.25, 0.90),
    "Equador": (1.20, 0.85),
    # Grupo F
    "Holanda": (1.65, 0.80),
    "Japão": (1.45, 0.85),
    "Suécia": (1.40, 0.85),
    "Tunísia": (0.90, 1.05),
    # Grupo G
    "Bélgica": (1.55, 0.90),
    "Egito": (1.20, 0.85),
    "Irã": (1.05, 0.90),
    "Nova Zelândia": (0.75, 1.40),
    # Grupo H
    "Espanha": (2.05, 0.70),
    "Cabo Verde": (0.95, 1.10),
    "Arábia Saudita": (0.90, 1.15),
    "Uruguai": (1.70, 0.80),
    # Grupo I
    "França": (2.10, 0.70),
    "Senegal": (1.30, 0.85),
    "Iraque": (0.85, 1.25),
    "Noruega": (1.30, 0.95),
    # Grupo J
    "Argentina": (2.00, 0.70),
    "Argélia": (1.15, 1.00),
    "Áustria": (1.35, 0.85),
    "Jordânia": (0.80, 1.35),
    # Grupo K
    "Portugal": (1.95, 0.75),
    "RD Congo": (0.95, 1.10),
    "Uzbequistão": (1.00, 1.00),
    "Colômbia": (1.60, 0.80),
    # Grupo L
    "Inglaterra": (1.95, 0.75),
    "Croácia": (1.35, 0.85),
    "Gana": (1.10, 1.10),
    "Panamá": (0.95, 1.15)
}

# Jogos concluídos até o momento (Copa do Mundo 2026)
JOGOS_CONCLUIDOS = [
    {"time_a": "México", "time_b": "África do Sul", "gols_a": 2, "gols_b": 0, "dias_atras": 11, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "Coreia do Sul", "time_b": "Tchéquia", "gols_a": 2, "gols_b": 1, "dias_atras": 10, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Canadá", "time_b": "Bósnia e Herzegovina", "gols_a": 1, "gols_b": 1, "dias_atras": 10, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "EUA", "time_b": "Paraguai", "gols_a": 4, "gols_b": 1, "dias_atras": 10, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "Catar", "time_b": "Suíça", "gols_a": 1, "gols_b": 1, "dias_atras": 9, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Brasil", "time_b": "Marrocos", "gols_a": 1, "gols_b": 1, "dias_atras": 9, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Austrália", "time_b": "Turquia", "gols_a": 2, "gols_b": 0, "dias_atras": 8, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Haiti", "time_b": "Escócia", "gols_a": 0, "gols_b": 1, "dias_atras": 8, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Alemanha", "time_b": "Curaçao", "gols_a": 7, "gols_b": 1, "dias_atras": 8, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Holanda", "time_b": "Japão", "gols_a": 2, "gols_b": 2, "dias_atras": 8, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Costa do Marfim", "time_b": "Equador", "gols_a": 1, "gols_b": 0, "dias_atras": 8, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Suécia", "time_b": "Tunísia", "gols_a": 5, "gols_b": 1, "dias_atras": 8, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Espanha", "time_b": "Cabo Verde", "gols_a": 0, "gols_b": 0, "dias_atras": 7, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Bélgica", "time_b": "Egito", "gols_a": 1, "gols_b": 1, "dias_atras": 7, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Uruguai", "time_b": "Arábia Saudita", "gols_a": 1, "gols_b": 1, "dias_atras": 7, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Irã", "time_b": "Nova Zelândia", "gols_a": 2, "gols_b": 2, "dias_atras": 7, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "França", "time_b": "Senegal", "gols_a": 3, "gols_b": 1, "dias_atras": 6, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Iraque", "time_b": "Noruega", "gols_a": 1, "gols_b": 4, "dias_atras": 6, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Argentina", "time_b": "Argélia", "gols_a": 3, "gols_b": 0, "dias_atras": 6, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Áustria", "time_b": "Jordânia", "gols_a": 3, "gols_b": 1, "dias_atras": 6, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Portugal", "time_b": "RD Congo", "gols_a": 1, "gols_b": 1, "dias_atras": 5, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Uzbequistão", "time_b": "Colômbia", "gols_a": 1, "gols_b": 3, "dias_atras": 5, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Inglaterra", "time_b": "Croácia", "gols_a": 4, "gols_b": 2, "dias_atras": 5, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Gana", "time_b": "Panamá", "gols_a": 1, "gols_b": 0, "dias_atras": 5, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Tchéquia", "time_b": "África do Sul", "gols_a": 1, "gols_b": 1, "dias_atras": 4, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "México", "time_b": "Coreia do Sul", "gols_a": 1, "gols_b": 0, "dias_atras": 4, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "Suíça", "time_b": "Bósnia e Herzegovina", "gols_a": 4, "gols_b": 1, "dias_atras": 4, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Canadá", "time_b": "Catar", "gols_a": 6, "gols_b": 0, "dias_atras": 4, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "Escócia", "time_b": "Marrocos", "gols_a": 0, "gols_b": 1, "dias_atras": 3, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Brasil", "time_b": "Haiti", "gols_a": 3, "gols_b": 0, "dias_atras": 3, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "EUA", "time_b": "Austrália", "gols_a": 2, "gols_b": 0, "dias_atras": 3, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "Turquia", "time_b": "Paraguai", "gols_a": 0, "gols_b": 1, "dias_atras": 3, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Alemanha", "time_b": "Costa do Marfim", "gols_a": 2, "gols_b": 1, "dias_atras": 2, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Equador", "time_b": "Curaçao", "gols_a": 0, "gols_b": 0, "dias_atras": 2, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Holanda", "time_b": "Suécia", "gols_a": 5, "gols_b": 1, "dias_atras": 2, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Tunísia", "time_b": "Japão", "gols_a": 0, "gols_b": 4, "dias_atras": 2, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Bélgica", "time_b": "Irã", "gols_a": 0, "gols_b": 0, "dias_atras": 1, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Nova Zelândia", "time_b": "Egito", "gols_a": 1, "gols_b": 3, "dias_atras": 1, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Espanha", "time_b": "Arábia Saudita", "gols_a": 4, "gols_b": 0, "dias_atras": 1, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Uruguai", "time_b": "Cabo Verde", "gols_a": 2, "gols_b": 2, "dias_atras": 1, "e_co_host_a": False, "e_co_host_b": False}
]

CO_HOSTS = ["EUA", "México", "Canadá"]

def poisson_pmf(lmbda, k):
    if lmbda <= 0:
        return 1.0 if k == 0 else 0.0
    return (math.pow(lmbda, k) * math.exp(-lmbda)) / math.factorial(k)

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

class PiRatingSystem:
    """Implementa o sistema de classificação dinâmica Pi-Ratings (Constantinou & Fenton, 2013)."""
    def __init__(self, learning_rate=0.07, gamma_cross=0.4):
        self.learning_rate = learning_rate
        self.gamma_cross = gamma_cross  # Influência de cruzamento entre ratings de casa e fora
        self.teams = sorted(list(BASE_PRIORS.keys()))
        self.home_ratings = {t: 0.0 for t in self.teams}
        self.away_ratings = {t: 0.0 for t in self.teams}
        
    def fit(self, matches):
        """Atualiza iterativamente as habilidades de casa e fora das equipes."""
        for match in matches:
            t_a = match["time_a"]
            t_b = match["time_b"]
            goals_a = match["gols_a"]
            goals_b = match["gols_b"]
            
            d_hat = self.home_ratings[t_a] - self.away_ratings[t_b]
            d = goals_a - goals_b
            
            # Margem de gols transformada logaritmicamente (retornos decrescentes)
            d_prime = np.sign(d) * 3.0 * math.log10(1 + abs(d))
            
            # Discrepância / Erro
            e = d_prime - d_hat
            
            # Atualização de Ratings (Soma-Zero)
            self.home_ratings[t_a] += self.learning_rate * e
            self.away_ratings[t_b] -= self.learning_rate * e
            
            # Atualização cruzada de localidade
            self.away_ratings[t_a] += self.learning_rate * self.gamma_cross * e
            self.home_ratings[t_b] -= self.learning_rate * self.gamma_cross * e

class DixonColesModel:
    def __init__(self, phi=0.0019, reg_lambda=1.5, shrink_lambda=0.1):
        self.phi = phi
        self.reg_lambda = reg_lambda  # Regularização L2 para aproximar dos Priors
        self.shrink_lambda = shrink_lambda  # Regularização bayesiana de encolhimento (Shrinkage) para a média 1.0
        self.teams = sorted(list(BASE_PRIORS.keys()))
        self.num_teams = len(self.teams)
        self.team_to_idx = {t: i for i, t in enumerate(self.teams)}
        
        # Parâmetros padrão
        self.alphas = np.array([BASE_PRIORS[t][0] for t in self.teams])
        self.betas = np.array([BASE_PRIORS[t][1] for t in self.teams])
        self.rho = -0.10
        self.gamma = 1.15
        self.mu = 1.35  # Multiplicador global de volume de gols (média de gols por time)
        
        # Instancia Pi-Ratings
        self.pi_system = PiRatingSystem()
        
    def fit(self, matches):
        # 1. Calcula os ratings Pi-Ratings com base nas partidas passadas
        self.pi_system.fit(matches)
        
        # 2. Ajusta dinamicamente os priors usando a performance real (Pi-Ratings)
        # Ratings positivos aumentam o ataque prior e diminuem a vulnerabilidade de defesa
        adjusted_priors = {}
        for t in self.teams:
            base_alpha, base_beta = BASE_PRIORS[t]
            rating_avg = (self.pi_system.home_ratings[t] + self.pi_system.away_ratings[t]) / 2.0
            
            # Mapeamento linear conservador
            prior_alpha = base_alpha + 0.12 * rating_avg
            prior_beta = max(base_beta - 0.08 * rating_avg, 0.3)
            adjusted_priors[t] = (prior_alpha, prior_beta)
            
        initial_params = np.zeros(2 * self.num_teams + 3)
        initial_params[:self.num_teams] = self.alphas
        initial_params[self.num_teams:2*self.num_teams] = self.betas
        initial_params[-3] = self.rho
        initial_params[-2] = self.gamma
        initial_params[-1] = self.mu
        
        def negative_log_likelihood(params):
            alphas = params[:self.num_teams]
            betas = params[self.num_teams:2*self.num_teams]
            rho = params[-3]
            gamma = params[-2]
            mu = params[-1]
            
            log_lik = 0.0
            for match in matches:
                t_a, t_b = match["time_a"], match["time_b"]
                goals_a, goals_b = match["gols_a"], match["gols_b"]
                dt = match.get("dias_atras", 0)
                w = math.exp(-self.phi * dt)
                
                idx_a = self.team_to_idx[t_a]
                idx_b = self.team_to_idx[t_b]
                
                factor_a = gamma if match.get("e_co_host_a", False) else 1.0
                factor_b = gamma if match.get("e_co_host_b", False) else 1.0
                
                lambda_a = mu * alphas[idx_a] * betas[idx_b] * factor_a
                lambda_b = mu * alphas[idx_b] * betas[idx_a] * factor_b
                
                p_ind_a = poisson_pmf(lambda_a, goals_a)
                p_ind_b = poisson_pmf(lambda_b, goals_b)
                p_independent = p_ind_a * p_ind_b
                
                tau = dixon_coles_tau(goals_a, goals_b, lambda_a, lambda_b, rho)
                prob_final = max(tau * p_independent, 1e-10)
                log_lik += w * math.log(prob_final)
                
            # A) Regularização L2 em relação aos priors dinâmicos do Pi-Ratings
            reg_penalty = 0.0
            for i, t in enumerate(self.teams):
                prior_alpha, prior_beta = adjusted_priors[t]
                reg_penalty += (alphas[i] - prior_alpha) ** 2
                reg_penalty += (betas[i] - prior_beta) ** 2
                
            # B) Regularização Hierárquica Bayesiana (Encolhimento à média 1.0)
            shrink_penalty = 0.0
            for i in range(self.num_teams):
                shrink_penalty += (alphas[i] - 1.0) ** 2
                shrink_penalty += (betas[i] - 1.0) ** 2
                
            # Restrições de média = 1.0 para alphas e betas (identificação do modelo e papel correto de mu)
            constraint_penalty = 100.0 * (np.mean(alphas) - 1.0) ** 2 + 100.0 * (np.mean(betas) - 1.0) ** 2
            
            return -log_lik + self.reg_lambda * reg_penalty + self.shrink_lambda * shrink_penalty + constraint_penalty

        bounds = [(0.1, 4.0)] * self.num_teams + [(0.1, 4.0)] * self.num_teams + [(-0.15, 0.0), (1.0, 1.25), (0.8, 2.5)]
        res = opt.minimize(negative_log_likelihood, initial_params, method="L-BFGS-B", bounds=bounds)
        
        if res.success:
            self.alphas = res.x[:self.num_teams]
            self.betas = res.x[self.num_teams:2*self.num_teams]
            self.rho = res.x[-3]
            self.gamma = res.x[-2]
            self.mu = res.x[-1]
            return True
        return False

    def predict_probabilities(self, time_a, time_b, odds_mercado=None, w_modelo=0.60,
                                distancia_a=0, rest_a=4, temp=20,
                                distancia_b=0, rest_b=4):
        """
        Gera as probabilidades incluindo o Índice de Fadiga Logística (delta)
        e a mesclagem bayesiana com odds de mercado.
        """
        idx_a = self.team_to_idx[time_a]
        idx_b = self.team_to_idx[time_b]
        
        factor_a = self.gamma if time_a in CO_HOSTS else 1.0
        factor_b = self.gamma if time_b in CO_HOSTS else 1.0
        
        # Força base de gols esperada do Dixon-Coles (inclui mu)
        lambda_a = self.mu * self.alphas[idx_a] * self.betas[idx_b] * factor_a
        lambda_b = self.mu * self.alphas[idx_b] * self.betas[idx_a] * factor_b
        
        # 1. Aplicação do Índice Dinâmico de Fadiga (delta)
        fatiga_a = (distancia_a / 1000.0) - rest_a + max(temp - 20, 0) / 10.0
        fatiga_b = (distancia_b / 1000.0) - rest_b + max(temp - 20, 0) / 10.0
        
        # Fator delta restrito a um intervalo realista [0.85, 1.15] para estabilidade
        delta_a = max(min(math.exp(-0.06 * fatiga_a), 1.15), 0.85)
        delta_b = max(min(math.exp(-0.06 * fatiga_b), 1.15), 0.85)
        
        # Fadiga relativa afeta o ataque próprio e beneficia a defesa adversária
        lambda_a *= (delta_a / delta_b)
        lambda_b *= (delta_b / delta_a)
        
        # 2. Coeficiente de Disparidade de Elenco (Disparity Boost) - limitado a 1.5 para estabilidade
        ratio = lambda_a / lambda_b if lambda_a > lambda_b else lambda_b / lambda_a
        if ratio > 1.8:
            boost = min(1.0 + 0.18 * (ratio - 1.8), 1.5)
            if lambda_a > lambda_b:
                lambda_a *= boost
                lambda_b *= 0.90
            else:
                lambda_b *= boost
                lambda_a *= 0.90
        
        # 2. Matriz Dixon-Coles
        P_model = np.zeros((6, 6))
        for x in range(6):
            for y in range(6):
                p_a = poisson_pmf(lambda_a, x)
                p_b = poisson_pmf(lambda_b, y)
                tau = dixon_coles_tau(x, y, lambda_a, lambda_b, self.rho)
                P_model[x, y] = max(tau * p_a * p_b, 0.0)
                
        P_model /= np.sum(P_model)
        
        # 3. Mesclagem Bayesiana com Odds
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
            
        return P_final, lambda_a, lambda_b

    def get_top_scores(self, time_a, time_b, odds_mercado=None, w_modelo=0.60,
                       distancia_a=0, rest_a=4, temp=20,
                       distancia_b=0, rest_b=4):
        P, la, lb = self.predict_probabilities(time_a, time_b, odds_mercado, w_modelo,
                                               distancia_a, rest_a, temp,
                                               distancia_b, rest_b)
        prob_win_a = 0.0
        prob_draw = 0.0
        prob_win_b = 0.0
        
        placares = []
        for x in range(6):
            for y in range(6):
                prob = P[x, y]
                placares.append(((x, y), prob))
                if x > y:
                    prob_win_a += prob
                elif x == y:
                    prob_draw += prob
                else:
                    prob_win_b += prob
                    
        placares_ordenados = sorted(placares, key=lambda val: val[1], reverse=True)
        best_placar, best_prob = placares_ordenados[0]
        
        if best_prob >= 0.16:
            conf = "Alta"
        elif best_prob >= 0.11:
            conf = "Média"
        else:
            conf = "Baixa"
            
        return {
            "confronto": f"{time_a} vs. {time_b}",
            "lambda_a": round(la, 2),
            "lambda_b": round(lb, 2),
            "prob_resultado": {
                "vitoria_a": f"{prob_win_a * 100:.1f}%",
                "empate": f"{prob_draw * 100:.1f}%",
                "vitoria_b": f"{prob_win_b * 100:.1f}%"
            },
            "top_3_placares": [
                (f"{p[0][0]} x {p[0][1]}", f"{p[1] * 100:.2f}%") for p in placares_ordenados[:3]
            ],
            "confianca_placar": conf
        }

if __name__ == "__main__":
    print("=" * 60)
    print(" MODELO HÍBRIDO DE ELITE (PI-RATINGS + DIXON-COLES) CONVERGIDO ")
    print("=" * 60)
    
    model = DixonColesModel(phi=0.0019, reg_lambda=5.0, shrink_lambda=0.1)
    sucesso = model.fit(JOGOS_CONCLUIDOS)
    print(f"Treinamento do Modelo: {'Sucesso' if sucesso else 'Falha'}")
    print(f"Parâmetro Dixon-Coles (rho): {model.rho:.4f}")
    print(f"Fator Casa Otimizado (gamma): {model.gamma:.4f}")
    print("-" * 60)
    
    # Exemplo: Simular Costa do Marfim vs. Equador aplicando o Índice de Fadiga
    # Costa do Marfim: viajou 800km, 5 dias de descanso
    # Equador: viajou 1800km (cansaço maior), 4 dias de descanso
    # Temperatura no jogo: 28°C (calor acentuado)
    res = model.get_top_scores(
        "Costa do Marfim", "Equador",
        odds_mercado={"vitoria_a": 2.60, "empate": 3.00, "vitoria_b": 2.65},
        w_modelo=0.60,
        distancia_a=800, rest_a=5, temp=28,
        distancia_b=1800, rest_b=4
    )
    
    print(f"Jogo: {res['confronto']} (Com Índice de Fadiga Logística)")
    print(f"Médias de Gols Finais: Costa do Marfim ({res['lambda_a']}) | Equador ({res['lambda_b']})")
    print(f"Probabilidades: Vitória A: {res['prob_resultado']['vitoria_a']} | Empate: {res['prob_resultado']['empate']} | Vitória B: {res['prob_resultado']['vitoria_b']}")
    print("Top 3 Placares:")
    for placar, prob in res['top_3_placares']:
        print(f" -> Placar: {placar} | Probabilidade: {prob}")
    print(f"Confiança: {res['confianca_placar']}")
    print("=" * 60)
