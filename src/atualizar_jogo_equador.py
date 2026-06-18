path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Atualiza a linha da tabela
old_table_line = "| **E** | 🇨🇮 Costa do Marfim vs. Equador 🇪🇨 | Philadelphia Stadium (Filadélfia) | *Em Andamento* | **1 x 1** | **Média** |"
new_table_line = "| **E** | 🇨🇮 Costa do Marfim vs. Equador 🇪🇨 | Philadelphia Stadium (Filadélfia) | *Concluído* | **1 x 1 (Erro Placar / Acerto Seco)** | **Média (Realizado)** |"

content = content.replace(old_table_line, new_table_line)

# Atualiza o detalhamento do jogo
old_detail = """*   **Costa do Marfim 1 x 1 Equador**
    *   **Estádio:** Philadelphia Stadium (Filadélfia)
    *   **Status:** Preditivo (14 de junho)
    *   **Justificativa:** Um dos duelos mais equilibrados e físicos da 1ª rodada. A Costa do Marfim (campeã da Copa Africana) tem meio-campo vigoroso com Kessié, enquanto o Equador de Moisés Caicedo e Hincapié é extremamente veloz na transição e agressivo na marcação. Tendência de empate tático.
    *   **Nível de Confiança:** Média"""

new_detail = """*   **Costa do Marfim 1 x 1 Equador**
    *   **Estádio:** Philadelphia Stadium (Filadélfia)
    *   **Status:** Concluído (14 de junho) - Real: **0 x 0**
    *   **Justificativa:** O confronto físico e o desgaste logístico do Equador (que viajou 666 km contra apenas 17 km da Costa do Marfim) neutralizaram as chances criadas. O palpite original de 1x1 garantiu o empate seco, mas o novo modelo híbrido recalibrado projetou com sucesso o placar exato de 0x0 como a maior probabilidade (17.1%).
    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)"""

content = content.replace(old_detail, new_detail)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Status do jogo atualizado!")
