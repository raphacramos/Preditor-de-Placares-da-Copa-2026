import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo_avancado_copa import DixonColesModel, JOGOS_CONCLUIDOS

model = DixonColesModel(phi=0.0019, reg_lambda=1.0, shrink_lambda=0.5)
model.fit(JOGOS_CONCLUIDOS)

# Imprime parâmetros de algumas seleções importantes
times = ["Alemanha", "Curaçao", "Espanha", "Cabo Verde", "Brasil", "Argentina", "França"]
print("| Seleção | Alpha (Ataque) | Beta (Defesa) | Prior Alpha | Prior Beta |")
print("| :--- | :---: | :---: | :---: | :---: |")
for t in times:
    idx = model.team_to_idx[t]
    print(f"| {t} | {model.alphas[idx]:.3f} | {model.betas[idx]:.3f} | {model.pi_system.home_ratings[t]:.3f} | {model.pi_system.away_ratings[t]:.3f} |")
