path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = 0

for i, line in enumerate(lines):
    if skip > 0:
        skip -= 1
        continue
        
    new_lines.append(line)
    
    if "*   **Suécia 1 x 0 Tunísia**" in line:
        # Substitui os próximos 4 bullet points (Estádio, Status, Justificativa, Confiança)
        # Verifica se as próximas linhas são de fato os bullet points
        if "Estádio" in lines[i+1]:
            new_lines.append(lines[i+1]) # Mantém estádio
            new_lines.append("    *   **Status:** Concluído (14 de junho) - Real: **5 x 1**\n")
            new_lines.append("    *   **Justificativa:** A Suécia confirmou a vitória seca (Acerto Seco), mas o placar foi um blowout atípico de 5x1. O gol precoce de Ayari (7') forçou a Tunísia a abrir seu bloco defensivo muito cedo, permitindo que a dupla de elite Isak e Gyökeres explorasse as transições rápidas e pulverizasse o teto defensivo projetado pelo modelo.\n")
            new_lines.append("    *   **Nível de Confiança:** Média (Acerto Seco / Erro de Placar)\n")
            skip = 4

with open(path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Relatório atualizado robustamente!")
