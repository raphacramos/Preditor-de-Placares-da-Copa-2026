# 📊 Relatório Preditivo: 2ª Rodada da Copa do Mundo FIFA 2026

Este relatório apresenta a análise estatística e tática atualizada para todas as 24 partidas da segunda rodada da fase de grupos. A metodologia preditiva foi calibrada e otimizada integrando as **odds reais de mercado** (40% de peso) e o modelo Dixon-Coles sintonizado (60% de peso).

Com as primeiras 16 partidas da rodada 2 já realizadas, o modelo foi recalibrado (com o banco de dados expandido para **40 jogos concluídos** no total). As previsões para as 8 partidas restantes foram geradas com base nesses novos parâmetros calibrados.

---

## 🏆 Painel de Desempenho (Bolão - 2ª Rodada)

- **Partidas Concluídas:** 16
- **Pontuação Total Acumulada:** **185 pontos** (média de 11.56 pts por partida)
- **Aproveitamento de Desfecho (Vitória/Empate/Derrota):** **68.8%** (11 acertos em 16 jogos)
  - 🎯 **Acertos de Placar Exato (30 pts):** 1
  - ⚽ **Acertos de Vencedor + Gols do Vencedor (20 pts):** 1
  - 👍 **Acertos Secos de Vencedor (15 pts):** 9
  - ❌ **Erros (0 pts):** 5

---

## 📅 Resumo dos Palpites (Tabela Rápida para o Bolão)

| Grupo | Confronto | Local / Estádio | Status | Palpite Sugerido | Resultado Real | Pontos Obtidos | Confiança |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **A** | Tchéquia vs. África do Sul | Atlanta Stadium | *Concluído* | **2 x 0** | **1 x 1** | **0 pts** (Erro) | **Média** |
| **A** | México vs. Coreia do Sul | Mexico City Stadium | *Concluído* | **2 x 1** | **1 x 0** | **15 pts** (Acerto Vencedor Seco) | **Média** |
| **B** | Suíça vs. Bósnia e Herzegovina | Los Angeles Stadium | *Concluído* | **2 x 0** | **4 x 1** | **15 pts** (Acerto Vencedor Seco) | **Média** |
| **B** | Canadá vs. Catar | Vancouver Stadium | *Concluído* | **2 x 1** | **6 x 0** | **15 pts** (Acerto Vencedor Seco) | **Média** |
| **C** | Escócia vs. Marrocos | Boston Stadium | *Concluído* | **0 x 2** | **0 x 1** | **15 pts** (Acerto Vencedor Seco) | **Média** |
| **C** | Brasil vs. Haiti | Philadelphia Stadium | *Concluído* | **4 x 0** | **3 x 0** | **15 pts** (Acerto Vencedor Seco) | **Alta** |
| **D** | EUA vs. Austrália | Seattle Stadium | *Concluído* | **2 x 1** | **2 x 0** | **20 pts** (Acerto Vencedor + Gols do Vencedor) | **Média** |
| **D** | Turquia vs. Paraguai | San Francisco Bay Stadium | *Concluído* | **2 x 1** | **0 x 1** | **0 pts** (Erro) | **Média** |
| **E** | Alemanha vs. Costa do Marfim | Toronto Stadium | *Concluído* | **2 x 1** | **2 x 1** | **30 pts** (Acerto Placar Exato) | **Média** |
| **E** | Equador vs. Curaçao | Kansas City Stadium | *Concluído* | **2 x 0** | **0 x 0** | **0 pts** (Erro) | **Média** |
| **F** | Holanda vs. Suécia | Houston Stadium | *Concluído* | **2 x 1** | **5 x 1** | **15 pts** (Acerto Vencedor Seco) | **Baixa** |
| **F** | Tunísia vs. Japão | Monterrey Stadium | *Concluído* | **0 x 3** | **0 x 4** | **15 pts** (Acerto Vencedor Seco) | **Baixa** |
| **G** | Bélgica vs. Irã | Los Angeles Stadium | *Concluído* | **2 x 1** | **0 x 0** | **0 pts** (Erro) | **Baixa** |
| **G** | Nova Zelândia vs. Egito | Vancouver Stadium | *Concluído* | **0 x 2** | **1 x 3** | **15 pts** (Acerto Vencedor Seco) | **Média** |
| **H** | Espanha vs. Arábia Saudita | Atlanta Stadium | *Concluído* | **3 x 0** | **4 x 0** | **15 pts** (Acerto Vencedor Seco) | **Média** |
| **H** | Uruguai vs. Cabo Verde | Miami Stadium | *Concluído* | **1 x 0** | **2 x 2** | **0 pts** (Erro) | **Alta** |
| **I** | França vs. Iraque | Philadelphia Stadium | Preditivo | **4 x 0** | - | EV: 16.71 pts | **Alta** |
| **I** | Noruega vs. Senegal | New York New Jersey Stadium | Preditivo | **2 x 1** | - | EV: 8.80 pts | **Baixa** |
| **J** | Argentina vs. Áustria | Dallas Stadium | Preditivo | **3 x 0** | - | EV: 13.99 pts | **Média** |
| **J** | Jordânia vs. Argélia | San Francisco Bay Stadium | Preditivo | **1 x 2** | - | EV: 9.76 pts | **Média** |
| **K** | Portugal vs. Uzbequistão | Houston Stadium | Preditivo | **3 x 0** | - | EV: 13.63 pts | **Baixa** |
| **K** | Colômbia vs. RD Congo | Guadalajara Stadium | Preditivo | **2 x 1** | - | EV: 10.82 pts | **Média** |
| **L** | Inglaterra vs. Gana | Boston Stadium | Preditivo | **3 x 1** | - | EV: 13.16 pts | **Baixa** |
| **L** | Panamá vs. Croácia | Toronto Stadium | Preditivo | **0 x 2** | - | EV: 13.22 pts | **Média** |

