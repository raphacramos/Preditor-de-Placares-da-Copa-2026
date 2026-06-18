import sys
import os
import math
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS

QGS = {
    "Costa do Marfim": (39.8496, -75.3565),
    "Equador": (40.0125, -82.9861),
    "Suécia": (32.7767, -96.7970),
    "Tunísia": (25.6866, -100.3161),
    "Bélgica": (47.4829, -122.2170),
    "Egito": (47.6588, -117.4260),
    "Irã": (32.5149, -117.0382),
    "Nova Zelândia": (32.7157, -117.1611),
    "Espanha": (35.0456, -85.3097),
    "Cabo Verde": (27.9506, -82.4572),
    "Uruguai": (20.6296, -87.0739),
    "Arábia Saudita": (30.2672, -97.7431),
    "França": (42.3601, -71.0589),
    "Senegal": (40.4862, -74.4518),
    "Iraque": (37.7926, -80.4452),
    "Noruega": (36.0726, -79.7920),
    "Argentina": (39.0997, -94.5786),
    "Argélia": (38.9717, -95.2353),
    "Áustria": (34.4208, -119.6982),
    "Jordânia": (45.5152, -122.6784),
    "Portugal": (26.7153, -80.0534),
    "RD Congo": (29.7604, -95.3698),
    "Uzbequistão": (33.7490, -84.3880),
    "Colômbia": (20.6790, -103.3933),
    "Inglaterra": (39.0997, -94.5786),
    "Croácia": (38.8048, -77.0469),
    "Gana": (41.9220, -71.5489),
    "Panamá": (43.6532, -79.3832)
}

ESTADIOS = {
    "Philadelphia Stadium": (39.9008, -75.1675),
    "Monterrey Stadium": (25.6692, -100.2443),
    "Seattle Stadium": (47.5952, -122.3316),
    "Los Angeles Stadium": (33.9535, -118.3390),
    "Atlanta Stadium": (33.7573, -84.4010),
    "Miami Stadium": (25.9580, -80.2389),
    "New York New Jersey Stadium": (40.8135, -74.0744),
    "Boston Stadium": (42.0909, -71.2643),
    "Kansas City Stadium": (39.0489, -94.4839),
    "Dallas Stadium": (32.7473, -97.0841),
    "Houston Stadium": (29.6847, -95.4082),
    "Toronto Stadium": (43.6332, -79.4186),
    "Mexico City Stadium": (19.3030, -99.1506)
}

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lon / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c

jogos_restantes = [
    ("Costa do Marfim", "Equador", "Philadelphia Stadium", 28),
    ("Suécia", "Tunísia", "Monterrey Stadium", 30),
    ("Bélgica", "Egito", "Seattle Stadium", 18),
    ("Irã", "Nova Zelândia", "Los Angeles Stadium", 22),
    ("Espanha", "Cabo Verde", "Atlanta Stadium", 24),
    ("Uruguai", "Arábia Saudita", "Miami Stadium", 28),
    ("França", "Senegal", "New York New Jersey Stadium", 22),
    ("Iraque", "Noruega", "Boston Stadium", 20),
    ("Argentina", "Argélia", "Kansas City Stadium", 24),
    ("Áustria", "Jordânia", "Dallas Stadium", 26),
    ("Portugal", "RD Congo", "Houston Stadium", 28),
    ("Uzbequistão", "Colômbia", "Mexico City Stadium", 20),
    ("Inglaterra", "Croácia", "Dallas Stadium", 26),
    ("Gana", "Panamá", "Toronto Stadium", 18)
]

model = DixonColesModel(phi=0.0019, reg_lambda=5.0, shrink_lambda=0.1)
model.fit(JOGOS_CONCLUIDOS)

def calcular_pontos(xp, yp, xr, yr):
    if xp == xr and yp == yr:
        return 30
    if xp == yp and xr == yr:
        return 15
    if xp > yp and xr > yr:
        return 20 if xp == xr else 15
    if xp < yp and xr < yr:
        return 20 if yp == yr else 15
    return 0

# Calcula as novas previsões otimizadas para o bolão
novas_prevs = {}
for t_a, t_b, stadium, temp in jogos_restantes:
    lat_s, lon_s = ESTADIOS[stadium]
    lat_a, lon_a = QGS[t_a]
    lat_b, lon_b = QGS[t_b]
    dist_a = haversine(lat_a, lon_a, lat_s, lon_s)
    dist_b = haversine(lat_b, lon_b, lat_s, lon_s)
    
    rest_a = 5 if t_a == "Costa do Marfim" else 4
    rest_b = 4
    
    P, la, lb = model.predict_probabilities(
        t_a, t_b, 
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b
    )
    
    # Otimização por Valor Esperado (EV) do Bolão
    best_ev = -1
    best_placar = (0, 0)
    for xp in range(4):
        for yp in range(4):
            ev = 0.0
            for xr in range(6):
                for yr in range(6):
                    ev += P[xr, yr] * calcular_pontos(xp, yp, xr, yr)
            if ev > best_ev:
                best_ev = ev
                best_placar = (xp, yp)
                
    placar_str = f"{best_placar[0]} x {best_placar[1]}"
    
    res = model.get_top_scores(
        t_a, t_b, 
        distancia_a=dist_a, rest_a=rest_a, temp=temp,
        distancia_b=dist_b, rest_b=rest_b
    )
    
    novas_prevs[(t_a, t_b)] = {
        "placar": placar_str,
        "confianca": res["confianca_placar"],
        "justificativa": f"Palpite otimizado por Valor Esperado (EV: {best_ev:.2f} pts) para o bolão. Lambdas ajustados pelo Disparity Boost: {res['lambda_a']} x {res['lambda_b']}."
    }

