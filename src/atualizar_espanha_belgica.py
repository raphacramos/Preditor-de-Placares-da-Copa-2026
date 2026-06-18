path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Tabela: Bélgica vs Egito
old_belgica_table = "| **G** | 🇧🇪 Bélgica vs. Egito 🇪🇬 | Seattle Stadium (Seattle) | Preditivo | **1 x 1** | **Média** |"
new_belgica_table = "| **G** | 🇧🇪 Bélgica vs. Egito 🇪🇬 | Seattle Stadium (Seattle) | *Concluído* | **1 x 1 (Acerto)** | **Média (Confirmado)** |"
content = content.replace(old_belgica_table, new_belgica_table)

# 2. Tabela: Espanha vs Cabo Verde
old_espanha_table = "| **H** | 🇪🇸 Espanha vs. Cabo Verde 🇨🇻 | Atlanta Stadium (Atlanta) | Preditivo | **2 x 0** | **Média** |"
new_espanha_table = "| **H** | 🇪🇸 Espanha vs. Cabo Verde 🇨🇻 | Atlanta Stadium (Atlanta) | *Concluído* | **2 x 0 (Erro)** | **Média (Confirmado)** |"
content = content.replace(old_espanha_table, new_espanha_table)

# 3. Detalhe: Bélgica vs Egito
old_belgica_detail = """*   **Bélgica 1 x 1 Egito**
    *   **Estádio:** Seattle Stadium (Seattle)
    *   **Status:** Preditivo (15 de junho)
    *   **Justificativa:** Modelo calibrado com as distâncias de QG (15 km vs. 368 km), dias de descanso e temperatura local (18°C). Lambdas ajustados: 1.24 x 1.01.
    *   **Nível de Confiança:** Média"""

new_belgica_detail = """*   **Bélgica 1 x 1 Egito**
    *   **Estádio:** Seattle Stadium (Seattle)
    *   **Status:** Concluído (15 de junho) - Real: **1 x 1**
    *   **Justificativa:** O modelo previu com perfeição o empate em 1 a 1, capturando a paridade logística e o desgaste físico de ambas as equipes. O Egito saiu na frente, mas a Bélgica arrancou o empate no segundo tempo.
    *   **Nível de Confiança:** Média (Acerto de Placar e Resultado)"""
content = content.replace(old_belgica_detail, new_belgica_detail)

# 4. Detalhe: Espanha vs Cabo Verde
old_espanha_detail = """*   **Espanha 2 x 0 Cabo Verde**
    *   **Estádio:** Atlanta Stadium (Atlanta)
    *   **Status:** Preditivo (15 de junho)
    *   **Justificativa:** Modelo calibrado com as distâncias de QG (166 km vs. 672 km), dias de descanso e temperatura local (24°C). Lambdas ajustados: 2.79 x 0.55.
    *   **Nível de Confiança:** Média"""

new_espanha_detail = """*   **Espanha 2 x 0 Cabo Verde**
    *   **Estádio:** Atlanta Stadium (Atlanta)
    *   **Status:** Concluído (15 de junho) - Real: **0 x 0**
    *   **Justificativa:** A Espanha teve amplo domínio de posse e chances criadas (conforme o xG projetado de 2.79), mas esbarrou em uma partida histórica do goleiro cabo-verdiano Vozinha. A retranca extrema e a eficácia defensiva de Cabo Verde travaram o placar em 0x0, superando os ajustes do modelo pré-jogo.
    *   **Nível de Confiança:** Média (Erro)"""
content = content.replace(old_espanha_detail, new_espanha_detail)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Relatório atualizado com os resultados de Espanha e Bélgica!")
