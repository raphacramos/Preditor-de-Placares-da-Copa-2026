# 📊 Relatório Preditivo: 2ª Rodada da Copa do Mundo FIFA 2026

Este relatório apresenta uma análise estatística e tática detalhada para todas as 24 partidas da segunda rodada da fase de grupos da Copa do Mundo FIFA 2026. A metodologia preditiva foi calibrada utilizando as 24 partidas concluídas da 1ª rodada (com peso estendido através de regularização mais leve `reg_lambda=1.5` e sintonização do fator global de gols `mu=1.3922`). Adicionalmente, este relatório incorpora as **odds reais de mercado das casas de apostas** através de uma fusão bayesiana (peso de 60% para o modelo estatístico e 40% para as cotações implícitas do mercado), maximizando o Valor Esperado (EV) dos palpites para o bolão.

---

## 📅 Resumo dos Palpites (Tabela Rápida para o Bolão)

| Grupo | Confronto | Local / Estádio | Status | Palpite Preditivo | Confiança | EV Otimizado |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **A** | Tchéquia vs. África do Sul | Atlanta Stadium | Preditivo | **2 x 0** | **Média** | 9.96 pts |
| **A** | México vs. Coreia do Sul | Mexico City Stadium | Preditivo | **2 x 1** | **Média** | 9.24 pts |
| **B** | Suíça vs. Bósnia e Herzegovina | Los Angeles Stadium | Preditivo | **2 x 0** | **Média** | 8.99 pts |
| **B** | Canadá vs. Catar | Vancouver Stadium | Preditivo | **2 x 1** | **Média** | 11.14 pts |
| **C** | Escócia vs. Marrocos | Boston Stadium | Preditivo | **0 x 2** | **Média** | 11.32 pts |
| **C** | Brasil vs. Haiti | Philadelphia Stadium | Preditivo | **4 x 0** | **Alta** | 17.80 pts |
| **D** | EUA vs. Austrália | Seattle Stadium | Preditivo | **2 x 1** | **Média** | 8.33 pts |
| **D** | Turquia vs. Paraguai | San Francisco Bay Stadium | Preditivo | **2 x 1** | **Média** | 8.35 pts |
| **E** | Alemanha vs. Costa do Marfim | Toronto Stadium | Preditivo | **2 x 1** | **Média** | 9.21 pts |
| **E** | Equador vs. Curaçao | Kansas City Stadium | Preditivo | **2 x 0** | **Média** | 14.64 pts |
| **F** | Holanda vs. Suécia | Houston Stadium | Preditivo | **2 x 1** | **Baixa** | 8.03 pts |
| **F** | Tunísia vs. Japão | Monterrey Stadium | Preditivo | **0 x 3** | **Baixa** | 12.81 pts |
| **G** | Bélgica vs. Irã | Los Angeles Stadium | Preditivo | **2 x 1** | **Baixa** | 10.93 pts |
| **G** | Nova Zelândia vs. Egito | Vancouver Stadium | Preditivo | **0 x 2** | **Média** | 11.09 pts |
| **H** | Espanha vs. Arábia Saudita | Atlanta Stadium | Preditivo | **3 x 0** | **Média** | 15.36 pts |
| **H** | Uruguai vs. Cabo Verde | Miami Stadium | Preditivo | **1 x 0** | **Alta** | 9.95 pts |
| **I** | França vs. Iraque | Philadelphia Stadium | Preditivo | **4 x 0** | **Alta** | 16.73 pts |
| **I** | Noruega vs. Senegal | New York New Jersey Stadium | Preditivo | **2 x 1** | **Média** | 8.87 pts |
| **J** | Argentina vs. Áustria | Dallas Stadium | Preditivo | **3 x 0** | **Média** | 13.93 pts |
| **J** | Jordânia vs. Argélia | San Francisco Bay Stadium | Preditivo | **1 x 2** | **Média** | 9.66 pts |
| **K** | Portugal vs. Uzbequistão | Houston Stadium | Preditivo | **3 x 0** | **Baixa** | 13.63 pts |
| **K** | Colômbia vs. RD Congo | Guadalajara Stadium | Preditivo | **2 x 0** | **Média** | 10.83 pts |
| **L** | Inglaterra vs. Gana | Boston Stadium | Preditivo | **3 x 0** | **Baixa** | 13.07 pts |
| **L** | Panamá vs. Croácia | Toronto Stadium | Preditivo | **0 x 2** | **Média** | 13.25 pts |

