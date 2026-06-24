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
| **B** | Suíça vs. Canadá | Vancouver Stadium | Preditivo | **1 x 2** | **Média** | 7.78 pts | Duelo Direto Decisivo (w: 0.55) |
| **B** | Bósnia e Herzegovina vs. Catar | Seattle Stadium | Preditivo | **2 x 1** | **Média** | 10.96 pts | Duelo Direto Decisivo (w: 0.55) |
| **C** | Escócia vs. Brasil | Miami Stadium | Preditivo | **0 x 2** | **Média** | 13.60 pts | Duelo Direto Decisivo (w: 0.55) |
| **C** | Marrocos vs. Haiti | Atlanta Stadium | Preditivo | **2 x 0** | **Alta** | 15.90 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **A** | Tchéquia vs. México | Mexico City Stadium | Preditivo | **0 x 2** | **Alta** | 12.41 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **A** | África do Sul vs. Coreia do Sul | Monterrey Stadium | Preditivo | **0 x 2** | **Média** | 11.13 pts | Duelo Direto Decisivo (w: 0.55) |
| **E** | Equador vs. Alemanha | New York New Jersey Stadium | Preditivo | **0 x 2** | **Alta** | 12.78 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **E** | Curaçao vs. Costa do Marfim | Philadelphia Stadium | Preditivo | **0 x 3** | **Média** | 15.67 pts | Duelo Direto Decisivo (w: 0.55) |
| **F** | Japão vs. Suécia | Dallas Stadium | Preditivo | **3 x 1** | **Baixa** | 10.42 pts | Duelo Direto Decisivo (w: 0.55) |
| **F** | Tunísia vs. Holanda | Kansas City Stadium | Preditivo | **0 x 4** | **Alta** | 16.49 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **D** | Turquia vs. EUA | Los Angeles Stadium | Preditivo | **0 x 3** | **Média** | 12.39 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **D** | Paraguai vs. Austrália | San Francisco Bay Stadium | Preditivo | **1 x 1** | **Alta** | 8.05 pts | Duelo Direto Decisivo (w: 0.55) |
| **I** | Noruega vs. França | Boston Stadium | Preditivo | **1 x 3** | **Baixa** | 10.34 pts | Ambas Classificadas (Poupa de Elenco) (w: 0.45) |
| **I** | Senegal vs. Iraque | Toronto Stadium | Preditivo | **3 x 0** | **Baixa** | 11.05 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **H** | Cabo Verde vs. Arábia Saudita | Houston Stadium | Preditivo | **2 x 0** | **Média** | 10.06 pts | Duelo Direto Decisivo (w: 0.55) |
| **H** | Uruguai vs. Espanha | Guadalajara Stadium | Preditivo | **0 x 3** | **Média** | 13.36 pts | Duelo Direto Decisivo (w: 0.55) |
| **G** | Egito vs. Irã | Seattle Stadium | Preditivo | **2 x 0** | **Média** | 9.02 pts | Duelo Direto Decisivo (w: 0.55) |
| **G** | Nova Zelândia vs. Bélgica | Vancouver Stadium | Preditivo | **0 x 2** | **Média** | 13.14 pts | Duelo Direto Decisivo (w: 0.55) |
| **L** | Panamá vs. Inglaterra | New York New Jersey Stadium | Preditivo | **0 x 3** | **Alta** | 15.46 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **L** | Croácia vs. Gana | Philadelphia Stadium | Preditivo | **0 x 0** | **Alta** | 7.65 pts | Duelo Direto Decisivo (w: 0.55) |
| **K** | Colômbia vs. Portugal | Miami Stadium | Preditivo | **1 x 2** | **Média** | 9.41 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **K** | RD Congo vs. Uzbequistão | Atlanta Stadium | Preditivo | **2 x 0** | **Média** | 9.33 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **J** | Argélia vs. Áustria | Kansas City Stadium | Preditivo | **1 x 2** | **Média** | 8.02 pts | Duelo Direto Decisivo (w: 0.55) |
| **J** | Jordânia vs. Argentina | Dallas Stadium | Preditivo | **0 x 4** | **Alta** | 15.86 pts | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |

