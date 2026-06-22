import sys
import os
import math
import numpy as np

# Adiciona o diretório atual ao path para importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from aplicar_novos_palpites_rodada2 import model, ESTADIOS, QGS, ULTIMO_JOGO, ODDS_MERCADO, haversine, calcular_pontos, JOGOS_CONCLUIDOS

# 16 jogos que já aconteceram com seus palpites originais e resultados reais
jogos_concluidos_detalhes = [
    {
        "grupo": "A", "time_a": "Tchéquia", "time_b": "África do Sul", "stadium": "Atlanta Stadium", "dia_jogo": "18/Jun", "temp": 24,
        "pred_a": 2, "pred_b": 0, "real_a": 1, "real_b": 1, "confianca": "Média", "ev_orig": 9.96,
        "recap": "A África do Sul surpreendeu ao segurar a Tchéquia em um empate de 1 a 1, contrariando o favoritismo do modelo que projetava maior volume ofensivo europeu. O empate quebrou o palpite seco de vitória da Tchéquia."
    },
    {
        "grupo": "A", "time_a": "México", "time_b": "Coreia do Sul", "stadium": "Mexico City Stadium", "dia_jogo": "18/Jun", "temp": 20,
        "pred_a": 2, "pred_b": 1, "real_a": 1, "real_b": 0, "confianca": "Média", "ev_orig": 9.24,
        "recap": "O México soube utilizar o fator altitude e o apoio massivo no Estádio Azteca para vencer a Coreia do Sul por 1 a 0. O palpite de 2x1 garantiu 15 pontos de vitória seca no bolão."
    },
    {
        "grupo": "B", "time_a": "Suíça", "time_b": "Bósnia e Herzegovina", "stadium": "Los Angeles Stadium", "dia_jogo": "18/Jun", "temp": 22,
        "pred_a": 2, "pred_b": 0, "real_a": 4, "real_b": 1, "confianca": "Média", "ev_orig": 8.99,
        "recap": "A Suíça impôs um ritmo ofensivo avassalador, superando com facilidade a defesa bósnia por 4 a 1. O palpite de 2x0 garantiu a vitória seca da Suíça (15 pontos)."
    },
    {
        "grupo": "B", "time_a": "Canadá", "time_b": "Catar", "stadium": "Vancouver Stadium", "dia_jogo": "18/Jun", "temp": 18,
        "pred_a": 2, "pred_b": 1, "real_a": 6, "real_b": 0, "confianca": "Média", "ev_orig": 11.14,
        "recap": "Jogando em Vancouver, o Canadá aplicou uma goleada histórica de 6 a 0 sobre o Catar, confirmando ampla superioridade técnica. O palpite seco de vitória canadense rendeu 15 pontos."
    },
    {
        "grupo": "C", "time_a": "Escócia", "time_b": "Marrocos", "stadium": "Boston Stadium", "dia_jogo": "19/Jun", "temp": 20,
        "pred_a": 0, "pred_b": 2, "real_a": 0, "real_b": 1, "confianca": "Média", "ev_orig": 11.32,
        "recap": "Marrocos confirmou seu favoritismo com uma vitória taticamente muito madura por 1 a 0 sobre a Escócia. O palpite de 0x2 assegurou os 15 pontos do vencedor no bolão."
    },
    {
        "grupo": "C", "time_a": "Brasil", "time_b": "Haiti", "stadium": "Philadelphia Stadium", "dia_jogo": "19/Jun", "temp": 24,
        "pred_a": 4, "pred_b": 0, "real_a": 3, "real_b": 0, "confianca": "Alta", "ev_orig": 17.80,
        "recap": "O Brasil dominou completamente a partida na Filadélfia e venceu por 3 a 0. O palpite de 4x0 garantiu os 15 pontos de vitória seca do Brasil."
    },
    {
        "grupo": "D", "time_a": "EUA", "time_b": "Austrália", "stadium": "Seattle Stadium", "dia_jogo": "19/Jun", "temp": 18,
        "pred_a": 2, "pred_b": 1, "real_a": 2, "real_b": 0, "confianca": "Média", "ev_orig": 8.33,
        "recap": "Os EUA venceram por 2 a 0 em Seattle, demonstrando excelente solidez defensiva. Como o palpite foi 2x1, houve o acerto do vencedor (EUA) e do número exato de gols do vencedor (2), garantindo a pontuação especial de 20 pontos no bolão."
    },
    {
        "grupo": "D", "time_a": "Turquia", "time_b": "Paraguai", "stadium": "San Francisco Bay Stadium", "dia_jogo": "19/Jun", "temp": 22,
        "pred_a": 2, "pred_b": 1, "real_a": 0, "real_b": 1, "confianca": "Média", "ev_orig": 8.35,
        "recap": "O Paraguai neutralizou as principais armas da Turquia e achou o gol da vitória por 1 a 0, contrariando o favoritismo do modelo. Placar de 0 pontos no bolão."
    },
    {
        "grupo": "E", "time_a": "Alemanha", "time_b": "Costa do Marfim", "stadium": "Toronto Stadium", "dia_jogo": "20/Jun", "temp": 18,
        "pred_a": 2, "pred_b": 1, "real_a": 2, "real_b": 1, "confianca": "Média", "ev_orig": 9.21,
        "recap": "PALPITE CRAVADO COM PRECISÃO ABSOLUTA! A Alemanha superou a forte oposição física da Costa do Marfim por 2 a 1, garantindo os 30 pontos de placar exato no bolão."
    },
    {
        "grupo": "E", "time_a": "Equador", "time_b": "Curaçao", "stadium": "Kansas City Stadium", "dia_jogo": "20/Jun", "temp": 24,
        "pred_a": 2, "pred_b": 0, "real_a": 0, "real_b": 0, "confianca": "Média", "ev_orig": 14.64,
        "recap": "Curaçao surpreendeu ao armar uma retranca muito eficiente e segurar o Equador em um empate sem gols, quebrando o favoritismo equatoriano."
    },
    {
        "grupo": "F", "time_a": "Holanda", "time_b": "Suécia", "stadium": "Houston Stadium", "dia_jogo": "20/Jun", "temp": 28,
        "pred_a": 2, "pred_b": 1, "real_a": 5, "real_b": 1, "confianca": "Baixa", "ev_orig": 8.03,
        "recap": "A Holanda passeou em Houston e aplicou uma goleada de 5 a 1 sobre a Suécia. O palpite de 2x1 garantiu 15 pontos para a vitória seca da Holanda."
    },
    {
        "grupo": "F", "time_a": "Tunísia", "time_b": "Japão", "stadium": "Monterrey Stadium", "dia_jogo": "20/Jun", "temp": 30,
        "pred_a": 0, "pred_b": 3, "real_a": 0, "real_b": 4, "confianca": "Baixa", "ev_orig": 12.81,
        "recap": "O Japão sobrou em campo e venceu por 4 a 0 no Monterrey Stadium. O palpite seco de vitória japonesa rendeu 15 pontos no bolão."
    },
    {
        "grupo": "G", "time_a": "Bélgica", "time_b": "Irã", "stadium": "Los Angeles Stadium", "dia_jogo": "21/Jun", "temp": 22,
        "pred_a": 2, "pred_b": 1, "real_a": 0, "real_b": 0, "confianca": "Baixa", "ev_orig": 10.93,
        "recap": "O Irã se defendeu de forma heróica e arrancou um empate em 0 a 0 contra a favorita Bélgica, frustrando as projeções ofensivas e quebrando as previsões do modelo."
    },
    {
        "grupo": "G", "time_a": "Nova Zelândia", "time_b": "Egito", "stadium": "Vancouver Stadium", "dia_jogo": "21/Jun", "temp": 18,
        "pred_a": 0, "pred_b": 2, "real_a": 1, "real_b": 3, "confianca": "Média", "ev_orig": 11.09,
        "recap": "O Egito comandado por Salah venceu com autoridade por 3 a 1, confirmando a vitória seca projetada e rendendo 15 pontos no bolão."
    },
    {
        "grupo": "H", "time_a": "Espanha", "time_b": "Arábia Saudita", "stadium": "Atlanta Stadium", "dia_jogo": "21/Jun", "temp": 24,
        "pred_a": 3, "pred_b": 0, "real_a": 4, "real_b": 0, "confianca": "Média", "ev_orig": 15.36,
        "recap": "A Espanha goleou por 4 a 0, confirmando sua imensa disparidade técnica. O palpite de 3x0 garantiu a vitória seca da Fúria e somou 15 pontos."
    },
    {
        "grupo": "H", "time_a": "Uruguai", "time_b": "Cabo Verde", "stadium": "Miami Stadium", "dia_jogo": "21/Jun", "temp": 28,
        "pred_a": 1, "pred_b": 0, "real_a": 2, "real_b": 2, "confianca": "Alta", "ev_orig": 9.95,
        "recap": "Cabo Verde foi valente e arrancou um empate histórico por 2 a 2 contra o Uruguai em Miami, frustrando os planos celestes e o palpite do modelo."
    }
]