---

## 🔍 Análise Detalhada Jogo a Jogo

### **Grupo A**

*   **Tchéquia 2 x 0 África do Sul**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (18/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.96 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Tchéquia (1.51) vs. África do Sul (0.71). Fatores Físicos: Tchéquia viajou 1193 km com 6 dias de descanso; África do Sul viajou 2077 km com 7 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Tchéquia: 51.8% | Empate: 29.8% | Vitória África do Sul: 18.4%
    *   **Top 3 Placares mais Prováveis:** 1 x 0 (13.97%), 1 x 1 (13.53%), 0 x 0 (12.69%)
    *   **Nível de Confiança:** Média

*   **México 2 x 1 Coreia do Sul**
    *   **Estádio:** Mexico City Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (18/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.24 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: México (1.76) vs. Coreia do Sul (1.09). Fatores Físicos: México viajou 0 km com 7 dias de descanso; Coreia do Sul viajou 469 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória México: 49.2% | Empate: 27.9% | Vitória Coreia do Sul: 23.0%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (13.26%), 2 x 1 (9.52%), 2 x 0 (8.72%)
    *   **Nível de Confiança:** Média

### **Grupo B**

*   **Suíça 2 x 0 Bósnia e Herzegovina**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (18/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.99 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Suíça (1.35) vs. Bósnia e Herzegovina (0.99). Fatores Físicos: Suíça viajou 149 km com 5 dias de descanso; Bósnia e Herzegovina viajou 935 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Suíça: 47.1% | Empate: 30.2% | Vitória Bósnia e Herzegovina: 22.7%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (14.25%), 1 x 0 (12.12%), 0 x 0 (11.09%)
    *   **Nível de Confiança:** Média

*   **Canadá 2 x 1 Catar**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (18/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.14 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Canadá (1.67) vs. Catar (1.11). Fatores Físicos: Canadá viajou 1 km com 6 dias de descanso; Catar viajou 1675 km com 5 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Canadá: 58.9% | Empate: 23.5% | Vitória Catar: 17.6%
    *   **Top 3 Placares mais Prováveis:** 2 x 1 (11.77%), 1 x 1 (11.20%), 2 x 0 (10.65%)
    *   **Nível de Confiança:** Média

### **Grupo C**

*   **Escócia 0 x 2 Marrocos**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (19/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.32 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Escócia (0.58) vs. Marrocos (1.67). Fatores Físicos: Escócia viajou 1127 km com 5 dias de descanso; Marrocos viajou 314 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Escócia: 14.0% | Empate: 27.2% | Vitória Marrocos: 58.8%
    *   **Top 3 Placares mais Prováveis:** 0 x 1 (15.33%), 0 x 2 (14.02%), 0 x 0 (12.41%)
    *   **Nível de Confiança:** Média

*   **Brasil 4 x 0 Haiti**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (19/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 17.80 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Brasil (4.97) vs. Haiti (0.12). Fatores Físicos: Brasil viajou 115 km com 6 dias de descanso; Haiti viajou 71 km com 5 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Brasil: 93.6% | Empate: 4.6% | Vitória Haiti: 1.8%
    *   **Top 3 Placares mais Prováveis:** 4 x 0 (23.99%), 5 x 0 (23.83%), 3 x 0 (19.32%)
    *   **Nível de Confiança:** Alta

### **Grupo D**

*   **EUA 2 x 1 Austrália**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (19/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.33 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: EUA (1.34) vs. Austrália (1.39). Fatores Físicos: EUA viajou 1592 km com 7 dias de descanso; Austrália viajou 1093 km com 5 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória EUA: 42.8% | Empate: 27.8% | Vitória Austrália: 29.4%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (13.26%), 2 x 1 (10.27%), 1 x 0 (8.72%)
    *   **Nível de Confiança:** Média

*   **Turquia 2 x 1 Paraguai**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (19/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.35 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Turquia (1.58) vs. Paraguai (1.23). Fatores Físicos: Turquia viajou 1019 km com 5 dias de descanso; Paraguai viajou 10 km com 7 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Turquia: 43.7% | Empate: 28.8% | Vitória Paraguai: 27.5%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (13.70%), 2 x 1 (9.36%), 0 x 0 (7.94%)
    *   **Nível de Confiança:** Média

### **Grupo E**

*   **Alemanha 2 x 1 Costa do Marfim**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (20/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.21 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Alemanha (1.48) vs. Costa do Marfim (1.33). Fatores Físicos: Alemanha viajou 841 km com 6 dias de descanso; Costa do Marfim viajou 539 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Alemanha: 47.8% | Empate: 26.2% | Vitória Costa do Marfim: 25.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.45%), 2 x 1 (10.86%), 1 x 0 (8.77%)
    *   **Nível de Confiança:** Média

*   **Equador 2 x 0 Curaçao**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (20/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 14.64 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Equador (2.70) vs. Curaçao (0.65). Fatores Físicos: Equador viajou 991 km com 6 dias de descanso; Curaçao viajou 1942 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Equador: 80.6% | Empate: 13.9% | Vitória Curaçao: 5.5%
    *   **Top 3 Placares mais Prováveis:** 2 x 0 (13.94%), 3 x 0 (12.54%), 1 x 0 (9.33%)
    *   **Nível de Confiança:** Média

### **Grupo F**

*   **Holanda 2 x 1 Suécia**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (20/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.03 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Holanda (1.88) vs. Suécia (2.08). Fatores Físicos: Holanda viajou 1050 km com 6 dias de descanso; Suécia viajou 368 km com 5 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Holanda: 43.0% | Empate: 24.1% | Vitória Suécia: 32.9%
    *   **Top 3 Placares mais Prováveis:** 2 x 1 (9.03%), 1 x 1 (9.01%), 2 x 2 (7.65%)
    *   **Nível de Confiança:** Baixa

*   **Tunísia 0 x 3 Japão**
    *   **Estádio:** Monterrey Stadium (Temperatura: 30°C)
    *   **Status:** Preditivo (20/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.81 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Tunísia (0.90) vs. Japão (3.23). Fatores Físicos: Tunísia viajou 7 km com 5 dias de descanso; Japão viajou 1732 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Tunísia: 9.9% | Empate: 17.9% | Vitória Japão: 72.1%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (9.24%), 0 x 2 (8.59%), 1 x 3 (8.32%)
    *   **Nível de Confiança:** Baixa

### **Grupo G**

*   **Bélgica 2 x 1 Irã**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (21/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.93 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Bélgica (2.04) vs. Irã (1.16). Fatores Físicos: Bélgica viajou 1539 km com 6 dias de descanso; Irã viajou 201 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Bélgica: 59.1% | Empate: 23.6% | Vitória Irã: 17.3%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (10.90%), 2 x 1 (10.68%), 2 x 0 (9.24%)
    *   **Nível de Confiança:** Baixa

*   **Nova Zelândia 0 x 2 Egito**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (21/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.09 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Nova Zelândia (0.82) vs. Egito (2.13). Fatores Físicos: Nova Zelândia viajou 1907 km com 6 dias de descanso; Egito viajou 456 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Nova Zelândia: 15.6% | Empate: 24.6% | Vitória Egito: 59.8%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.76%), 0 x 2 (11.11%), 0 x 1 (9.14%)
    *   **Nível de Confiança:** Média

### **Grupo H**

*   **Espanha 3 x 0 Arábia Saudita**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (21/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.36 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Espanha (2.91) vs. Arábia Saudita (0.52). Fatores Físicos: Espanha viajou 166 km com 6 dias de descanso; Arábia Saudita viajou 1315 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Espanha: 84.7% | Empate: 11.7% | Vitória Arábia Saudita: 3.6%
    *   **Top 3 Placares mais Prováveis:** 2 x 0 (14.99%), 3 x 0 (14.53%), 4 x 0 (10.56%)
    *   **Nível de Confiança:** Média

*   **Uruguai 1 x 0 Cabo Verde**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (21/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.95 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Uruguai (0.86) vs. Cabo Verde (0.76). Fatores Físicos: Uruguai viajou 915 km com 6 dias de descanso; Cabo Verde viajou 312 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Uruguai: 45.8% | Empate: 32.6% | Vitória Cabo Verde: 21.6%
    *   **Top 3 Placares mais Prováveis:** 1 x 0 (20.56%), 0 x 0 (18.13%), 1 x 1 (12.53%)
    *   **Nível de Confiança:** Alta

### **Grupo I**

*   **França 4 x 0 Iraque**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (22/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 16.73 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: França (6.15) vs. Iraque (0.64). Fatores Físicos: França viajou 439 km com 6 dias de descanso; Iraque viajou 514 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória França: 91.8% | Empate: 6.2% | Vitória Iraque: 2.0%
    *   **Top 3 Placares mais Prováveis:** 5 x 0 (18.65%), 4 x 0 (15.17%), 5 x 1 (12.00%)
    *   **Nível de Confiança:** Alta

*   **Noruega 2 x 1 Senegal**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (22/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.87 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Noruega (1.94) vs. Senegal (1.54). Fatores Físicos: Noruega viajou 725 km com 6 dias de descanso; Senegal viajou 48 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Noruega: 47.5% | Empate: 25.8% | Vitória Senegal: 26.6%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.08%), 2 x 1 (9.55%), 2 x 2 (7.20%)
    *   **Nível de Confiança:** Média

### **Grupo J**

*   **Argentina 3 x 0 Áustria**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (22/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.93 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Argentina (3.05) vs. Áustria (0.64). Fatores Físicos: Argentina viajou 741 km com 6 dias de descanso; Áustria viajou 2099 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Argentina: 77.3% | Empate: 15.6% | Vitória Áustria: 7.1%
    *   **Top 3 Placares mais Prováveis:** 3 x 0 (12.19%), 2 x 0 (12.00%), 4 x 0 (9.28%)
    *   **Nível de Confiança:** Média

*   **Jordânia 1 x 2 Argélia**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (22/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.66 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Jordânia (1.09) vs. Argélia (1.69). Fatores Físicos: Jordânia viajou 904 km com 6 dias de descanso; Argélia viajou 2335 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Jordânia: 21.6% | Empate: 27.2% | Vitória Argélia: 51.2%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.97%), 1 x 2 (10.11%), 0 x 2 (9.27%)
    *   **Nível de Confiança:** Média

### **Grupo K**

*   **Portugal 3 x 0 Uzbequistão**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (23/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.63 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Portugal (3.03) vs. Uzbequistão (0.89). Fatores Físicos: Portugal viajou 1539 km com 6 dias de descanso; Uzbequistão viajou 1135 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Portugal: 76.5% | Empate: 15.6% | Vitória Uzbequistão: 7.9%
    *   **Top 3 Placares mais Prováveis:** 3 x 0 (10.02%), 2 x 0 (9.94%), 3 x 1 (8.88%)
    *   **Nível de Confiança:** Baixa

*   **Colômbia 2 x 0 RD Congo**
    *   **Estádio:** Guadalajara Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (23/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.83 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Colômbia (1.76) vs. RD Congo (0.99). Fatores Físicos: Colômbia viajou 7 km com 6 dias de descanso; RD Congo viajou 1296 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Colômbia: 57.8% | Empate: 25.1% | Vitória RD Congo: 17.1%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.03%), 2 x 0 (10.85%), 2 x 1 (10.71%)
    *   **Nível de Confiança:** Média

### **Grupo L**

*   **Inglaterra 3 x 0 Gana**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (23/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.07 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Inglaterra (2.82) vs. Gana (0.99). Fatores Físicos: Inglaterra viajou 1990 km com 6 dias de descanso; Gana viajou 30 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Inglaterra: 73.6% | Empate: 16.9% | Vitória Gana: 9.4%
    *   **Top 3 Placares mais Prováveis:** 2 x 0 (9.59%), 2 x 1 (9.52%), 3 x 0 (9.00%)
    *   **Nível de Confiança:** Baixa

*   **Panamá 0 x 2 Croácia**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (23/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.25 pts) para as regras do bolão. Médias de gols projetadas pelo Dixon-Coles sintonizado: Panamá (0.49) vs. Croácia (2.59). Fatores Físicos: Panamá viajou 4 km com 6 dias de descanso; Croácia viajou 572 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Panamá: 9.4% | Empate: 18.9% | Vitória Croácia: 71.6%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (14.41%), 0 x 3 (12.44%), 0 x 1 (10.31%)
    *   **Nível de Confiança:** Média

