path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Tabela: Uruguai vs Arábia Saudita
old_uruguai_table = "| **H** | 🇺🇾 Uruguai vs. Arábia Saudita 🇸🇦 | Miami Stadium (Miami Gardens) | Preditivo | **2 x 0** | **Média** |"
new_uruguai_table = "| **H** | 🇺🇾 Uruguai vs. Arábia Saudita 🇸🇦 | Miami Stadium (Miami Gardens) | *Concluído* | **2 x 0 (Erro)** | **Média (Confirmado)** |"
content = content.replace(old_uruguai_table, new_uruguai_table)

# 2. Tabela: Irã vs Nova Zelândia
old_ira_table = "| **G** | 🇮🇷 Irã vs. Nova Zelândia 🇳🇿 | Los Angeles Stadium (Inglewood) | Preditivo | **1 x 0** | **Alta** |"
new_ira_table = "| **G** | 🇮🇷 Irã vs. Nova Zelândia 🇳🇿 | Los Angeles Stadium (Inglewood) | *Concluído* | **1 x 0 (Erro)** | **Alta (Confirmado)** |"
content = content.replace(old_ira_table, new_ira_table)

# 3. Detalhe: Uruguai vs Arábia Saudita
old_uruguai_detail = """*   **Uruguai 2 x 0 Arábia Saudita**
    *   **Estádio:** Miami Stadium (Miami Gardens)
    *   **Status:** Preditivo (15 de junho)
    *   **Justificativa:** Modelo calibrado com as distâncias de QG (915 km vs. 1780 km), dias de descanso e temperatura local (28°C). Lambdas ajustados: 2.39 x 0.56.
    *   **Nível de Confiança:** Média"""

new_uruguai_detail = """*   **Uruguai 2 x 0 Arábia Saudita**
    *   **Estádio:** Miami Stadium (Miami Gardens)
    *   **Status:** Concluído (15 de junho) - Real: **1 x 1**
    *   **Justificativa:** Apesar do amplo favoritismo uruguaio no xG (2.39 contra 0.56), a Arábia Saudita aproveitou uma falha aérea para marcar com Al-Amri. Maxi Araújo empatou para o Uruguai, mas o ferrolho defensivo saudita impediu a virada, resultando em mais um empate inesperado na rodada.
    *   **Nível de Confiança:** Média (Erro)"""
content = content.replace(old_uruguai_detail, new_uruguai_detail)

# 4. Detalhe: Irã vs Nova Zelândia
old_ira_detail = """*   **Irã 1 x 0 Nova Zelândia**
    *   **Estádio:** Los Angeles Stadium (Inglewood)
    *   **Status:** Preditivo (15 de junho)
    *   **Justificativa:** Modelo calibrado com as distâncias de QG (201 km vs. 176 km), dias de descanso e temperatura local (22°C). Lambdas ajustados: 1.27 x 0.49.
    *   **Nível de Confiança:** Alta"""

new_ira_detail = """*   **Irã 1 x 0 Nova Zelândia**
    *   **Estádio:** Los Angeles Stadium (Inglewood)
    *   **Status:** Concluído (15 de junho) - Real: **2 x 2**
    *   **Justificativa:** Uma partida frenética e aberta contrariou as expectativas de gols baixos. Elijah Just marcou duas vezes para a Nova Zelândia, forçando o Irã a sair para o jogo e buscar o empate com Rezaeian e Mohebi, quebrando o teto tático e gerando um placar elástico.
    *   **Nível de Confiança:** Alta (Erro)"""
content = content.replace(old_ira_detail, new_ira_detail)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Relatório atualizado com os resultados de Uruguai e Irã!")
