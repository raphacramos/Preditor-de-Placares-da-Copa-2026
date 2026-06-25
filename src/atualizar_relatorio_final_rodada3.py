import sys
import os
import math
import numpy as np

# Adiciona o diretório atual ao path para importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from aplicar_novos_palpites_rodada3 import model, ESTADIOS, QGS, ULTIMO_JOGO, ODDS_MERCADO, haversine, calcular_pontos, JOGOS_CONCLUIDOS, get_blend_weight, DEFENSIVE_UNDERDOGS

# 8 jogos que já aconteceram com seus palpites originais e resultados reais
jogos_concluidos_detalhes = [
    {
        "grupo": "B", "time_a": "Suíça", "time_b": "Canadá", "stadium": "Vancouver Stadium", "dia_jogo": "24/Jun", "temp": 18,
        "pred_a": 1, "pred_b": 2, "real_a": 2, "real_b": 1, "confianca": "Média", "just_peso": "Duelo Direto Decisivo (w: 0.55)",
        "recap": "A Suíça jogou de forma muito sólida em Vancouver e venceu o Canadá por 2 a 1, superando o favoritismo canadense projetado pelo modelo. Placar de 0 pontos no bolão."
    },
    {
        "grupo": "B", "time_a": "Bósnia e Herzegovina", "time_b": "Catar", "stadium": "Seattle Stadium", "dia_jogo": "24/Jun", "temp": 18,
        "pred_a": 2, "pred_b": 1, "real_a": 3, "real_b": 1, "confianca": "Média", "just_peso": "Duelo Direto Decisivo (w: 0.55)",
        "recap": "A Bósnia impôs sua superioridade técnica e física sobre o Catar, vencendo por 3 a 1. O palpite de 2x1 garantiu 15 pontos de vitória seca."
    },
    {
        "grupo": "C", "time_a": "Escócia", "time_b": "Brasil", "stadium": "Miami Stadium", "dia_jogo": "24/Jun", "temp": 28,
        "pred_a": 0, "pred_b": 2, "real_a": 0, "real_b": 3, "confianca": "Média", "just_peso": "Duelo Direto Decisivo (w: 0.55)",
        "recap": "O Brasil teve atuação de gala sob calor em Miami e bateu a Escócia por 3 a 0. O palpite de 0x2 garantiu o acerto seco de vitória (15 pontos)."
    },
    {
        "grupo": "C", "time_a": "Marrocos", "time_b": "Haiti", "stadium": "Atlanta Stadium", "dia_jogo": "24/Jun", "temp": 24,
        "pred_a": 2, "pred_b": 0, "real_a": 4, "real_b": 2, "confianca": "Alta", "just_peso": "Motivação Assimétrica (w: 0.40)",
        "recap": "Marrocos confirmou seu amplo favoritismo e venceu o Haiti por 4 a 2, gerando 15 pontos de vitória seca no bolão."
    },
    {
        "grupo": "A", "time_a": "Tchéquia", "time_b": "México", "stadium": "Mexico City Stadium", "dia_jogo": "24/Jun", "temp": 20,
        "pred_a": 0, "pred_b": 2, "real_a": 0, "real_b": 3, "confianca": "Alta", "just_peso": "Motivação Assimétrica (w: 0.40)",
        "recap": "O México confirmou sua força como anfitrião e dominou a República Tcheca no Azteca, vencendo por 3 a 0. O palpite seco de vitória mexicana rendeu 15 pontos."
    },
    {
        "grupo": "A", "time_a": "África do Sul", "time_b": "Coreia do Sul", "stadium": "Monterrey Stadium", "dia_jogo": "24/Jun", "temp": 30,
        "pred_a": 0, "pred_b": 2, "real_a": 1, "real_b": 0, "confianca": "Média", "just_peso": "Duelo Direto Decisivo (w: 0.55)",
        "recap": "A África do Sul se defendeu bravamente e bateu a Coreia do Sul por 1 a 0, surpreendendo o favoritismo coreano e resultando em 0 pontos no bolão."
    },
    {
        "grupo": "E", "time_a": "Equador", "time_b": "Alemanha", "stadium": "New York New Jersey Stadium", "dia_jogo": "25/Jun", "temp": 22,
        "pred_a": 0, "pred_b": 2, "real_a": 2, "real_b": 1, "confianca": "Alta", "just_peso": "Motivação Assimétrica (w: 0.40)",
        "recap": "Em confronto de motivação assimétrica, o Equador lutou intensamente e venceu a Alemanha (que já estava qualificada e poupou jogadores) por 2 a 1. Placar de 0 pontos."
    },
    {
        "grupo": "E", "time_a": "Curaçao", "time_b": "Costa do Marfim", "stadium": "Philadelphia Stadium", "dia_jogo": "25/Jun", "temp": 24,
        "pred_a": 0, "pred_b": 3, "real_a": 0, "real_b": 2, "confianca": "Média", "just_peso": "Duelo Direto Decisivo (w: 0.55)",
        "recap": "A Costa do Marfim controlou o jogo e venceu Curaçao por 2 a 0. O palpite de 0x3 garantiu a vitória seca da seleção africana (15 pontos)."
    }
]