---

## 🔍 Análise Detalhada Jogo a Jogo

### **Grupo B**

*   **Suíça 1 x 2 Canadá**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.78 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Suíça (1.39) vs. Canadá (2.18). Fatores Físicos: Suíça viajou 1873 km com 6 dias de descanso; Canadá viajou 1 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Suíça: 31.7% | Empate: 25.9% | Vitória Canadá: 42.4%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.04%), 2 x 1 (8.37%), 1 x 2 (7.60%)
    *   **Nível de Confiança:** Média

*   **Bósnia e Herzegovina 2 x 1 Catar**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.96 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Bósnia e Herzegovina (1.73) vs. Catar (1.02). Fatores Físicos: Bósnia e Herzegovina viajou 1137 km com 6 dias de descanso; Catar viajou 1481 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Bósnia e Herzegovina: 58.4% | Empate: 24.3% | Vitória Catar: 17.3%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.63%), 2 x 1 (11.05%), 2 x 0 (10.87%)
    *   **Nível de Confiança:** Média

### **Grupo C**

*   **Escócia 0 x 2 Brasil**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.60 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Escócia (0.62) vs. Brasil (2.37). Fatores Físicos: Escócia viajou 1032 km com 5 dias de descanso; Brasil viajou 1733 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Escócia: 8.2% | Empate: 18.5% | Vitória Brasil: 73.3%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (14.35%), 0 x 3 (11.35%), 0 x 1 (10.96%)
    *   **Nível de Confiança:** Média

*   **Marrocos 2 x 0 Haiti**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.90 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Marrocos (2.98) vs. Haiti (0.06). Fatores Físicos: Marrocos viajou 1164 km com 5 dias de descanso; Haiti viajou 1082 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Marrocos: 84.6% | Empate: 12.0% | Vitória Haiti: 3.4%
    *   **Top 3 Placares mais Prováveis:** 2 x 0 (21.00%), 3 x 0 (20.85%), 4 x 0 (15.53%)
    *   **Nível de Confiança:** Alta

### **Grupo A**

*   **Tchéquia 0 x 2 México**
    *   **Estádio:** Mexico City Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.41 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Tchéquia (0.11) vs. México (2.64). Fatores Físicos: Tchéquia viajou 1488 km com 6 dias de descanso; México viajou 0 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Tchéquia: 15.2% | Empate: 19.7% | Vitória México: 65.1%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (16.96%), 0 x 3 (14.91%), 0 x 0 (14.49%)
    *   **Nível de Confiança:** Alta

