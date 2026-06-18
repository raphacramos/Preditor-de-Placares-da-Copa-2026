path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Atualiza a linha da tabela
old_table_line = "| **F** | 🇸🇪 Suécia vs. Tunísia 🇹🇳 | Monterrey Stadium (Guadalupe) | Preditivo | **1 x 0** | **Média** |"
new_table_line = "| **F** | 🇸🇪 Suécia vs. Tunísia 🇹🇳 | Monterrey Stadium (Guadalupe) | *Concluído* | **1 x 0 (Erro Placar / Acerto Seco)** | **Média (Realizado)** |"

content = content.replace(old_table_line, new_table_line)

# Atualiza o detalhamento do jogo
old_detail = """*   **Suécia 1 x 0 Tunísia**
    *   **Estádio:** Monterrey Stadium (Guadalupe)
    *   **Status:** Preditivo (15 de junho)
    *   **Justificativa:** Modelo calibrado com as distâncias de QG (858 km vs. 7 km), dias de descanso e temperatura local (30°C). Lambdas ajustados: 1.23 x 0.64.
    *   **Nível de Confiança:** Média"""

new_detail = """*   **Suécia 1 x 0 Tunísia**
    *   **Estádio:** Monterrey Stadium (Guadalupe)
    *   **Status:** Concluído (14 de junho) - Real: **5 x 1**
    *   **Justificativa:** A Suécia confirmou a vitória seca (Acerto Seco), mas o placar foi um blowout atípico de 5x1. O gol precoce de Ayari (7') forçou a Tunísia a abrir seu bloco defensivo muito cedo, permitindo que a dupla de elite Isak e Gyökeres explorasse as transições rápidas e pulverizasse o teto defensivo projetado pelo modelo.
    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)"""

content = content.replace(old_detail, new_detail)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Status do jogo da Suécia atualizado para 5x1!")