# 16 jogos restantes da 3ª Rodada
jogos_restantes = [
    # 25 de Junho
    ("F", "Japão", "Suécia", "Dallas Stadium", 25, 26),
    ("F", "Tunísia", "Holanda", "Kansas City Stadium", 25, 24),
    ("D", "Turquia", "EUA", "Los Angeles Stadium", 25, 22),
    ("D", "Paraguai", "Austrália", "San Francisco Bay Stadium", 25, 22),
    # 26 de Junho
    ("I", "Noruega", "França", "Boston Stadium", 26, 20),
    ("I", "Senegal", "Iraque", "Toronto Stadium", 26, 18),
    ("H", "Cabo Verde", "Arábia Saudita", "Houston Stadium", 26, 28),
    ("H", "Uruguai", "Espanha", "Guadalajara Stadium", 26, 24),
    # 27 de Junho
    ("G", "Egito", "Irã", "Seattle Stadium", 27, 18),
    ("G", "Nova Zelândia", "Bélgica", "Vancouver Stadium", 27, 18),
    ("L", "Panamá", "Inglaterra", "New York New Jersey Stadium", 27, 22),
    ("L", "Croácia", "Gana", "Philadelphia Stadium", 27, 24),
    ("K", "Colômbia", "Portugal", "Miami Stadium", 27, 28),
    ("K", "RD Congo", "Uzbequistão", "Atlanta Stadium", 27, 24),
    ("J", "Argélia", "Áustria", "Kansas City Stadium", 27, 24),
    ("J", "Jordânia", "Argentina", "Dallas Stadium", 27, 26)
]

# Calcula pontos totais e estatísticas dos concluídos
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

# Recalcula as previsões para os 16 jogos restantes usando o modelo calibrado com 56 jogos
model.fit(JOGOS_CONCLUIDOS)

# Aplica novamente o ajuste defensivo
for team in DEFENSIVE_UNDERDOGS:
    if team in model.team_to_idx:
        idx = model.team_to_idx[team]
        model.betas[idx] *= 0.95

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
    
    w_modelo, justificativa_peso = get_blend_weight(t_a, t_b)
    
    P, la, lb = model.predict_probabilities(
        t_a, t_b, odds_mercado=odds, w_modelo=w_modelo,
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b, max_boost=1.30
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
        t_a, t_b, odds_mercado=odds, w_modelo=w_modelo,
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b, max_boost=1.30
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
        "confianca": res["confianca_placar"],
        "justificativa_peso": justificativa_peso,
        "w_modelo": w_modelo
    })

# Monta o Markdown final
lines = []
lines.append("# 📊 Relatório Preditivo: 3ª Rodada da Copa do Mundo FIFA 2026")
lines.append("")
lines.append(f"Este relatório apresenta a análise estatística e tática detalhada para todas as 24 partidas da terceira e última rodada da fase de grupos. A metodologia preditiva foi calibrada e otimizada integrando as **odds reais de mercado** e o modelo Dixon-Coles sintonizado.")
lines.append("")
lines.append(f"Com as primeiras 8 partidas da rodada 3 já realizadas (jogos de 24/Jun e início de 25/Jun), o modelo foi recalibrado (com o banco de dados expandido para **56 jogos concluídos** no total). As previsões para os 16 jogos restantes foram geradas utilizando o modelo calibrado sob esta base expandida.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 🏆 Painel de Desempenho (Bolão - 3ª Rodada Parcial)")
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
lines.append("| Grupo | Confronto | Local / Estádio | Status | Palpite Sugerido | Resultado Real | Pontos Obtidos | Confiança | Contexto de Peso |")
lines.append("| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |")