path = "/Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada1.md"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_table = False

for line in lines:
    if "| Grupo | Confronto | Local / Estádio | Status |" in line:
        new_lines.append(line)
        in_table = True
        continue
    
    if in_table and line.startswith("|"):
        if line.strip() == "":
            in_table = False
            new_lines.append(line)
            continue
        
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 7:
            confronto = parts[2]
            status = parts[4]
            
            # Só atualiza se o status for "Preditivo"
            if "Preditivo" in status:
                jogo_chave = None
                for (t1, t2) in novas_prevs.keys():
                    if t1.lower() in confronto.lower() and t2.lower() in confronto.lower():
                        jogo_chave = (t1, t2)
                        break
                    if "coreia" in confronto.lower() and t1 == "Coreia do Sul":
                        if t2.lower() in confronto.lower() or "tch" in confronto.lower():
                            jogo_chave = (t1, t2)
                            break
                
                if jogo_chave:
                    data_prev = novas_prevs[jogo_chave]
                    parts[5] = f"**{data_prev['placar']}**"
                    parts[6] = f"**{data_prev['confianca']}**"
                    
            line = " | ".join(parts).strip() + "\n"
            if not line.startswith("|"):
                line = "| " + line
            if not line.endswith("|\n"):
                line = line.rstrip() + " |\n"
            new_lines.append(line)
            continue
            
    new_lines.append(line)

# Reescreve o arquivo
content = "".join(new_lines)

# Agora atualiza as justificativas e títulos no corpo do texto para as partidas preditivas
for (t1, t2), data_prev in novas_prevs.items():
    # Costa do Marfim já está concluído, não atualiza no corpo como preditivo
    if t1 == "Costa do Marfim":
        continue
        
    # Encontra o bloco do confronto
    pattern = rf"\*\s+\*\*{t1}\s+[^v]*vs\.\s+{t2}\*\*\s*.*?Nível de Confiança:.*?(?=\n\n|\n\*|\Z)"
    
    # Vamos fazer substituição via regex
    # Procura a justificativa original
    match_str = rf"\*\s+\*\*{t1}\s+([0-9]\s+x\s+[0-9])\s+{t2}\*\*"
    
    # Substitui o placar no título do detalhe: Ex: *   **Suécia 2 x 0 Tunísia** -> *   **Suécia 1 x 0 Tunísia**
    # Na verdade, os títulos no arquivo original estavam no formato "*   **Suécia 2 x 0 Tunísia**"
    # Vamos encontrar e substituir
    placar_novo = data_prev["placar"]
    
    # Procura e substitui o padrão exato do título
    # Ex: Suécia 2 x 0 Tunísia
    # Vamos achar o placar antigo
    reg = rf"\*\s+\*\*{t1}\s+([0-9]+\s+x\s+[0-9]+)\s+{t2}\*\*"
    m = re.search(reg, content)
    if m:
        placar_antigo = m.group(1)
        content = content.replace(f"**{t1} {placar_antigo} {t2}**", f"**{t1} {placar_novo} {t2}**")
        
        # Agora substitui a justificativa e o nível de confiança
        # Vamos reconstruir a seção para esse jogo
        old_section_reg = rf"\*\s+\*\*{t1}\s+{placar_novo}\s+{t2}\*\*\n\s+\*\s+\*\*Estádio:\*\*.*?\n\s+\*\s+\*\*Status:\*\* Preditivo.*?\n\s+\*\s+\*\*Justificativa:\*\*.*?\n\s+\*\s+\*\*Nível de Confiança:\*\*.*?(?=\n\n|\n\*|\Z)"
        
        # Busca a seção antiga
        # Como as justificativas originais diferem, vamos achar a seção dinamicamente
        # Uma forma mais segura de substituir é buscar a linha do Estádio e Status e substituir a justificativa
        # Vamos fazer isso de forma direta buscando a justificativa sob o título do confronto
        lines_content = content.split("\n")
        new_lines_content = []
        skip = 0
        for i, l in enumerate(lines_content):
            if skip > 0:
                skip -= 1
                continue
            new_lines_content.append(l)
            if f"**{t1} {placar_novo} {t2}**" in l:
                # Substitui as próximas 4 linhas (Estádio, Status, Justificativa, Confiança)
                # Vamos verificar se as próximas linhas são de fato os bullet points
                if i+1 < len(lines_content) and "Estádio" in lines_content[i+1]:
                    new_lines_content.append(lines_content[i+1]) # Mantém estádio
                    new_lines_content.append(lines_content[i+2]) # Mantém status
                    # Substitui Justificativa e Confiança
                    new_lines_content.append(f"    *   **Justificativa:** {data_prev['justificativa']}")
                    new_lines_content.append(f"    *   **Nível de Confiança:** {data_prev['confianca']}")
                    skip = 4
        content = "\n".join(new_lines_content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Previsões do relatório atualizadas com os novos palpites calibrados!")
