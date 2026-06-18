# 📊 Relatório Preditivo: 2ª Rodada da Copa do Mundo FIFA 2026

Este relatório apresenta uma análise estatística e tática detalhada para todas as 24 partidas da segunda rodada da fase de grupos da Copa do Mundo FIFA 2026. A metodologia preditiva foi calibrada utilizando as 24 partidas concluídas da 1ª rodada (com peso estendido através de regularização mais leve `reg_lambda=1.5` e sintonização do fator global de gols `mu=1.3922` para refletir a alta taxa de gols de 3.125 por partida observada na rodada inicial).

---

## 📅 Resumo dos Palpites (Tabela Rápida para o Bolão)

| Grupo | Confronto | Local / Estádio | Status | Palpite Preditivo | Confiança | EV Otimizado |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **A** | Tchéquia vs. África do Sul | Atlanta Stadium | Preditivo | **2 x 0** | **Média** | 10.46 pts |
| **A** | México vs. Coreia do Sul | Mexico City Stadium | Preditivo | **2 x 1** | **Média** | 9.58 pts |
| **B** | Suíça vs. Bósnia e Herzegovina | Los Angeles Stadium | Preditivo | **2 x 0** | **Média** | 8.22 pts |
| **B** | Canadá vs. Catar | Vancouver Stadium | Preditivo | **2 x 1** | **Média** | 9.16 pts |
| **C** | Escócia vs. Marrocos | Boston Stadium | Preditivo | **0 x 2** | **Alta** | 12.00 pts |
| **C** | Brasil vs. Haiti | Philadelphia Stadium | Preditivo | **4 x 0** | **Alta** | 18.64 pts |
| **D** | EUA vs. Austrália | Seattle Stadium | Preditivo | **1 x 2** | **Média** | 7.06 pts |
| **D** | Turquia vs. Paraguai | San Francisco Bay Stadium | Preditivo | **2 x 1** | **Média** | 8.30 pts |
| **E** | Alemanha vs. Costa do Marfim | Toronto Stadium | Preditivo | **2 x 1** | **Média** | 7.49 pts |
| **E** | Equador vs. Curaçao | Kansas City Stadium | Preditivo | **2 x 0** | **Média** | 14.22 pts |
| **F** | Holanda vs. Suécia | Houston Stadium | Preditivo | **1 x 2** | **Baixa** | 7.68 pts |
| **F** | Tunísia vs. Japão | Monterrey Stadium | Preditivo | **0 x 3** | **Baixa** | 14.05 pts |
| **G** | Bélgica vs. Irã | Los Angeles Stadium | Preditivo | **2 x 1** | **Média** | 10.28 pts |
| **G** | Nova Zelândia vs. Egito | Vancouver Stadium | Preditivo | **0 x 2** | **Média** | 12.16 pts |
| **H** | Espanha vs. Arábia Saudita | Atlanta Stadium | Preditivo | **3 x 0** | **Média** | 15.13 pts |
| **H** | Uruguai vs. Cabo Verde | Miami Stadium | Preditivo | **0 x 0** | **Alta** | 9.05 pts |
| **I** | França vs. Iraque | Philadelphia Stadium | Preditivo | **4 x 0** | **Alta** | 17.46 pts |
| **I** | Noruega vs. Senegal | New York New Jersey Stadium | Preditivo | **2 x 1** | **Baixa** | 8.47 pts |
| **J** | Argentina vs. Áustria | Dallas Stadium | Preditivo | **3 x 0** | **Média** | 14.87 pts |
| **J** | Jordânia vs. Argélia | San Francisco Bay Stadium | Preditivo | **1 x 2** | **Média** | 9.30 pts |
| **K** | Portugal vs. Uzbequistão | Houston Stadium | Preditivo | **3 x 0** | **Baixa** | 13.75 pts |
| **K** | Colômbia vs. RD Congo | Guadalajara Stadium | Preditivo | **2 x 0** | **Média** | 10.01 pts |
| **L** | Inglaterra vs. Gana | Boston Stadium | Preditivo | **3 x 0** | **Baixa** | 12.84 pts |
| **L** | Panamá vs. Croácia | Toronto Stadium | Preditivo | **0 x 2** | **Alta** | 14.94 pts |

