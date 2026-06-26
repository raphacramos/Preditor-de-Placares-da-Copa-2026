# 📊 Relatório Preditivo: 3ª Rodada da Copa do Mundo FIFA 2026

Este relatório apresenta a análise estatística e tática detalhada para todas as 24 partidas da terceira e última rodada da fase de grupos. A metodologia preditiva foi adaptada especificamente para contornar as anomalias comuns de encerramento de grupo (poupa de titulares de equipes já qualificadas, motivação assimétrica e retrancas desesperadas).

## 🛠️ Ajustes de Calibração Utilizados:
1. **Mesclagem Dinâmica com Odds de Mercado (`w_modelo`):** Para jogos de times qualificados ou eliminados, as odds reais detêm 60% do peso, já que o mercado reage instantaneamente a informações de escalação alternativa. Para jogos de confronto direto, o modelo estatístico mantém a primazia (55% do peso).
2. **Underdog Resiliency Buffer:** Incremento de 5% na solidez defensiva (redução do parâmetro `beta`) para seleções com perfil de forte bloco defensivo baixo (Cabo Verde, RD Congo, Irã, Curaçao, África do Sul).
3. **Curinga de Disparidade Controlado:** O limitador do *Disparity Boost* foi reduzido de `1.50` para `1.30` para evitar a projeção de goleadas irreais em jogos sem interesse ofensivo de seleções qualificadas.
4. **Banco de Dados Completo:** Calibração executada sobre o histórico completo de **48 jogos reais** das rodadas 1 e 2.

---

## 📅 Resumo dos Palpites (Tabela Rápida para o Bolão)

| Grupo | Confronto | Local / Estádio | Status | Palpite Preditivo | Confiança | EV Otimizado | Contexto de Peso |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **B** | Suíça vs. Canadá | Vancouver Stadium | Preditivo | **2 x 1** | **Média** | 7.35 pts | Duelo Direto Decisivo (w: 0.55) |
| **B** | Bósnia e Herzegovina vs. Catar | Seattle Stadium | Preditivo | **2 x 0** | **Baixa** | 12.07 pts | Duelo Direto Decisivo (w: 0.55) |
| **C** | Escócia vs. Brasil | Miami Stadium | Preditivo | **0 x 2** | **Alta** | 15.04 pts | Duelo Direto Decisivo (w: 0.55) |
| **C** | Marrocos vs. Haiti | Atlanta Stadium | Preditivo | **4 x 0** | **Média** | 14.89 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **A** | Tchéquia vs. México | Mexico City Stadium | Preditivo | **0 x 3** | **Média** | 12.51 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **A** | África do Sul vs. Coreia do Sul | Monterrey Stadium | Preditivo | **0 x 1** | **Alta** | 9.47 pts | Duelo Direto Decisivo (w: 0.55) |
| **E** | Equador vs. Alemanha | New York New Jersey Stadium | Preditivo | **0 x 2** | **Média** | 9.81 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **E** | Curaçao vs. Costa do Marfim | Philadelphia Stadium | Preditivo | **0 x 3** | **Alta** | 15.89 pts | Duelo Direto Decisivo (w: 0.55) |
| **F** | Japão vs. Suécia | Dallas Stadium | Preditivo | **3 x 1** | **Baixa** | 10.43 pts | Duelo Direto Decisivo (w: 0.55) |
| **F** | Tunísia vs. Holanda | Kansas City Stadium | Preditivo | **0 x 4** | **Alta** | 16.52 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **D** | Turquia vs. EUA | Los Angeles Stadium | Preditivo | **0 x 4** | **Média** | 12.48 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **D** | Paraguai vs. Austrália | San Francisco Bay Stadium | Preditivo | **1 x 1** | **Alta** | 8.05 pts | Duelo Direto Decisivo (w: 0.55) |
| **I** | Noruega vs. França | Boston Stadium | Preditivo | **0 x 3** | **Média** | 12.44 pts | Ambas Classificadas (Poupa de Elenco) (w: 0.45) |
| **I** | Senegal vs. Iraque | Toronto Stadium | Preditivo | **3 x 0** | **Baixa** | 11.15 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **H** | Cabo Verde vs. Arábia Saudita | Houston Stadium | Preditivo | **2 x 1** | **Média** | 10.21 pts | Duelo Direto Decisivo (w: 0.55) |
| **H** | Uruguai vs. Espanha | Guadalajara Stadium | Preditivo | **1 x 2** | **Média** | 12.75 pts | Duelo Direto Decisivo (w: 0.55) |
| **G** | Egito vs. Irã | Seattle Stadium | Preditivo | **2 x 1** | **Média** | 9.09 pts | Duelo Direto Decisivo (w: 0.55) |
| **G** | Nova Zelândia vs. Bélgica | Vancouver Stadium | Preditivo | **0 x 3** | **Baixa** | 13.16 pts | Duelo Direto Decisivo (w: 0.55) |
| **L** | Panamá vs. Inglaterra | New York New Jersey Stadium | Preditivo | **0 x 3** | **Alta** | 15.52 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **L** | Croácia vs. Gana | Philadelphia Stadium | Preditivo | **1 x 0** | **Alta** | 7.43 pts | Duelo Direto Decisivo (w: 0.55) |
| **K** | Colômbia vs. Portugal | Miami Stadium | Preditivo | **1 x 2** | **Média** | 9.41 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **K** | RD Congo vs. Uzbequistão | Atlanta Stadium | Preditivo | **2 x 0** | **Média** | 9.33 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **J** | Argélia vs. Áustria | Kansas City Stadium | Preditivo | **1 x 2** | **Média** | 8.03 pts | Duelo Direto Decisivo (w: 0.55) |
| **J** | Jordânia vs. Argentina | Dallas Stadium | Preditivo | **0 x 4** | **Alta** | 15.95 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |

