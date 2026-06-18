path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Tabela: Portugal vs RD Congo
old_portugal_table = "| **K** | 🇵🇹 Portugal vs. RD Congo 🇨🇩 | Houston Stadium (Houston) | Preditivo | **2 x 0** | **Média** |"
new_portugal_table = "| **K** | 🇵🇹 Portugal vs. RD Congo 🇨🇩 | Houston Stadium (Houston) | *Concluído* | **2 x 0 (Erro)** | **Média (Confirmado)** |"
content = content.replace(old_portugal_table, new_portugal_table)

# 2. Tabela: Uzbequistão vs Colômbia
old_colombia_table = "| **K** | 🇺🇿 Uzbequistão vs. Colômbia 🇨🇴 | Mexico City Stadium (C. do México) | Preditivo | **0 x 2** | **Média** |"
new_colombia_table = "| **K** | 🇺🇿 Uzbequistão vs. Colômbia 🇨🇴 | Mexico City Stadium (C. do México) | *Concluído* | **0 x 2 (Erro Placar / Acerto Seco)** | **Média (Confirmado)** |"
content = content.replace(old_colombia_table, new_colombia_table)

# 3. Tabela: Inglaterra vs Croácia
old_inglaterra_table = "| **L** | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra vs. Croácia 🇭🇷 | Dallas Stadium (Arlington) | Preditivo | **2 x 0** | **Média** |"
new_inglaterra_table = "| **L** | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra vs. Croácia 🇭🇷 | Dallas Stadium (Arlington) | *Concluído* | **2 x 0 (Erro Placar / Acerto Seco)** | **Média (Confirmado)** |"
content = content.replace(old_inglaterra_table, new_inglaterra_table)

# 4. Tabela: Gana vs Panamá
old_gana_table = "| **L** | 🇬🇭 Gana vs. Panamá 🇵🇦 | Toronto Stadium (Toronto) | Preditivo | **1 x 0** | **Média** |"
new_gana_table = "| **L** | 🇬🇭 Gana vs. Panamá 🇵🇦 | Toronto Stadium (Toronto) | *Concluído* | **1 x 0 (Acerto)** | **Média (Confirmado)** |"
content = content.replace(old_gana_table, new_gana_table)


# 5. Detalhe: Portugal vs RD Congo
old_portugal_detail = """*   **Portugal 2 x 0 RD Congo**
    *   **Estádio:** Houston Stadium (Houston)
    *   **Status:** Preditivo (17 de junho)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.01 pts) para o bolão. Lambdas ajustados pelo Disparity Boost: 2.32 x 0.62.
    *   **Nível de Confiança:** Média"""

new_portugal_detail = """*   **Portugal 2 x 0 RD Congo**
    *   **Estádio:** Houston Stadium (Houston)
    *   **Status:** Concluído (17 de junho) - Real: **1 x 1**
    *   **Justificativa:** O RD Congo confirmou sua disciplina tática defensiva, anulando o ímpeto técnico português. João Neves abriu o placar, mas Wissa garantiu o empate histórico congolês, quebrando a expectativa de vitória seca de Portugal.
    *   **Nível de Confiança:** Média (Erro)"""
content = content.replace(old_portugal_detail, new_portugal_detail)

# 6. Detalhe: Uzbequistão vs Colômbia
old_colombia_detail = """*   **Uzbequistão 0 x 2 Colômbia**
    *   **Estádio:** Mexico City Stadium (C. do México)
    *   **Status:** Preditivo (17 de junho)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.82 pts) para o bolão. Lambdas ajustados pelo Disparity Boost: 0.65 x 1.66.
    *   **Nível de Confiança:** Média"""

new_colombia_detail = """*   **Uzbequistão 0 x 2 Colômbia**
    *   **Estádio:** Mexico City Stadium (C. do México)
    *   **Status:** Concluído (17 de junho) - Real: **1 x 3**
    *   **Justificativa:** A Colômbia dominou a partida em alta intensidade e venceu por 3 a 1 na altitude do Azteca. O palpite de 0x2 garantiu o acerto do vencedor no bolão (15 pontos).
    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)"""
content = content.replace(old_colombia_detail, new_colombia_detail)

# 7. Detalhe: Inglaterra vs Croácia
old_inglaterra_detail = """*   **Inglaterra 2 x 0 Croácia**
    *   **Estádio:** Dallas Stadium (Arlington)
    *   **Status:** Preditivo (17 de junho)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.60 pts) para o bolão. Lambdas ajustados pelo Disparity Boost: 1.67 x 0.81.
    *   **Nível de Confiança:** Média"""

new_inglaterra_detail = """*   **Inglaterra 2 x 0 Croácia**
    *   **Estádio:** Dallas Stadium (Arlington)
    *   **Status:** Concluído (17 de junho) - Real: **4 x 2**
    *   **Justificativa:** Harry Kane liderou o ataque inglês com dois gols na emocionante vitória por 4 a 2 em Dallas. O palpite de 2x0 garantiu a vitória inglesa seca no bolão (15 pontos).
    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)"""
content = content.replace(old_inglaterra_detail, new_inglaterra_detail)

# 8. Detalhe: Gana vs Panamá
old_gana_detail = """*   **Gana 1 x 0 Panamá**
    *   **Estádio:** Toronto Stadium (Toronto)
    *   **Status:** Preditivo (17 de junho)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.58 pts) para o bolão. Lambdas ajustados pelo Disparity Boost: 1.17 x 0.96.
    *   **Nível de Confiança:** Média"""

new_gana_detail = """*   **Gana 1 x 0 Panamá**
    *   **Estádio:** Toronto Stadium (Toronto)
    *   **Status:** Concluído (17 de junho) - Real: **1 x 0**
    *   **Justificativa:** O palpite otimizado por EV de 1x0 foi cravado com precisão absoluta! Gana conquistou a vitória magra com gol de Yirenkyi nos acréscimos, garantindo a pontuação máxima de 30 pontos no bolão.
    *   **Nível de Confiança:** Média (Acerto de Placar e Resultado)"""
content = content.replace(old_gana_detail, new_gana_detail)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Relatório de Rodada 1 finalizado!")