---

## 🔍 Análise Detalhada Jogo a Jogo

### **Grupo A**

*   **Tchéquia 2 x 0 África do Sul**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (18/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.46 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Tchéquia (1.51) vs. África do Sul (0.71). Fatores Físicos: Tchéquia viajou 1193 km com 6 dias de descanso; África do Sul viajou 2077 km com 7 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Tchéquia: 54.4% | Empate: 29.7% | Vitória África do Sul: 15.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 0 (14.67%), 1 x 1 (13.48%), 0 x 0 (12.64%)
    *   **Nível de Confiança:** Média

*   **México 2 x 1 Coreia do Sul**
    *   **Estádio:** Mexico City Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (18/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.58 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: México (1.76) vs. Coreia do Sul (1.09). Fatores Físicos: México viajou 0 km com 7 dias de descanso; Coreia do Sul viajou 469 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória México: 51.0% | Empate: 27.1% | Vitória Coreia do Sul: 21.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.89%), 2 x 1 (9.87%), 2 x 0 (9.04%)
    *   **Nível de Confiança:** Média

### **Grupo B**

*   **Suíça 2 x 0 Bósnia e Herzegovina**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (18/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.22 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Suíça (1.35) vs. Bósnia e Herzegovina (0.99). Fatores Físicos: Suíça viajou 149 km com 5 dias de descanso; Bósnia e Herzegovina viajou 935 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Suíça: 43.1% | Empate: 31.4% | Vitória Bósnia e Herzegovina: 25.5%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (14.84%), 0 x 0 (11.54%), 1 x 0 (11.08%)
    *   **Nível de Confiança:** Média

*   **Canadá 2 x 1 Catar**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (18/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.16 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Canadá (1.67) vs. Catar (1.11). Fatores Físicos: Canadá viajou 1 km com 6 dias de descanso; Catar viajou 1675 km com 5 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Canadá: 48.5% | Empate: 28.0% | Vitória Catar: 23.6%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (13.34%), 2 x 1 (9.69%), 2 x 0 (8.76%)
    *   **Nível de Confiança:** Média

### **Grupo C**

*   **Escócia 0 x 2 Marrocos**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (19/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.00 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Escócia (0.58) vs. Marrocos (1.67). Fatores Físicos: Escócia viajou 1127 km com 5 dias de descanso; Marrocos viajou 314 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Escócia: 11.0% | Empate: 26.7% | Vitória Marrocos: 62.3%
    *   **Top 3 Placares mais Prováveis:** 0 x 1 (16.26%), 0 x 2 (14.86%), 0 x 0 (12.19%)
    *   **Nível de Confiança:** Alta

*   **Brasil 4 x 0 Haiti**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (19/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 18.64 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Brasil (4.97) vs. Haiti (0.12). Fatores Físicos: Brasil viajou 115 km com 6 dias de descanso; Haiti viajou 71 km com 5 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Brasil: 98.0% | Empate: 1.9% | Vitória Haiti: 0.1%
    *   **Top 3 Placares mais Prováveis:** 4 x 0 (25.11%), 5 x 0 (24.94%), 3 x 0 (20.22%)
    *   **Nível de Confiança:** Alta

### **Grupo D**

*   **EUA 1 x 2 Austrália**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (19/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.06 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: EUA (1.34) vs. Austrália (1.39). Fatores Físicos: EUA viajou 1592 km com 7 dias de descanso; Austrália viajou 1093 km com 5 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória EUA: 34.1% | Empate: 29.5% | Vitória Austrália: 36.4%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (14.05%), 1 x 2 (8.50%), 0 x 0 (8.39%)
    *   **Nível de Confiança:** Média

*   **Turquia 2 x 1 Paraguai**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (19/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.30 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Turquia (1.58) vs. Paraguai (1.23). Fatores Físicos: Turquia viajou 1019 km com 5 dias de descanso; Paraguai viajou 10 km com 7 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Turquia: 43.5% | Empate: 28.5% | Vitória Paraguai: 28.0%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (13.57%), 2 x 1 (9.31%), 0 x 0 (7.86%)
    *   **Nível de Confiança:** Média

### **Grupo E**

*   **Alemanha 2 x 1 Costa do Marfim**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (20/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.49 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Alemanha (1.48) vs. Costa do Marfim (1.33). Fatores Físicos: Alemanha viajou 841 km com 6 dias de descanso; Costa do Marfim viajou 539 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Alemanha: 38.9% | Empate: 28.8% | Vitória Costa do Marfim: 32.3%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (13.69%), 2 x 1 (8.83%), 1 x 2 (7.94%)
    *   **Nível de Confiança:** Média

*   **Equador 2 x 0 Curaçao**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (20/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 14.22 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Equador (2.70) vs. Curaçao (0.65). Fatores Físicos: Equador viajou 991 km com 6 dias de descanso; Curaçao viajou 1942 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Equador: 78.3% | Empate: 15.7% | Vitória Curaçao: 6.0%
    *   **Top 3 Placares mais Prováveis:** 2 x 0 (13.55%), 3 x 0 (12.18%), 1 x 0 (9.06%)
    *   **Nível de Confiança:** Média

### **Grupo F**

*   **Holanda 1 x 2 Suécia**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (20/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.68 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Holanda (1.88) vs. Suécia (2.08). Fatores Físicos: Holanda viajou 1050 km com 6 dias de descanso; Suécia viajou 368 km com 5 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Holanda: 34.5% | Empate: 23.7% | Vitória Suécia: 41.8%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (8.87%), 1 x 2 (8.02%), 2 x 2 (7.53%)
    *   **Nível de Confiança:** Baixa

*   **Tunísia 0 x 3 Japão**
    *   **Estádio:** Monterrey Stadium (Temperatura: 30°C)
    *   **Status:** Preditivo (20/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 14.05 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Tunísia (0.90) vs. Japão (3.23). Fatores Físicos: Tunísia viajou 7 km com 5 dias de descanso; Japão viajou 1732 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Tunísia: 6.9% | Empate: 14.0% | Vitória Japão: 79.1%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (10.13%), 0 x 2 (9.42%), 1 x 3 (9.12%)
    *   **Nível de Confiança:** Baixa

### **Grupo G**

*   **Bélgica 2 x 1 Irã**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (21/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.28 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Bélgica (2.04) vs. Irã (1.16). Fatores Físicos: Bélgica viajou 1539 km com 6 dias de descanso; Irã viajou 201 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Bélgica: 55.6% | Empate: 24.5% | Vitória Irã: 19.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.32%), 2 x 1 (10.04%), 2 x 0 (8.68%)
    *   **Nível de Confiança:** Média

*   **Nova Zelândia 0 x 2 Egito**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (21/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.16 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Nova Zelândia (0.82) vs. Egito (2.13). Fatores Físicos: Nova Zelândia viajou 1907 km com 6 dias de descanso; Egito viajou 456 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Nova Zelândia: 12.0% | Empate: 22.4% | Vitória Egito: 65.6%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (12.18%), 1 x 1 (10.73%), 0 x 1 (10.02%)
    *   **Nível de Confiança:** Média

### **Grupo H**

*   **Espanha 3 x 0 Arábia Saudita**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (21/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.13 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Espanha (2.91) vs. Arábia Saudita (0.52). Fatores Físicos: Espanha viajou 166 km com 6 dias de descanso; Arábia Saudita viajou 1315 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Espanha: 83.4% | Empate: 12.8% | Vitória Arábia Saudita: 3.7%
    *   **Top 3 Placares mais Prováveis:** 2 x 0 (14.77%), 3 x 0 (14.31%), 4 x 0 (10.40%)
    *   **Nível de Confiança:** Média

*   **Uruguai 0 x 0 Cabo Verde**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (21/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.05 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Uruguai (0.86) vs. Cabo Verde (0.76). Fatores Físicos: Uruguai viajou 915 km com 6 dias de descanso; Cabo Verde viajou 312 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Uruguai: 33.4% | Empate: 38.8% | Vitória Cabo Verde: 27.8%
    *   **Top 3 Placares mais Prováveis:** 0 x 0 (21.57%), 1 x 0 (15.02%), 1 x 1 (14.91%)
    *   **Nível de Confiança:** Alta

### **Grupo I**

*   **França 4 x 0 Iraque**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (22/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 17.46 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: França (6.15) vs. Iraque (0.64). Fatores Físicos: França viajou 439 km com 6 dias de descanso; Iraque viajou 514 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória França: 95.9% | Empate: 3.3% | Vitória Iraque: 0.9%
    *   **Top 3 Placares mais Prováveis:** 5 x 0 (19.47%), 4 x 0 (15.84%), 5 x 1 (12.52%)
    *   **Nível de Confiança:** Alta

*   **Noruega 2 x 1 Senegal**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (22/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.47 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Noruega (1.94) vs. Senegal (1.54). Fatores Físicos: Noruega viajou 725 km com 6 dias de descanso; Senegal viajou 48 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Noruega: 45.4% | Empate: 25.2% | Vitória Senegal: 29.5%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (10.79%), 2 x 1 (9.11%), 1 x 2 (7.22%)
    *   **Nível de Confiança:** Baixa

### **Grupo J**

*   **Argentina 3 x 0 Áustria**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (22/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 14.87 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Argentina (3.05) vs. Áustria (0.64). Fatores Físicos: Argentina viajou 741 km com 6 dias de descanso; Áustria viajou 2099 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Argentina: 82.5% | Empate: 12.9% | Vitória Áustria: 4.5%
    *   **Top 3 Placares mais Prováveis:** 3 x 0 (13.01%), 2 x 0 (12.82%), 4 x 0 (9.90%)
    *   **Nível de Confiança:** Média

*   **Jordânia 1 x 2 Argélia**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (22/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.30 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Jordânia (1.09) vs. Argélia (1.69). Fatores Físicos: Jordânia viajou 904 km com 6 dias de descanso; Argélia viajou 2335 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Jordânia: 22.9% | Empate: 27.8% | Vitória Argélia: 49.3%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (13.26%), 1 x 2 (9.74%), 0 x 2 (8.93%)
    *   **Nível de Confiança:** Média

### **Grupo K**

*   **Portugal 3 x 0 Uzbequistão**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (23/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.75 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Portugal (3.03) vs. Uzbequistão (0.89). Fatores Físicos: Portugal viajou 1539 km com 6 dias de descanso; Uzbequistão viajou 1135 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Portugal: 77.2% | Empate: 15.2% | Vitória Uzbequistão: 7.6%
    *   **Top 3 Placares mais Prováveis:** 3 x 0 (10.11%), 2 x 0 (10.03%), 3 x 1 (8.96%)
    *   **Nível de Confiança:** Baixa

*   **Colômbia 2 x 0 RD Congo**
    *   **Estádio:** Guadalajara Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (23/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.01 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Colômbia (1.76) vs. RD Congo (0.99). Fatores Físicos: Colômbia viajou 7 km com 6 dias de descanso; RD Congo viajou 1296 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Colômbia: 53.4% | Empate: 27.1% | Vitória RD Congo: 19.5%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.95%), 2 x 0 (10.02%), 2 x 1 (9.90%)
    *   **Nível de Confiança:** Média

### **Grupo L**

*   **Inglaterra 3 x 0 Gana**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (23/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.84 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Inglaterra (2.82) vs. Gana (0.99). Fatores Físicos: Inglaterra viajou 1990 km com 6 dias de descanso; Gana viajou 30 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Inglaterra: 72.4% | Empate: 17.4% | Vitória Gana: 10.2%
    *   **Top 3 Placares mais Prováveis:** 2 x 0 (9.43%), 2 x 1 (9.36%), 3 x 0 (8.85%)
    *   **Nível de Confiança:** Baixa

*   **Panamá 0 x 2 Croácia**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (23/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 14.94 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Panamá (0.49) vs. Croácia (2.59). Fatores Físicos: Panamá viajou 4 km com 6 dias de descanso; Croácia viajou 572 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Panamá: 4.3% | Empate: 15.0% | Vitória Croácia: 80.7%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (16.24%), 0 x 3 (14.02%), 0 x 1 (11.62%)
    *   **Nível de Confiança:** Alta

