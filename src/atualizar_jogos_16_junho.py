path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Tabela: França vs Senegal
old_franca_table = "| **I** | 🇫🇷 França vs. Senegal 🇸🇳 | New York New Jersey Stadium (East Rutherford) | Preditivo | **2 x 0** | **Média** |"
new_franca_table = "| **I** | 🇫🇷 França vs. Senegal 🇸🇳 | New York New Jersey Stadium (East Rutherford) | *Concluído* | **2 x 0 (Erro Placar / Acerto Seco)** | **Média (Confirmado)** |"
content = content.replace(old_franca_table, new_franca_table)

# 2. Tabela: Iraque vs Noruega
old_iraque_table = "| **I** | 🇮🇶 Iraque vs. Noruega 🇳🇴 | Boston Stadium (Foxborough) | Preditivo | **0 x 2** | **Média** |"
new_iraque_table = "| **I** | 🇮🇶 Iraque vs. Noruega 🇳🇴 | Boston Stadium (Foxborough) | *Concluído* | **0 x 2 (Erro Placar / Acerto Seco)** | **Média (Confirmado)** |"
content = content.replace(old_iraque_table, new_iraque_table)

# 3. Tabela: Argentina vs Argélia
old_argentina_table = "| **J** | 🇦🇷 Argentina vs. Argélia 🇩🇿 | Kansas City Stadium (Kansas City) | Preditivo | **2 x 0** | **Média** |"
new_argentina_table = "| **J** | 🇦🇷 Argentina vs. Argélia 🇩🇿 | Kansas City Stadium (Kansas City) | *Concluído* | **2 x 0 (Erro Placar / Acerto Seco)** | **Média (Confirmado)** |"
content = content.replace(old_argentina_table, new_argentina_table)

# 4. Tabela: Áustria vs Jordânia
old_austria_table = "| **J** | 🇦🇹 Áustria vs. Jordânia 🇯🇴 | Dallas Stadium (Arlington) | Preditivo | **2 x 0** | **Alta** |"
new_austria_table = "| **J** | 🇦🇹 Áustria vs. Jordânia 🇯🇴 | Dallas Stadium (Arlington) | *Concluído* | **2 x 0 (Erro Placar / Acerto Seco)** | **Alta (Confirmado)** |"
content = content.replace(old_austria_table, new_austria_table)


# 5. Detalhe: França vs Senegal
old_franca_detail = """*   **França 2 x 0 Senegal**
    *   **Estádio:** New York New Jersey Stadium (East Rutherford)
    *   **Status:** Preditivo (16 de junho)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.20 pts) para o bolão. Lambdas ajustados pelo Disparity Boost: 1.76 x 0.77.
    *   **Nível de Confiança:** Média"""

new_franca_detail = """*   **França 2 x 0 Senegal**
    *   **Estádio:** New York New Jersey Stadium (East Rutherford)
    *   **Status:** Concluído (16 de junho) - Real: **3 x 1**
    *   **Justificativa:** A França confirmou o favoritismo e venceu a partida por dois gols de diferença. Mbappé anotou duas vezes e Barcola marcou o terceiro, enquanto Mbaye diminuiu para o Senegal. O palpite otimizado garantiu o acerto do vencedor seco (15 pontos).
    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)"""
content = content.replace(old_franca_detail, new_franca_detail)

# 6. Detalhe: Iraque vs Noruega
old_iraque_detail = """*   **Iraque 0 x 2 Noruega**
    *   **Estádio:** Boston Stadium (Foxborough)
    *   **Status:** Preditivo (16 de junho)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.10 pts) para o bolão. Lambdas ajustados pelo Disparity Boost: 0.66 x 1.58.
    *   **Nível de Confiança:** Média"""

new_iraque_detail = """*   **Iraque 0 x 2 Noruega**
    *   **Estádio:** Boston Stadium (Foxborough)
    *   **Status:** Concluído (16 de junho) - Real: **1 x 4**
    *   **Justificativa:** A Noruega atropelou o Iraque com grande atuação de Haaland, que marcou duas vezes. Østigård e um gol contra de Hussein selaram o placar de 4 a 1. O palpite de 0x2 garantiu a vitória norueguesa seca no bolão (15 pontos).
    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)"""
content = content.replace(old_iraque_detail, new_iraque_detail)

# 7. Detalhe: Argentina vs Argélia
old_argentina_detail = """*   **Argentina 2 x 0 Argélia**
    *   **Estádio:** Kansas City Stadium (Kansas City)
    *   **Status:** Preditivo (16 de junho)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.98 pts) para o bolão. Lambdas ajustados pelo Disparity Boost: 2.15 x 0.68.
    *   **Nível de Confiança:** Média"""

new_argentina_detail = """*   **Argentina 2 x 0 Argélia**
    *   **Estádio:** Kansas City Stadium (Kansas City)
    *   **Status:** Concluído (16 de junho) - Real: **3 x 0**
    *   **Justificativa:** Show de Lionel Messi, que marcou os três gols da partida. A Argentina dominou por completo e manteve a zaga sem sofrer gols, selando o 3x0. Garantido o acerto do vencedor no bolão (15 pontos).
    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)"""
content = content.replace(old_argentina_detail, new_argentina_detail)

# 8. Detalhe: Áustria vs Jordânia
old_austria_detail = """*   **Áustria 2 x 0 Jordânia**
    *   **Estádio:** Dallas Stadium (Arlington)
    *   **Status:** Preditivo (16 de junho)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.67 pts) para o bolão. Lambdas ajustados pelo Disparity Boost: 2.1 x 0.54.
    *   **Nível de Confiança:** Alta"""

new_austria_detail = """*   **Áustria 2 x 0 Jordânia**
    *   **Estádio:** Dallas Stadium (Arlington)
    *   **Status:** Concluído (16 de junho) - Real: **3 x 1**
    *   **Justificativa:** A Áustria confirmou sua superioridade em Arlington vencendo por 3 a 1, com gols de Schmid, Arnautovic e um gol contra de Al Arab. O palpite de 2x0 garantiu a vitória seca da Áustria no bolão (15 pontos).
    *   **Nível de Confiança:** Alta (Acerto Seco / Erro de Placar)"""
content = content.replace(old_austria_detail, new_austria_detail)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Relatório atualizado com os resultados de 16 de junho!")