---

## 🔍 Análise Detalhada Jogo a Jogo

### **Grupo B**

*   **Suíça 2 x 1 Canadá**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.35 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Suíça (1.55) vs. Canadá (1.63). Fatores Físicos: Suíça viajou 1873 km com 6 dias de descanso; Canadá viajou 1 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Suíça: 38.1% | Empate: 27.7% | Vitória Canadá: 34.2%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.56%), 2 x 1 (9.03%), 1 x 2 (7.74%)
    *   **Nível de Confiança:** Média

*   **Bósnia e Herzegovina 2 x 0 Catar**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.07 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Bósnia e Herzegovina (2.37) vs. Catar (0.94). Fatores Físicos: Bósnia e Herzegovina viajou 1137 km com 6 dias de descanso; Catar viajou 1481 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Bósnia e Herzegovina: 66.6% | Empate: 20.7% | Vitória Catar: 12.8%
    *   **Top 3 Placares mais Prováveis:** 2 x 0 (10.58%), 2 x 1 (9.93%), 1 x 1 (9.64%)
    *   **Nível de Confiança:** Baixa

### **Grupo C**

*   **Escócia 0 x 2 Brasil**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.04 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Escócia (0.26) vs. Brasil (2.59). Fatores Físicos: Escócia viajou 1032 km com 5 dias de descanso; Brasil viajou 1733 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Escócia: 5.3% | Empate: 15.0% | Vitória Brasil: 79.7%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (18.93%), 0 x 3 (16.36%), 0 x 1 (14.04%)
    *   **Nível de Confiança:** Alta

*   **Marrocos 4 x 0 Haiti**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 14.89 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Marrocos (4.06) vs. Haiti (0.62). Fatores Físicos: Marrocos viajou 1164 km com 5 dias de descanso; Haiti viajou 1082 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Marrocos: 83.2% | Empate: 12.5% | Vitória Haiti: 4.3%
    *   **Top 3 Placares mais Prováveis:** 4 x 0 (12.48%), 3 x 0 (12.29%), 5 x 0 (10.14%)
    *   **Nível de Confiança:** Média

### **Grupo A**

*   **Tchéquia 0 x 3 México**
    *   **Estádio:** Mexico City Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.51 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Tchéquia (0.12) vs. México (3.40). Fatores Físicos: Tchéquia viajou 1488 km com 6 dias de descanso; México viajou 0 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Tchéquia: 15.1% | Empate: 18.0% | Vitória México: 66.9%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (15.80%), 0 x 2 (13.93%), 0 x 4 (13.44%)
    *   **Nível de Confiança:** Média

