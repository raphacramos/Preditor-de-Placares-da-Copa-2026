import re

ESTADIOS_JOGOS = {
    ("México", "África do Sul"): "Mexico City Stadium (C. do México)",
    ("Coreia do Sul", "Tchéquia"): "Guadalajara Stadium (Guadalajara)",
    ("Canadá", "Bósnia e Herzegovina"): "Toronto Stadium (Toronto)",
    ("Catar", "Suíça"): "San Francisco Bay Stadium (S. Clara)",
    ("Brasil", "Marrocos"): "New York New Jersey Stadium (East Rutherford)",
    ("Haiti", "Escócia"): "Boston Stadium (Foxborough)",
    ("EUA", "Paraguai"): "Los Angeles Stadium (Inglewood)",
    ("Austrália", "Turquia"): "Vancouver Stadium (Vancouver)",
    ("Alemanha", "Curaçao"): "Houston Stadium (Houston)",
    ("Costa do Marfim", "Equador"): "Philadelphia Stadium (Filadélfia)",
    ("Holanda", "Japão"): "Dallas Stadium (Arlington)",
    ("Suécia", "Tunísia"): "Monterrey Stadium (Guadalupe)",
    ("Bélgica", "Egito"): "Seattle Stadium (Seattle)",
    ("Irã", "Nova Zelândia"): "Los Angeles Stadium (Inglewood)",
    ("Espanha", "Cabo Verde"): "Atlanta Stadium (Atlanta)",
    ("Uruguai", "Arábia Saudita"): "Miami Stadium (Miami Gardens)",
    ("França", "Senegal"): "New York New Jersey Stadium (East Rutherford)",
    ("Iraque", "Noruega"): "Boston Stadium (Foxborough)",
    ("Argentina", "Argélia"): "Kansas City Stadium (Kansas City)",
    ("Áustria", "Jordânia"): "Dallas Stadium (Arlington)",
    ("Portugal", "RD Congo"): "Houston Stadium (Houston)",
    ("Uzbequistão", "Colômbia"): "Mexico City Stadium (C. do México)",
    ("Inglaterra", "Croácia"): "Dallas Stadium (Arlington)",
    ("Gana", "Panamá"): "Toronto Stadium (Toronto)"
}

path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_table = False

for line in lines:
    # Atualiza o cabeçalho da tabela
    if "| Grupo | Confronto | Status |" in line:
        line = line.replace("| Grupo | Confronto | Status |", "| Grupo | Confronto | Local / Estádio | Status |")
        new_lines.append(line)
        in_table = True
        continue
    elif in_table and "| :---: | :--- | :---: |" in line:
        line = line.replace("| :---: | :--- | :---: |", "| :---: | :--- | :--- | :---: |")
        new_lines.append(line)
        continue
    
    # Processa linhas da tabela de jogos
    if in_table and line.startswith("|"):
        # Verifica se a tabela terminou
        if line.strip() == "":
            in_table = False
            new_lines.append(line)
            continue
        
        parts = [p.strip() for p in line.split("|")]
        # Formato esperado: ['', 'Grupo', 'Confronto', 'Status', 'Palpite', 'Confiança', '']
        if len(parts) >= 6:
            confronto = parts[2]
            estadio_encontrado = "Desconhecido"
            for (t1, t2), est in ESTADIOS_JOGOS.items():
                # Normaliza nomes dos times para busca
                t1_clean = t1.lower()
                t2_clean = t2.lower()
                conf_clean = confronto.lower()
                if t1_clean in conf_clean and t2_clean in conf_clean:
                    estadio_encontrado = est
                    break
                # Trata casos como Coreia do Sul (Korea Republic) ou Turquia/Tchéquia
                if "coreia" in conf_clean and t1 == "Coreia do Sul":
                    if t2_clean in conf_clean or "tch" in conf_clean:
                        estadio_encontrado = est
                        break
            
            # Insere a nova coluna
            parts.insert(3, estadio_encontrado)
            line = " | ".join(parts).strip() + "\n"
            # Garante barras corretas no início e fim
            if not line.startswith("|"):
                line = "| " + line
            if not line.endswith("|\n"):
                line = line.rstrip() + " |\n"
            new_lines.append(line)
            continue

    # Processa linhas fora da tabela (detalhes jogo a jogo)
    new_lines.append(line)
    
    # Se for o título de um confronto
    if line.startswith("*   **") and "vs." in line or " x " in line:
        # Encontra o estádio correspondente
        estadio_encontrado = None
        line_clean = line.lower()
        for (t1, t2), est in ESTADIOS_JOGOS.items():
            t1_clean = t1.lower()
            t2_clean = t2.lower()
            if t1_clean in line_clean and t2_clean in line_clean:
                estadio_encontrado = est
                break
            if "coreia" in line_clean and t1 == "Coreia do Sul":
                if t2_clean in line_clean or "tch" in line_clean:
                    estadio_encontrado = est
                    break
        
        if estadio_encontrado:
            new_lines.append(f"    *   **Estádio:** {estadio_encontrado}\n")

with open(path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Relatório atualizado com sucesso!")
