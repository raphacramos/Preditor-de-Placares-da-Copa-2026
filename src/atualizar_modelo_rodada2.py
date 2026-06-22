import re
import os

# Caminhos dos arquivos modelo_avancado_copa.py (relativo para o repo e absoluto para o scratch do agente)
paths = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), "modelo_avancado_copa.py")),
    "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/scratch/modelo_avancado_copa.py"
]

# Novos 16 jogos concluídos da 2ª rodada
novos_jogos = [
    {"time_a": "Tchéquia", "time_b": "África do Sul", "gols_a": 1, "gols_b": 1, "dias_atras": 4, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "México", "time_b": "Coreia do Sul", "gols_a": 1, "gols_b": 0, "dias_atras": 4, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "Suíça", "time_b": "Bósnia e Herzegovina", "gols_a": 4, "gols_b": 1, "dias_atras": 4, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Canadá", "time_b": "Catar", "gols_a": 6, "gols_b": 0, "dias_atras": 4, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "Escócia", "time_b": "Marrocos", "gols_a": 0, "gols_b": 1, "dias_atras": 3, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Brasil", "time_b": "Haiti", "gols_a": 3, "gols_b": 0, "dias_atras": 3, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "EUA", "time_b": "Austrália", "gols_a": 2, "gols_b": 0, "dias_atras": 3, "e_co_host_a": True, "e_co_host_b": False},
    {"time_a": "Turquia", "time_b": "Paraguai", "gols_a": 0, "gols_b": 1, "dias_atras": 3, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Alemanha", "time_b": "Costa do Marfim", "gols_a": 2, "gols_b": 1, "dias_atras": 2, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Equador", "time_b": "Curaçao", "gols_a": 0, "gols_b": 0, "dias_atras": 2, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Holanda", "time_b": "Suécia", "gols_a": 5, "gols_b": 1, "dias_atras": 2, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Tunísia", "time_b": "Japão", "gols_a": 0, "gols_b": 4, "dias_atras": 2, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Bélgica", "time_b": "Irã", "gols_a": 0, "gols_b": 0, "dias_atras": 1, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Nova Zelândia", "time_b": "Egito", "gols_a": 1, "gols_b": 3, "dias_atras": 1, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Espanha", "time_b": "Arábia Saudita", "gols_a": 4, "gols_b": 0, "dias_atras": 1, "e_co_host_a": False, "e_co_host_b": False},
    {"time_a": "Uruguai", "time_b": "Cabo Verde", "gols_a": 2, "gols_b": 2, "dias_atras": 1, "e_co_host_a": False, "e_co_host_b": False}
]

for p in paths:
    if not os.path.exists(p):
        print(f"Arquivo não encontrado: {p}")
        continue
        
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Encontra a declaração do vetor JOGOS_CONCLUIDOS
    match_vec = re.search(r"JOGOS_CONCLUIDOS\s*=\s*\[(.*?)\]", content, re.DOTALL)
    if not match_vec:
        print(f"Não foi possível encontrar JOGOS_CONCLUIDOS em {p}")
        continue
        
    inner_content = match_vec.group(1)
    
    # Extrai cada jogo como dicionário usando eval
    jogos_existentes = []
    # Divide os dicionários
    dict_strings = re.findall(r"\{.*?\}", inner_content)
    for ds in dict_strings:
        try:
            j = eval(ds)
            # Soma +4 no dias_atras de cada jogo já concluído
            j["dias_atras"] += 4
            jogos_existentes.append(j)
        except Exception as e:
            print(f"Erro ao processar dicionário {ds}: {e}")
            
    # Combina existentes e novos
    todos_jogos = jogos_existentes + novos_jogos
    
    # Formata a nova string do vetor de forma legível
    formatted_games = "JOGOS_CONCLUIDOS = [\n"
    for i, j in enumerate(todos_jogos):
        line = f"    {{\"time_a\": \"{j['time_a']}\", \"time_b\": \"{j['time_b']}\", \"gols_a\": {j['gols_a']}, \"gols_b\": {j['gols_b']}, \"dias_atras\": {j['dias_atras']}, \"e_co_host_a\": {j['e_co_host_a']}, \"e_co_host_b\": {j['e_co_host_b']}}}"
        if i < len(todos_jogos) - 1:
            line += ",\n"
        else:
            line += "\n"
        formatted_games += line
    formatted_games += "]"
    
    # Substitui no arquivo original
    new_content = content.replace(match_vec.group(0), formatted_games)
    
    with open(p, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Arquivo {p} atualizado com sucesso!")
