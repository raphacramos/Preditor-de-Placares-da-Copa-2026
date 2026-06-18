# 🏆 Preditor de Placares da Copa do Mundo FIFA 2026

Repositório contendo o pipeline estatístico de elite para previsão de resultados e otimização de palpites para bolões da Copa do Mundo FIFA 2026. O modelo combina conceitos clássicos de desporto-ciência (Dixon-Coles, Pi-Ratings) com ajustes bayesianos hierárquicos, fadiga física logística e um coeficiente dinâmico de disparidade tática.

---

## 📐 Metodologia e Modelagem Estatística

O motor de previsões baseia-se em quatro pilares fundamentais sintonizados com dados reais do torneio:

1.  **Dixon-Coles + Pi-Ratings Dinâmico:** Ajuste dinâmico de força de ataque ($\alpha$) e defesa ($\beta$) baseado no saldo de gols real com retornos decrescentes (logarítmicos) para evitar o ruído de goleadas atípicas.
2.  **Bayesian Shrinkage (Encolhimento Hierárquico):** Regularização L2 sintonizada (`reg_lambda=1.5`) para forçar o encolhimento de seleções com poucos dados em direção à média global, prevenindo *overfitting* após a 1ª rodada.
3.  **Índice de Fadiga Logística (Fator $\delta$):** Ajuste exponencial na expectativa de gols com base em:
    *   Distância percorrida (km via fórmula Haversine entre o QG oficial e o estádio).
    *   Dias de descanso acumulados entre partidas.
    *   Temperatura média do estádio no dia do jogo.
4.  **Coeficiente de Disparidade (Disparity Boost):** Correção não-linear de expectativa de gols em confrontos de abismo técnico (razão de forças $> 1.8$), limitado a um teto estável de `1.5` para capturar a probabilidade real de goleadas (ex: Brasil vs. Haiti, França vs. Iraque).
5.  **Otimização por Valor Esperado (EV):** Otimização de palpites baseada nas regras de pontuação personalizadas do bolão:
    *   **30 pontos:** Placar exato cravado.
    *   **20 pontos:** Acerto do vencedor + gols exatos do vencedor.
    *   **15 pontos:** Empate correto ou acerto seco do vencedor.

---

## 📁 Estrutura do Repositório

```bash
├── README.md                          # Este arquivo
├── src/                               # Códigos fonte em Python
│   ├── modelo_avancado_copa.py         # Motor de modelagem Dixon-Coles e ajuste de priors
│   ├── aplicar_novos_palpites_rodada2.py# Pipeline de predição e geração da 2ª Rodada
│   ├── recalibrador_placares.py        # Wrapper para ajustes táticos rápidos e odds
│   ├── simulador_campeao_copa.py       # Simulador Monte Carlo do torneio (10.000 simulações)
│   ├── comparar_odds.py                # Script de análise de EV vs. Odds Reais de Mercado
│   ├── calcular_distancias.py          # Cálculo geográfico Haversine para fadiga
│   └── ... (scripts de teste e calibração de rodada 1)
└── relatorios/                         # Relatórios executivos de palpites gerados
    ├── palpites_copa_2026_rodada1.md   # Relatório e fechamento da 1ª Rodada
    ├── palpites_copa_2026_rodada2.md   # Relatório com palpites otimizados para a 2ª Rodada
    └── relatorio_metodologia_preditiva.pdf # PDF de metodologia técnica distribuída
```

---

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de possuir Python 3 e as bibliotecas científicas básicas instaladas:
```bash
pip install numpy scipy pandas
```

### 1. Executar Palpites da 2ª Rodada
Para rodar a calibração com dados da 1ª rodada e gerar o relatório otimizado por Valor Esperado (EV) da 2ª rodada:
```bash
python src/aplicar_novos_palpites_rodada2.py
```

### 2. Simular o Campeão da Copa do Mundo (Monte Carlo)
Rode a simulação de 10.000 torneios completos (fase de grupos e mata-mata com desempates) para estimar as probabilidades atualizadas de título das 48 seleções:
```bash
python src/simulador_campeao_copa.py
```

### 3. Cruzamento e Análise de Valor Esperado (EV) contra as Odds de Mercado
Compare as odds justas do modelo com as cotas reais oferecidas pelas casas de apostas para encontrar apostas com EV positivo:
```bash
python src/comparar_odds.py
```
