path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Corrige a linha da tabela
old_table_line = "| **E** | 🇨🇮 Costa do Marfim vs. Equador 🇪🇨 | Philadelphia Stadium (Filadélfia) | *Concluído* | **1 x 1 (Erro Placar / Acerto Seco)** | **Média (Realizado)** |"
new_table_line = "| **E** | 🇨🇮 Costa do Marfim vs. Equador 🇪🇨 | Philadelphia Stadium (Filadélfia) | *Concluído* | **1 x 1 (Erro)** | **Média (Realizado)** |"

content = content.replace(old_table_line, new_table_line)

# Corrige o detalhamento do jogo
old_detail = """*   **Costa do Marfim 1 x 1 Equador**
    *   **Estádio:** Philadelphia Stadium (Filadélfia)
    *   **Status:** Concluído (14 de junho) - Real: **0 x 0**
    *   **Justificativa:** O confronto físico e o desgaste logístico do Equador (que viajou 666 km contra apenas 17 km da Costa do Marfim) neutralizaram as chances criadas. O palpite original de 1x1 garantiu o empate seco, mas o novo modelo híbrido recalibrado projetou com sucesso o placar exato de 0x0 como a maior probabilidade (17.1%).
    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)"""

new_detail = """*   **Costa do Marfim 1 x 1 Equador**
    *   **Estádio:** Philadelphia Stadium (Filadélfia)
    *   **Status:** Concluído (14 de junho) - Real: **1 x 0**
    *   **Justificativa:** O confronto físico e o desgaste logístico do Equador (que viajou 666 km contra apenas 17 km da Costa do Marfim) tornaram o jogo extremamente truncado. No entanto, o cansaço equatoriano na reta final permitiu que a Costa do Marfim marcasse o gol da vitória aos 44' do segundo tempo com Amad Diallo. O palpite original de 1x1 falhou (Erro) ao não prever a vitória tardia marfinesa.
    *   **Nível de Confiança:** Média (Erro)"""

content = content.replace(old_detail, new_detail)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Relatório corrigido com o placar de 1x0!")