*   **África do Sul 0 x 2 Coreia do Sul**
    *   **Estádio:** Monterrey Stadium (Temperatura: 30°C)
    *   **Status:** Preditivo (24/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.13 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: África do Sul (0.75) vs. Coreia do Sul (1.75). Fatores Físicos: África do Sul viajou 638 km com 6 dias de descanso; Coreia do Sul viajou 641 km com 6 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória África do Sul: 15.5% | Empate: 25.9% | Vitória Coreia do Sul: 58.5%
    *   **Top 3 Placares mais Prováveis:** 0 x 1 (12.77%), 0 x 2 (12.56%), 1 x 1 (12.19%)
    *   **Nível de Confiança:** Média

### **Grupo E**

*   **Equador 0 x 2 Alemanha**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.78 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Equador (0.11) vs. Alemanha (2.49). Fatores Físicos: Equador viajou 759 km com 5 dias de descanso; Alemanha viajou 750 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Equador: 14.9% | Empate: 18.5% | Vitória Alemanha: 66.6%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (17.97%), 0 x 3 (14.95%), 0 x 1 (14.17%)
    *   **Nível de Confiança:** Alta

*   **Curaçao 0 x 3 Costa do Marfim**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.67 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Curaçao (0.52) vs. Costa do Marfim (3.64). Fatores Físicos: Curaçao viajou 1573 km com 5 dias de descanso; Costa do Marfim viajou 17 km com 5 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória Curaçao: 3.4% | Empate: 9.8% | Vitória Costa do Marfim: 86.8%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (14.51%), 0 x 4 (13.20%), 0 x 2 (11.97%)
    *   **Nível de Confiança:** Média

### **Grupo F**

*   **Japão 3 x 1 Suécia**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.42 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Japão (2.86) vs. Suécia (1.41). Fatores Físicos: Japão viajou 1017 km com 5 dias de descanso; Suécia viajou 27 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Japão: 58.4% | Empate: 22.7% | Vitória Suécia: 18.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (8.32%), 2 x 1 (7.91%), 3 x 1 (7.54%)
    *   **Nível de Confiança:** Baixa

*   **Tunísia 0 x 4 Holanda**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 16.49 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Tunísia (0.49) vs. Holanda (5.24). Fatores Físicos: Tunísia viajou 1583 km com 5 dias de descanso; Holanda viajou 10 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Tunísia: 2.5% | Empate: 7.8% | Vitória Holanda: 89.7%
    *   **Top 3 Placares mais Prováveis:** 0 x 5 (17.55%), 0 x 4 (16.74%), 0 x 3 (12.77%)
    *   **Nível de Confiança:** Alta

### **Grupo D**

*   **Turquia 0 x 3 EUA**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.39 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Turquia (0.28) vs. EUA (3.82). Fatores Físicos: Turquia viajou 605 km com 6 dias de descanso; EUA viajou 56 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Turquia: 16.1% | Empate: 16.4% | Vitória EUA: 67.5%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (13.69%), 0 x 4 (13.09%), 0 x 2 (10.75%)
    *   **Nível de Confiança:** Média

*   **Paraguai 1 x 1 Austrália**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (25/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.05 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Paraguai (0.92) vs. Austrália (1.38). Fatores Físicos: Paraguai viajou 10 km com 6 dias de descanso; Austrália viajou 47 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Paraguai: 27.6% | Empate: 36.5% | Vitória Austrália: 35.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (17.13%), 0 x 0 (13.95%), 0 x 1 (9.44%)
    *   **Nível de Confiança:** Alta

### **Grupo I**

*   **Noruega 1 x 3 França**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (26/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.34 pts) para o bolão com blending de 45% modelo / 55% odds de mercado (Ambas Classificadas (Poupa de Elenco)). Médias de gols projetadas: Noruega (1.07) vs. França (3.14). Fatores Físicos: Noruega viajou 994 km com 4 dias de descanso; França viajou 34 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Noruega: 17.9% | Empate: 23.7% | Vitória França: 58.3%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (9.67%), 1 x 3 (7.10%), 2 x 2 (7.06%)
    *   **Nível de Confiança:** Baixa

*   **Senegal 3 x 0 Iraque**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (26/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.05 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Senegal (2.76) vs. Iraque (0.81). Fatores Físicos: Senegal viajou 539 km com 4 dias de descanso; Iraque viajou 655 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Senegal: 61.8% | Empate: 23.3% | Vitória Iraque: 14.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (10.86%), 2 x 0 (9.34%), 3 x 0 (8.60%)
    *   **Nível de Confiança:** Baixa

### **Grupo H**

*   **Cabo Verde 2 x 0 Arábia Saudita**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (26/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.06 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Cabo Verde (1.79) vs. Arábia Saudita (0.59). Fatores Físicos: Cabo Verde viajou 1276 km com 5 dias de descanso; Arábia Saudita viajou 234 km com 5 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória Cabo Verde: 52.5% | Empate: 27.6% | Vitória Arábia Saudita: 19.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.48%), 1 x 0 (12.37%), 2 x 0 (12.15%)
    *   **Nível de Confiança:** Média

*   **Uruguai 0 x 3 Espanha**
    *   **Estádio:** Guadalajara Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (26/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.36 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Uruguai (0.27) vs. Espanha (3.38). Fatores Físicos: Uruguai viajou 1705 km com 5 dias de descanso; Espanha viajou 2387 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Uruguai: 11.2% | Empate: 16.5% | Vitória Espanha: 72.4%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (15.15%), 0 x 2 (13.44%), 0 x 4 (12.80%)
    *   **Nível de Confiança:** Média

### **Grupo G**

*   **Egito 2 x 0 Irã**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.02 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Egito (1.38) vs. Irã (0.93). Fatores Físicos: Egito viajou 368 km com 6 dias de descanso; Irã viajou 1735 km com 6 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória Egito: 47.2% | Empate: 30.2% | Vitória Irã: 22.5%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (14.21%), 1 x 0 (12.30%), 0 x 0 (11.44%)
    *   **Nível de Confiança:** Média

*   **Nova Zelândia 0 x 2 Bélgica**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.14 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Nova Zelândia (0.76) vs. Bélgica (2.60). Fatores Físicos: Nova Zelândia viajou 1907 km com 6 dias de descanso; Bélgica viajou 210 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Nova Zelândia: 9.1% | Empate: 18.4% | Vitória Bélgica: 72.5%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (12.04%), 0 x 3 (10.44%), 1 x 2 (9.10%)
    *   **Nível de Confiança:** Média

### **Grupo L**

*   **Panamá 0 x 3 Inglaterra**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.46 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Panamá (0.17) vs. Inglaterra (3.83). Fatores Físicos: Panamá viajou 539 km com 4 dias de descanso; Inglaterra viajou 1754 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Panamá: 5.1% | Empate: 11.5% | Vitória Inglaterra: 83.4%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (18.54%), 0 x 4 (17.73%), 0 x 2 (14.53%)
    *   **Nível de Confiança:** Alta

*   **Croácia 0 x 0 Gana**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.65 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Croácia (0.62) vs. Gana (1.06). Fatores Físicos: Croácia viajou 202 km com 4 dias de descanso; Gana viajou 378 km com 4 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto, contendo o ímpeto de gols. 
    *   **Probabilidades:** Vitória Croácia: 33.6% | Empate: 32.7% | Vitória Gana: 33.7%
    *   **Top 3 Placares mais Prováveis:** 0 x 0 (18.29%), 1 x 0 (16.89%), 0 x 1 (13.78%)
    *   **Nível de Confiança:** Alta

### **Grupo K**

*   **Colômbia 1 x 2 Portugal**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.41 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Colômbia (1.18) vs. Portugal (2.53). Fatores Físicos: Colômbia viajou 2432 km com 4 dias de descanso; Portugal viajou 86 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Colômbia: 21.6% | Empate: 25.8% | Vitória Portugal: 52.6%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.10%), 1 x 2 (7.93%), 2 x 2 (7.18%)
    *   **Nível de Confiança:** Média

*   **RD Congo 2 x 0 Uzbequistão**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.33 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: RD Congo (1.75) vs. Uzbequistão (0.82). Fatores Físicos: RD Congo viajou 1127 km com 4 dias de descanso; Uzbequistão viajou 2 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória RD Congo: 49.3% | Empate: 28.2% | Vitória Uzbequistão: 22.5%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (13.41%), 1 x 0 (10.16%), 2 x 0 (10.13%)
    *   **Nível de Confiança:** Média

### **Grupo J**

*   **Argélia 1 x 2 Áustria**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.02 pts) para o bolão com blending de 55% modelo / 45% odds de mercado (Duelo Direto Decisivo). Médias de gols projetadas: Argélia (1.21) vs. Áustria (1.96). Fatores Físicos: Argélia viajou 65 km com 5 dias de descanso; Áustria viajou 2297 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Argélia: 29.6% | Empate: 27.3% | Vitória Áustria: 43.1%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.56%), 2 x 1 (8.23%), 1 x 2 (8.14%)
    *   **Nível de Confiança:** Média

*   **Jordânia 0 x 4 Argentina**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (27/Jun)
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.86 pts) para o bolão com blending de 40% modelo / 60% odds de mercado (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Jordânia (0.09) vs. Argentina (5.12). Fatores Físicos: Jordânia viajou 2607 km com 5 dias de descanso; Argentina viajou 741 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Jordânia: 5.7% | Empate: 11.5% | Vitória Argentina: 82.9%
    *   **Top 3 Placares mais Prováveis:** 0 x 5 (22.72%), 0 x 4 (22.18%), 0 x 3 (17.33%)
    *   **Nível de Confiança:** Alta