# Adiciona concluídos na tabela
for j in jogos_concluidos_detalhes:
    match_str = f"{j['time_a']} vs. {j['time_b']}"
    palpite_str = f"**{j['pred_a']} x {j['pred_b']}**"
    real_str = f"**{j['real_a']} x {j['real_b']}**"
    pts_str = f"**{j['pontos']} pts** ({j['outcome_label']})"
    lines.append(f"| **{j['grupo']}** | {match_str} | {j['stadium']} | *Concluído* | {palpite_str} | {real_str} | {pts_str} | **{j['confianca']}** | {j['just_peso']} |")

# Adiciona restantes na tabela
for p in previsoes_restantes:
    match_str = f"{p['time_a']} vs. {p['time_b']}"
    palpite_str = f"**{p['best_placar'][0]} x {p['best_placar'][1]}**"
    lines.append(f"| **{p['grupo']}** | {match_str} | {p['stadium']} | Preditivo | {palpite_str} | - | EV: {p['best_ev']:.2f} pts | **{p['confianca']}** | {p['justificativa_peso']} (w: {p['w_modelo']:.2f}) |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## 🔍 Análise Detalhada Jogo a Jogo")
lines.append("")

concluidos_dict = {f"{j['time_a']} vs. {j['time_b']}": j for j in jogos_concluidos_detalhes}
restantes_dict = {f"{r['time_a']} vs. {r['time_b']}": r for r in previsoes_restantes}

confrontos_ordem = [
    # 24 de Junho
    ("B", "Suíça", "Canadá"),
    ("B", "Bósnia e Herzegovina", "Catar"),
    ("C", "Escócia", "Brasil"),
    ("C", "Marrocos", "Haiti"),
    ("A", "Tchéquia", "México"),
    ("A", "África do Sul", "Coreia do Sul"),
    # 25 de Junho
    ("E", "Equador", "Alemanha"),
    ("E", "Curaçao", "Costa do Marfim"),
    ("F", "Japão", "Suécia"),
    ("F", "Tunísia", "Holanda"),
    ("D", "Turquia", "EUA"),
    ("D", "Paraguai", "Austrália"),
    # 26 de Junho
    ("I", "Noruega", "França"),
    ("I", "Senegal", "Iraque"),
    ("H", "Cabo Verde", "Arábia Saudita"),
    ("H", "Uruguai", "Espanha"),
    # 27 de Junho
    ("G", "Egito", "Irã"),
    ("G", "Nova Zelândia", "Bélgica"),
    ("L", "Panamá", "Inglaterra"),
    ("L", "Croácia", "Gana"),
    ("K", "Colômbia", "Portugal"),
    ("K", "RD Congo", "Uzbequistão"),
    ("J", "Argélia", "Áustria"),
    ("J", "Jordânia", "Argentina")
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
        lines.append(f"    *   **Status:** Preditivo ({p['dia_jogo']}) [Modelo Calibrado com 56 Jogos]")
        
        just = f"Palpite otimizado por Valor Esperado (EV: {p['best_ev']:.2f} pts) sob o modelo Dixon-Coles recalibrado com Blending de {p['w_modelo']*100:.0f}% ({p['justificativa_peso']}). "
        just += f"Médias de gols projetadas: {p['time_a']} ({p['lambda_a']:.2f}) vs. {p['time_b']} ({p['lambda_b']:.2f}). "
        just += f"Fatores Físicos: {p['time_a']} viajou {p['dist_a']} km com {p['rest_a']} dias de descanso; "
        just += f"{p['time_b']} viajou {p['dist_b']} km com {p['rest_b']} dias de descanso. "
        
        if p['time_a'] in DEFENSIVE_UNDERDOGS or p['time_b'] in DEFENSIVE_UNDERDOGS:
            just += "O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto. "
            
        lines.append(f"    *   **Justificativa:** {just}")
        lines.append(f"    *   **Probabilidades:** Vitória {p['time_a']}: {p['prob_win_a']*100:.1f}% | Empate: {p['prob_draw']*100:.1f}% | Vitória {p['time_b']}: {p['prob_win_b']*100:.1f}%")
        lines.append(f"    *   **Top 3 Placares mais Prováveis:** {p['top_3_placares'][0][0]} ({p['top_3_placares'][0][1]}), {p['top_3_placares'][1][0]} ({p['top_3_placares'][1][1]}), {p['top_3_placares'][2][0]} ({p['top_3_placares'][2][1]})")
        lines.append(f"    *   **Nível de Confiança:** {p['confianca']}")
        lines.append("")

output_content = "\n".join(lines)

paths = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../relatorios/palpites_copa_2026_rodada3.md")),
    "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada3.md"
]

for path in paths:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(output_content)
    print(f"Salvo com sucesso em: {path}")