# 8 jogos restantes da 2ª Rodada
jogos_restantes = [
    ("I", "França", "Iraque", "Philadelphia Stadium", 22, 24),
    ("I", "Noruega", "Senegal", "New York New Jersey Stadium", 22, 22),
    ("J", "Argentina", "Áustria", "Dallas Stadium", 22, 26),
    ("J", "Jordânia", "Argélia", "San Francisco Bay Stadium", 22, 22),
    ("K", "Portugal", "Uzbequistão", "Houston Stadium", 23, 28),
    ("K", "Colômbia", "RD Congo", "Guadalajara Stadium", 23, 24),
    ("L", "Inglaterra", "Gana", "Boston Stadium", 23, 20),
    ("L", "Panamá", "Croácia", "Toronto Stadium", 23, 18)
]

total_pontos = 0
exact_hits = 0
winner_goals_hits = 0
winner_seco_hits = 0
errors = 0

for j in jogos_concluidos_detalhes:
    pts = calcular_pontos(j["pred_a"], j["pred_b"], j["real_a"], j["real_b"])
    j["pontos"] = pts
    total_pontos += pts
    if pts == 30:
        exact_hits += 1
        j["outcome_label"] = "Acerto Placar Exato"
    elif pts == 20:
        winner_goals_hits += 1
        j["outcome_label"] = "Acerto Vencedor + Gols do Vencedor"
    elif pts == 15:
        winner_seco_hits += 1
        j["outcome_label"] = "Acerto Vencedor Seco"
    else:
        errors += 1
        j["outcome_label"] = "Erro"