---

## 🔍 Análise Detalhada Jogo a Jogo

### **Grupo A**

*   **Tchéquia 2 x 0 África do Sul**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Concluído (18/Jun) - Real: **1 x 1**
    *   **Justificativa:** A África do Sul surpreendeu ao segurar a Tchéquia em um empate de 1 a 1, contrariando o favoritismo do modelo que projetava maior volume ofensivo europeu. O empate quebrou o palpite seco de vitória da Tchéquia.
    *   **Pontuação:** Pontuação obtida: 0 pts (Erro).
    *   **Nível de Confiança:** Média

*   **México 2 x 1 Coreia do Sul**
    *   **Estádio:** Mexico City Stadium (Temperatura: 20°C)
    *   **Status:** Concluído (18/Jun) - Real: **1 x 0**
    *   **Justificativa:** O México soube utilizar o fator altitude e o apoio massivo no Estádio Azteca para vencer a Coreia do Sul por 1 a 0. O palpite de 2x1 garantiu 15 pontos de vitória seca no bolão.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

### **Grupo B**

*   **Suíça 2 x 0 Bósnia e Herzegovina**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Concluído (18/Jun) - Real: **4 x 1**
    *   **Justificativa:** A Suíça impôs um ritmo ofensivo avassalador, superando com facilidade a defesa bósnia por 4 a 1. O palpite de 2x0 garantiu a vitória seca da Suíça (15 pontos).
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

*   **Canadá 2 x 1 Catar**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Concluído (18/Jun) - Real: **6 x 0**
    *   **Justificativa:** Jogando em Vancouver, o Canadá aplicou uma goleada histórica de 6 a 0 sobre o Catar, confirmando ampla superioridade técnica. O palpite seco de vitória canadense rendeu 15 pontos.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

### **Grupo C**

*   **Escócia 0 x 2 Marrocos**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Concluído (19/Jun) - Real: **0 x 1**
    *   **Justificativa:** Marrocos confirmou seu favoritismo com uma vitória taticamente muito madura por 1 a 0 sobre a Escócia. O palpite de 0x2 assegurou os 15 pontos do vencedor no bolão.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

*   **Brasil 4 x 0 Haiti**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Concluído (19/Jun) - Real: **3 x 0**
    *   **Justificativa:** O Brasil dominou completamente a partida na Filadélfia e venceu por 3 a 0. O palpite de 4x0 garantiu os 15 pontos de vitória seca do Brasil.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Alta

### **Grupo D**

*   **EUA 2 x 1 Austrália**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Concluído (19/Jun) - Real: **2 x 0**
    *   **Justificativa:** Os EUA venceram por 2 a 0 em Seattle, demonstrando excelente solidez defensiva. Como o palpite foi 2x1, houve o acerto do vencedor (EUA) e do número exato de gols do vencedor (2), garantindo a pontuação especial de 20 pontos no bolão.
    *   **Pontuação:** Pontuação obtida: 20 pts (Acerto Vencedor + Gols do Vencedor).
    *   **Nível de Confiança:** Média

