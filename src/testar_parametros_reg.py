import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS

def testar(reg_l, shrink_l):
    model = DixonColesModel(phi=0.0019, reg_lambda=reg_l, shrink_lambda=shrink_l)
    model.fit(JOGOS_CONCLUIDOS)
    
    # Próximos jogos
    jogos = [
        ("Espanha", "Cabo Verde"),
        ("Uruguai", "Arábia Saudita"),
        ("Argentina", "Argélia"),
        ("Portugal", "RD Congo")
    ]
    print(f"--- reg_lambda={reg_l}, shrink_lambda={shrink_l} ---")
    for t_a, t_b in jogos:
        res = model.get_top_scores(t_a, t_b)
        top_placar = res["top_3_placares"][0][0]
        prob_placar = res["top_3_placares"][0][1]
        print(f" {t_a} vs. {t_b}: {top_placar} ({prob_placar}) | Lambdas: {res['lambda_a']} x {res['lambda_b']}")

testar(1.0, 0.5)  # Atual
testar(5.0, 0.1)  # Nova proposta
testar(10.0, 0.05) # Outra opção