*   **África do Sul 0 x 1 Coreia do Sul**
    *   **Estádio:** Monterrey Stadium (Temperatura: 30°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.47 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: África do Sul (0.83) vs. Coreia do Sul (0.94). Fatores Físicos: África do Sul viajou 638 km com 6 dias de descanso; Coreia do Sul viajou 641 km com 6 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória África do Sul: 23.4% | Empate: 31.8% | Vitória Coreia do Sul: 44.8%
    *   **Top 3 Placares mais Prováveis:** 0 x 1 (18.34%), 0 x 0 (16.36%), 1 x 1 (13.04%)
    *   **Nível de Confiança:** Alta

### **Grupo E**

*   **Equador 0 x 2 Alemanha**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.81 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Equador (0.93) vs. Alemanha (1.63). Fatores Físicos: Equador viajou 759 km com 5 dias de descanso; Alemanha viajou 750 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Equador: 22.5% | Empate: 25.6% | Vitória Alemanha: 51.8%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.24%), 0 x 1 (10.98%), 0 x 2 (10.37%)
    *   **Nível de Confiança:** Média

*   **Curaçao 0 x 3 Costa do Marfim**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.89 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Curaçao (0.31) vs. Costa do Marfim (2.96). Fatores Físicos: Curaçao viajou 1573 km com 5 dias de descanso; Costa do Marfim viajou 17 km com 5 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória Curaçao: 3.1% | Empate: 10.6% | Vitória Costa do Marfim: 86.3%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (17.75%), 0 x 3 (17.53%), 0 x 4 (12.98%)
    *   **Nível de Confiança:** Alta

### **Grupo F**

*   **Japão 3 x 1 Suécia**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.43 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Japão (2.87) vs. Suécia (1.41). Fatores Físicos: Japão viajou 1017 km com 5 dias de descanso; Suécia viajou 27 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Japão: 58.4% | Empate: 22.6% | Vitória Suécia: 18.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (8.26%), 2 x 1 (7.88%), 3 x 1 (7.53%)
    *   **Nível de Confiança:** Baixa

*   **Tunísia 0 x 4 Holanda**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 16.52 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Tunísia (0.52) vs. Holanda (5.68). Fatores Físicos: Tunísia viajou 1583 km com 5 dias de descanso; Holanda viajou 10 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Tunísia: 2.5% | Empate: 7.6% | Vitória Holanda: 89.9%
    *   **Top 3 Placares mais Prováveis:** 0 x 5 (18.74%), 0 x 4 (16.49%), 0 x 3 (11.60%)
    *   **Nível de Confiança:** Alta

### **Grupo D**

*   **Turquia 0 x 4 EUA**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.48 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Turquia (0.28) vs. EUA (4.14). Fatores Físicos: Turquia viajou 605 km com 6 dias de descanso; EUA viajou 56 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Turquia: 16.0% | Empate: 16.1% | Vitória EUA: 67.9%
    *   **Top 3 Placares mais Prováveis:** 0 x 4 (13.80%), 0 x 3 (13.32%), 0 x 5 (11.43%)
    *   **Nível de Confiança:** Média

*   **Paraguai 1 x 1 Austrália**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.05 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Paraguai (0.93) vs. Austrália (1.38). Fatores Físicos: Paraguai viajou 10 km com 6 dias de descanso; Austrália viajou 47 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Paraguai: 27.6% | Empate: 36.5% | Vitória Austrália: 35.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (17.13%), 0 x 0 (13.85%), 0 x 1 (9.37%)
    *   **Nível de Confiança:** Alta

### **Grupo I**

*   **Noruega 0 x 3 França**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (26/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.44 pts) para o bolão com blending de 45% modelo / 55% odds de mercado (Ambas Classificadas (Poupa de Elenco)). Médias de gols projetadas: Noruega (0.38) vs. França (4.64). Fatores Físicos: Noruega viajou 994 km com 4 dias de descanso; França viajou 34 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Noruega: 13.9% | Empate: 18.6% | Vitória França: 67.5%
    *   **Top 3 Placares mais Prováveis:** 0 x 4 (13.36%), 0 x 5 (12.40%), 0 x 3 (11.52%)
    *   **Nível de Confiança:** Média