aproveitamento_desfecho = (exact_hits + winner_goals_hits + winner_seco_hits) / len(jogos_concluidos_detalhes) * 100

previsoes_restantes = []
for grupo, t_a, t_b, stadium, dia_jogo, temp in jogos_restantes:
    lat_s, lon_s = ESTADIOS[stadium]
    lat_a, lon_a = QGS[t_a]
    lat_b, lon_b = QGS[t_b]
    
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    rest_a = dia_jogo - ULTIMO_JOGO[t_a]
    rest_b = dia_jogo - ULTIMO_JOGO[t_b]
    
    odds = ODDS_MERCADO.get((t_a, t_b))
    
    P, la, lb = model.predict_probabilities(
        t_a, t_b, odds_mercado=odds, w_modelo=0.60,
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b
    )
    
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
        t_a, t_b, odds_mercado=odds, w_modelo=0.60,
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b
    )
    
    prob_win_a = sum(P[x, y] for x in range(6) for y in range(6) if x > y)
    prob_draw = sum(P[x, y] for x in range(6) for y in range(6) if x == y)
    prob_win_b = sum(P[x, y] for x in range(6) for y in range(6) if x < y)
    
    previsoes_restantes.append({
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

lines = []
lines.append("# 📊 Relatório Preditivo: 2ª Rodada da Copa do Mundo FIFA 2026")
lines.append("")
lines.append(f"Este relatório apresenta a análise estatística e tática atualizada para todas as 24 partidas da segunda rodada da fase de grupos. A metodologia preditiva foi calibrada e otimizada integrando as **odds reais de mercado** (40% de peso) e o modelo Dixon-Coles sintonizado (60% de peso).")
lines.append("")
lines.append("Com as primeiras 16 partidas da rodada 2 já realizadas, o modelo foi recalibrado (com o banco de dados expandido para **40 jogos concluídos** no total). As previsões para as 8 partidas restantes foram geradas com base nesses novos parâmetros calibrados.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 🏆 Painel de Desempenho (Bolão - 2ª Rodada)")
lines.append("")
lines.append(f"- **Partidas Concluídas:** {len(jogos_concluidos_detalhes)}")
lines.append(f"- **Pontuação Total Acumulada:** **{total_pontos} pontos** (média de {total_pontos / len(jogos_concluidos_detalhes):.2f} pts por partida)")
lines.append(f"- **Aproveitamento de Desfecho (Vitória/Empate/Derrota):** **{aproveitamento_desfecho:.1f}%** ({exact_hits + winner_goals_hits + winner_seco_hits} acertos em {len(jogos_concluidos_detalhes)} jogos)")
lines.append(f"  - 🎯 **Acertos de Placar Exato (30 pts):** {exact_hits}")
lines.append(f"  - ⚽ **Acertos de Vencedor + Gols do Vencedor (20 pts):** {winner_goals_hits}")
lines.append(f"  - 👍 **Acertos Secos de Vencedor (15 pts):** {winner_seco_hits}")
lines.append(f"  - ❌ **Erros (0 pts):** {errors}")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 📅 Resumo dos Palpites (Tabela Rápida para o Bolão)")
lines.append("")
lines.append("| Grupo | Confronto | Local / Estádio | Status | Palpite Sugerido | Resultado Real | Pontos Obtidos | Confiança |")
lines.append("| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |")

for j in jogos_concluidos_detalhes:
    match_str = f"{j['time_a']} vs. {j['time_b']}"
    palpite_str = f"**{j['pred_a']} x {j['pred_b']}**"
    real_str = f"**{j['real_a']} x {j['real_b']}**"
    pts_str = f"**{j['pontos']} pts** ({j['outcome_label']})"
    lines.append(f"| **{j['grupo']}** | {match_str} | {j['stadium']} | *Concluído* | {palpite_str} | {real_str} | {pts_str} | **{j['confianca']}** |")

for p in previsoes_restantes:
    match_str = f"{p['time_a']} vs. {p['time_b']}"
    palpite_str = f"**{p['best_placar'][0]} x {p['best_placar'][1]}**"
    lines.append(f"| **{p['grupo']}** | {match_str} | {p['stadium']} | Preditivo | {palpite_str} | - | EV: {p['best_ev']:.2f} pts | **{p['confianca']}** |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## 🔍 Análise Detalhada Jogo a Jogo")
lines.append("")

concluidos_dict = {f"{j['time_a']} vs. {j['time_b']}": j for j in jogos_concluidos_detalhes}
restantes_dict = {f"{r['time_a']} vs. {r['time_b']}": r for r in previsoes_restantes}

confrontos_ordem = [
    ("A", "Tchéquia", "África do Sul"),
    ("A", "México", "Coreia do Sul"),
    ("B", "Suíça", "Bósnia e Herzegovina"),
    ("B", "Canadá", "Catar"),
    ("C", "Escócia", "Marrocos"),
    ("C", "Brasil", "Haiti"),
    ("D", "EUA", "Austrália"),
    ("D", "Turquia", "Paraguai"),
    ("E", "Alemanha", "Costa do Marfim"),
    ("E", "Equador", "Curaçao"),
    ("F", "Holanda", "Suécia"),
    ("F", "Tunísia", "Japão"),
    ("G", "Bélgica", "Irã"),
    ("G", "Nova Zelândia", "Egito"),
    ("H", "Espanha", "Arábia Saudita"),
    ("H", "Uruguai", "Cabo Verde"),
    ("I", "França", "Iraque"),
    ("I", "Noruega", "Senegal"),
    ("J", "Argentina", "Áustria"),
    ("J", "Jordânia", "Argélia"),
    ("K", "Portugal", "Uzbequistão"),
    ("K", "Colômbia", "RD Congo"),
    ("L", "Inglaterra", "Gana"),
    ("L", "Panamá", "Croácia")
]

current_group = ""
for g, ta, tb in confrontos_ordem:
    if g != current_group:
        current_group = g
        lines.append(f"### **Grupo {current_group}**")
        lines.append("")
        
    key = f"{ta} vs. {tb}"
    if key in concluidos_dict:
        j = concluidos_dict[key]
        lines.append(f"*   **{j['time_a']} {j['pred_a']} x {j['pred_b']} {j['time_b']}**")
        lines.append(f"    *   **Estádio:** {j['stadium']} (Temperatura: {j['temp']}°C)")
        lines.append(f"    *   **Status:** Concluído ({j['dia_jogo']}) - Real: **{j['real_a']} x {j['real_b']}**")
        lines.append(f"    *   **Justificativa:** {j['recap']}")
        lines.append(f"    *   **Pontuação:** Pontuação obtida: {j['pontos']} pts ({j['outcome_label']}).")
        lines.append(f"    *   **Nível de Confiança:** {j['confianca']}")
        lines.append("")
    else:
        p = restantes_dict[key]
        placar_str = f"{p['best_placar'][0]} x {p['best_placar'][1]}"
        lines.append(f"*   **{p['time_a']} {placar_str} {p['time_b']}**")
        lines.append(f"    *   **Estádio:** {p['stadium']} (Temperatura: {p['temp']}°C)")
        lines.append(f"    *   **Status:** Preditivo ({p['dia_jogo']}) [Modelo Calibrado com 40 Jogos]")
        
        just = f"Palpite otimizado por Valor Esperado (EV: {p['best_ev']:.2f} pts) sob o modelo Dixon-Coles recalibrado. "
        just += f"Médias de gols projetadas: {p['time_a']} ({p['lambda_a']:.2f}) vs. {p['time_b']} ({p['lambda_b']:.2f}). "
        just += f"Fatores Físicos: {p['time_a']} viajou {p['dist_a']} km com {p['rest_a']} dias de descanso; "
        just += f"{p['time_b']} viajou {p['dist_b']} km com {p['rest_b']} dias de descanso. "
        
        ratio = p['lambda_a'] / p['lambda_b'] if p['lambda_a'] > p['lambda_b'] else p['lambda_b'] / p['lambda_a']
        if ratio > 1.8:
            just += "O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. "
        else:
            just += "Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. "
            
        lines.append(f"    *   **Justificativa:** {just}")
        lines.append(f"    *   **Probabilidades:** Vitória {p['time_a']}: {p['prob_win_a']*100:.1f}% | Empate: {p['prob_draw']*100:.1f}% | Vitória {p['time_b']}: {p['prob_win_b']*100:.1f}%")
        lines.append(f"    *   **Top 3 Placares mais Prováveis:** {p['top_3_placares'][0][0]} ({p['top_3_placares'][0][1]}), {p['top_3_placares'][1][0]} ({p['top_3_placares'][1][1]}), {p['top_3_placares'][2][0]} ({p['top_3_placares'][2][1]})")
        lines.append(f"    *   **Nível de Confiança:** {p['confianca']}")
        lines.append("")

output_content = "\n".join(lines)

paths = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../relatorios/palpites_copa_2026_rodada2.md")),
    "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada2.md"
]

for path in paths:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(output_content)
    print(f"Salvo com sucesso em: {path}")