*   **Turquia 2 x 1 Paraguai**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Concluído (19/Jun) - Real: **0 x 1**
    *   **Justificativa:** O Paraguai neutralizou as principais armas da Turquia e achou o gol da vitória por 1 a 0, contrariando o favoritismo do modelo. Placar de 0 pontos no bolão.
    *   **Pontuação:** Pontuação obtida: 0 pts (Erro).
    *   **Nível de Confiança:** Média

### **Grupo E**

*   **Alemanha 2 x 1 Costa do Marfim**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Concluído (20/Jun) - Real: **2 x 1**
    *   **Justificativa:** PALPITE CRAVADO COM PRECISÃO ABSOLUTA! A Alemanha superou a forte oposição física da Costa do Marfim por 2 a 1, garantindo os 30 pontos de placar exato no bolão.
    *   **Pontuação:** Pontuação obtida: 30 pts (Acerto Placar Exato).
    *   **Nível de Confiança:** Média

*   **Equador 2 x 0 Curaçao**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Concluído (20/Jun) - Real: **0 x 0**
    *   **Justificativa:** Curaçao surpreendeu ao armar uma retranca muito eficiente e segurar o Equador em um empate sem gols, quebrando o favoritismo equatoriano.
    *   **Pontuação:** Pontuação obtida: 0 pts (Erro).
    *   **Nível de Confiança:** Média

### **Grupo F**

*   **Holanda 2 x 1 Suécia**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Concluído (20/Jun) - Real: **5 x 1**
    *   **Justificativa:** A Holanda passeou em Houston e aplicou uma goleada de 5 a 1 sobre a Suécia. O palpite de 2x1 garantiu 15 pontos para a vitória seca da Holanda.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Baixa

*   **Tunísia 0 x 3 Japão**
    *   **Estádio:** Monterrey Stadium (Temperatura: 30°C)
    *   **Status:** Concluído (20/Jun) - Real: **0 x 4**
    *   **Justificativa:** O Japão sobrou em campo e venceu por 4 a 0 no Monterrey Stadium. O palpite seco de vitória japonesa rendeu 15 pontos no bolão.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Baixa

### **Grupo G**

*   **Bélgica 2 x 1 Irã**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Concluído (21/Jun) - Real: **0 x 0**
    *   **Justificativa:** O Irã se defendeu de forma heróica e arrancou um empate em 0 a 0 contra a favorita Bélgica, frustrando as projeções ofensivas e quebrando as previsões do modelo.
    *   **Pontuação:** Pontuação obtida: 0 pts (Erro).
    *   **Nível de Confiança:** Baixa

*   **Nova Zelândia 0 x 2 Egito**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Concluído (21/Jun) - Real: **1 x 3**
    *   **Justificativa:** O Egito comandado por Salah venceu com autoridade por 3 a 1, confirmando a vitória seca projetada e rendendo 15 pontos no bolão.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

### **Grupo H**

*   **Espanha 3 x 0 Arábia Saudita**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Concluído (21/Jun) - Real: **4 x 0**
    *   **Justificativa:** A Espanha goleou por 4 a 0, confirmando sua imensa disparidade técnica. O palpite de 3x0 garantiu a vitória seca da Fúria e somou 15 pontos.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

*   **Uruguai 1 x 0 Cabo Verde**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Concluído (21/Jun) - Real: **2 x 2**
    *   **Justificativa:** Cabo Verde foi valente e arrancou um empate histórico por 2 a 2 contra o Uruguai em Miami, frustrando os planos celestes e o palpite do modelo.
    *   **Pontuação:** Pontuação obtida: 0 pts (Erro).
    *   **Nível de Confiança:** Alta

### **Grupo I**

*   **França 4 x 0 Iraque**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (22/Jun) [Modelo Calibrado com 40 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 16.71 pts) sob o modelo Dixon-Coles recalibrado. Médias de gols projetadas: França (6.34) vs. Iraque (0.67). Fatores Físicos: França viajou 439 km com 6 dias de descanso; Iraque viajou 514 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória França: 91.9% | Empate: 6.1% | Vitória Iraque: 2.0%
    *   **Top 3 Placares mais Prováveis:** 5 x 0 (18.89%), 4 x 0 (14.89%), 5 x 1 (12.57%)
    *   **Nível de Confiança:** Alta

*   **Noruega 2 x 1 Senegal**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (22/Jun) [Modelo Calibrado com 40 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.80 pts) sob o modelo Dixon-Coles recalibrado. Médias de gols projetadas: Noruega (1.99) vs. Senegal (1.60). Fatores Físicos: Noruega viajou 725 km com 6 dias de descanso; Senegal viajou 48 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Noruega: 47.3% | Empate: 25.6% | Vitória Senegal: 27.1%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (10.68%), 2 x 1 (9.39%), 2 x 2 (7.40%)
    *   **Nível de Confiança:** Baixa