*   **Senegal 3 x 0 Iraque**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (26/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.15 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Senegal (3.24) vs. Iraque (0.94). Fatores Físicos: Senegal viajou 539 km com 4 dias de descanso; Iraque viajou 655 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Senegal: 62.9% | Empate: 22.3% | Vitória Iraque: 14.8%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (9.52%), 3 x 0 (7.83%), 3 x 1 (7.34%)
    *   **Nível de Confiança:** Baixa

### **Grupo H**

*   **Cabo Verde 2 x 1 Arábia Saudita**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (26/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.21 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Cabo Verde (2.09) vs. Arábia Saudita (0.69). Fatores Físicos: Cabo Verde viajou 1276 km com 5 dias de descanso; Arábia Saudita viajou 234 km com 5 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória Cabo Verde: 54.5% | Empate: 25.9% | Vitória Arábia Saudita: 19.7%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.31%), 2 x 0 (11.08%), 1 x 0 (9.50%)
    *   **Nível de Confiança:** Média

*   **Uruguai 1 x 2 Espanha**
    *   **Estádio:** Guadalajara Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (26/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.75 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Uruguai (0.34) vs. Espanha (2.57). Fatores Físicos: Uruguai viajou 1705 km com 5 dias de descanso; Espanha viajou 2387 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Uruguai: 12.1% | Empate: 19.9% | Vitória Espanha: 68.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (15.25%), 0 x 3 (13.08%), 0 x 1 (11.25%)
    *   **Nível de Confiança:** Média

### **Grupo G**

*   **Egito 2 x 1 Irã**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.09 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Egito (1.50) vs. Irã (1.01). Fatores Físicos: Egito viajou 368 km com 6 dias de descanso; Irã viajou 1735 km com 6 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória Egito: 47.9% | Empate: 29.4% | Vitória Irã: 22.6%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (14.06%), 1 x 0 (10.74%), 0 x 0 (9.92%)
    *   **Nível de Confiança:** Média

*   **Nova Zelândia 0 x 3 Bélgica**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.16 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Nova Zelândia (0.89) vs. Bélgica (3.02). Fatores Físicos: Nova Zelândia viajou 1907 km com 6 dias de descanso; Bélgica viajou 210 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Nova Zelândia: 8.9% | Empate: 17.2% | Vitória Bélgica: 73.9%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (9.69%), 0 x 2 (9.61%), 1 x 3 (8.58%)
    *   **Nível de Confiança:** Baixa

### **Grupo L**

*   **Panamá 0 x 3 Inglaterra**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.52 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Panamá (0.15) vs. Inglaterra (3.84). Fatores Físicos: Panamá viajou 539 km com 4 dias de descanso; Inglaterra viajou 1754 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Panamá: 5.0% | Empate: 11.4% | Vitória Inglaterra: 83.5%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (18.92%), 0 x 4 (18.15%), 0 x 2 (14.79%)
    *   **Nível de Confiança:** Alta

*   **Croácia 1 x 0 Gana**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.43 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Croácia (0.69) vs. Gana (1.15). Fatores Físicos: Croácia viajou 202 km com 4 dias de descanso; Gana viajou 378 km com 4 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória Croácia: 34.2% | Empate: 31.8% | Vitória Gana: 34.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 0 (16.10%), 1 x 0 (15.32%), 1 x 1 (13.19%)
    *   **Nível de Confiança:** Alta

### **Grupo K**

*   **Colômbia 1 x 2 Portugal**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.41 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Colômbia (1.19) vs. Portugal (2.55). Fatores Físicos: Colômbia viajou 2432 km com 4 dias de descanso; Portugal viajou 86 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Colômbia: 21.6% | Empate: 25.8% | Vitória Portugal: 52.6%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.01%), 1 x 2 (7.90%), 2 x 2 (7.24%)
    *   **Nível de Confiança:** Média

*   **RD Congo 2 x 0 Uzbequistão**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.33 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: RD Congo (2.04) vs. Uzbequistão (0.96). Fatores Físicos: RD Congo viajou 1127 km com 4 dias de descanso; Uzbequistão viajou 2 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória RD Congo: 50.5% | Empate: 27.1% | Vitória Uzbequistão: 22.5%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.86%), 2 x 0 (8.87%), 2 x 1 (8.48%)
    *   **Nível de Confiança:** Média

### **Grupo J**

*   **Argélia 1 x 2 Áustria**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.03 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Argélia (1.21) vs. Áustria (1.96). Fatores Físicos: Argélia viajou 65 km com 5 dias de descanso; Áustria viajou 2297 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Argélia: 29.6% | Empate: 27.2% | Vitória Áustria: 43.2%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.54%), 2 x 1 (8.22%), 1 x 2 (8.14%)
    *   **Nível de Confiança:** Média

*   **Jordânia 0 x 4 Argentina**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.95 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Jordânia (0.09) vs. Argentina (5.56). Fatores Físicos: Jordânia viajou 2607 km com 5 dias de descanso; Argentina viajou 741 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Jordânia: 5.7% | Empate: 11.3% | Vitória Argentina: 83.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 5 (25.11%), 0 x 4 (22.59%), 0 x 3 (16.25%)
    *   **Nível de Confiança:** Alta