### **Grupo J**

*   **Argentina 3 x 0 Áustria**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (22/Jun) [Modelo Calibrado com 40 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.99 pts) sob o modelo Dixon-Coles recalibrado. Médias de gols projetadas: Argentina (3.17) vs. Áustria (0.66). Fatores Físicos: Argentina viajou 741 km com 6 dias de descanso; Áustria viajou 2099 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Argentina: 77.7% | Empate: 15.2% | Vitória Áustria: 7.0%
    *   **Top 3 Placares mais Prováveis:** 3 x 0 (12.03%), 2 x 0 (11.39%), 4 x 0 (9.52%)
    *   **Nível de Confiança:** Média

*   **Jordânia 1 x 2 Argélia**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (22/Jun) [Modelo Calibrado com 40 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.76 pts) sob o modelo Dixon-Coles recalibrado. Médias de gols projetadas: Jordânia (1.12) vs. Argélia (1.78). Fatores Físicos: Jordânia viajou 904 km com 6 dias de descanso; Argélia viajou 2335 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Jordânia: 21.4% | Empate: 26.7% | Vitória Argélia: 51.9%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.64%), 1 x 2 (10.13%), 0 x 2 (9.01%)
    *   **Nível de Confiança:** Média

### **Grupo K**

*   **Portugal 3 x 0 Uzbequistão**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (23/Jun) [Modelo Calibrado com 40 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.63 pts) sob o modelo Dixon-Coles recalibrado. Médias de gols projetadas: Portugal (3.12) vs. Uzbequistão (0.92). Fatores Físicos: Portugal viajou 1539 km com 6 dias de descanso; Uzbequistão viajou 1135 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Portugal: 76.8% | Empate: 15.4% | Vitória Uzbequistão: 7.9%
    *   **Top 3 Placares mais Prováveis:** 3 x 0 (9.74%), 2 x 0 (9.37%), 3 x 1 (8.98%)
    *   **Nível de Confiança:** Baixa

*   **Colômbia 2 x 1 RD Congo**
    *   **Estádio:** Guadalajara Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (23/Jun) [Modelo Calibrado com 40 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.82 pts) sob o modelo Dixon-Coles recalibrado. Médias de gols projetadas: Colômbia (1.80) vs. RD Congo (1.03). Fatores Físicos: Colômbia viajou 7 km com 6 dias de descanso; RD Congo viajou 1296 km com 6 dias de descanso. Equilíbrio tático acentuado projetado, favorecendo um confronto truncado e de alta disputa física no meio-campo. 
    *   **Probabilidades:** Vitória Colômbia: 57.9% | Empate: 24.9% | Vitória RD Congo: 17.3%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.87%), 2 x 1 (10.78%), 2 x 0 (10.49%)
    *   **Nível de Confiança:** Média

### **Grupo L**

*   **Inglaterra 3 x 1 Gana**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (23/Jun) [Modelo Calibrado com 40 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.16 pts) sob o modelo Dixon-Coles recalibrado. Médias de gols projetadas: Inglaterra (2.94) vs. Gana (1.03). Fatores Físicos: Inglaterra viajou 1990 km com 6 dias de descanso; Gana viajou 30 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Inglaterra: 74.2% | Empate: 16.5% | Vitória Gana: 9.3%
    *   **Top 3 Placares mais Prováveis:** 2 x 1 (9.23%), 3 x 1 (9.04%), 2 x 0 (9.00%)
    *   **Nível de Confiança:** Baixa

*   **Panamá 0 x 2 Croácia**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (23/Jun) [Modelo Calibrado com 40 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.22 pts) sob o modelo Dixon-Coles recalibrado. Médias de gols projetadas: Panamá (0.51) vs. Croácia (2.68). Fatores Físicos: Panamá viajou 4 km com 6 dias de descanso; Croácia viajou 572 km com 6 dias de descanso. O modelo identificou alta disparidade técnica entre as equipes, aplicando o Coeficiente de Disparidade (Disparity Boost) para capturar a probabilidade de um placar elástico. 
    *   **Probabilidades:** Vitória Panamá: 9.4% | Empate: 18.7% | Vitória Croácia: 71.9%
    *   **Top 3 Placares mais Prováveis:** 0 x 2 (13.86%), 0 x 3 (12.36%), 0 x 1 (9.56%)
    *   **Nível de Confiança:** Média
