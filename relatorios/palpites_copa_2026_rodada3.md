# 📊 Relatório Preditivo: 3ª Rodada da Copa do Mundo FIFA 2026

Este relatório apresenta a análise estatística e tática detalhada para todas as 24 partidas da terceira e última rodada da fase de grupos. A metodologia preditiva foi calibrada e otimizada integrando as **odds reais de mercado** e o modelo Dixon-Coles sintonizado.

Com as primeiras 8 partidas da rodada 3 já realizadas (jogos de 24/Jun e início de 25/Jun), o modelo foi recalibrado (com o banco de dados expandido para **56 jogos concluídos** no total). As previsões para os 16 jogos restantes foram geradas utilizando o modelo calibrado sob esta base expandida.

---

## 🏆 Painel de Desempenho (Bolão - 3ª Rodada Parcial)

- **Partidas Concluídas:** 8
- **Pontuação Total Acumulada:** **75 pontos** (média de 9.38 pts por partida)
- **Aproveitamento de Desfecho (Vitória/Empate/Derrota):** **62.5%** (5 acertos em 8 jogos)
  - 🎯 **Acertos de Placar Exato (30 pts):** 0
  - ⚽ **Acertos de Vencedor + Gols do Vencedor (20 pts):** 0
  - 👍 **Acertos Secos de Vencedor (15 pts):** 5
  - ❌ **Erros (0 pts):** 3

---

## 📅 Resumo dos Palpites (Tabela Rápida para o Bolão)

| Grupo | Confronto | Local / Estádio | Status | Palpite Sugerido | Resultado Real | Pontos Obtidos | Confiança | Contexto de Peso |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **B** | Suíça vs. Canadá | Vancouver Stadium | *Concluído* | **1 x 2** | **2 x 1** | **0 pts** (Erro) | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **B** | Bósnia e Herzegovina vs. Catar | Seattle Stadium | *Concluído* | **2 x 1** | **3 x 1** | **15 pts** (Acerto Vencedor Seco) | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **C** | Escócia vs. Brasil | Miami Stadium | *Concluído* | **0 x 2** | **0 x 3** | **15 pts** (Acerto Vencedor Seco) | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **C** | Marrocos vs. Haiti | Atlanta Stadium | *Concluído* | **2 x 0** | **4 x 2** | **15 pts** (Acerto Vencedor Seco) | **Alta** | Motivação Assimétrica (w: 0.40) |
| **A** | Tchéquia vs. México | Mexico City Stadium | *Concluído* | **0 x 2** | **0 x 3** | **15 pts** (Acerto Vencedor Seco) | **Alta** | Motivação Assimétrica (w: 0.40) |
| **A** | África do Sul vs. Coreia do Sul | Monterrey Stadium | *Concluído* | **0 x 2** | **1 x 0** | **0 pts** (Erro) | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **E** | Equador vs. Alemanha | New York New Jersey Stadium | *Concluído* | **0 x 2** | **2 x 1** | **0 pts** (Erro) | **Alta** | Motivação Assimétrica (w: 0.40) |
| **E** | Curaçao vs. Costa do Marfim | Philadelphia Stadium | *Concluído* | **0 x 3** | **0 x 2** | **15 pts** (Acerto Vencedor Seco) | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **F** | Japão vs. Suécia | Dallas Stadium | Preditivo | **3 x 1** | - | EV: 10.46 pts | **Baixa** | Duelo Direto Decisivo (w: 0.55) |
| **F** | Tunísia vs. Holanda | Kansas City Stadium | Preditivo | **0 x 4** | - | EV: 16.55 pts | **Alta** | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **D** | Turquia vs. EUA | Los Angeles Stadium | Preditivo | **0 x 4** | - | EV: 12.53 pts | **Média** | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **D** | Paraguai vs. Austrália | San Francisco Bay Stadium | Preditivo | **1 x 1** | - | EV: 8.04 pts | **Alta** | Duelo Direto Decisivo (w: 0.55) |
| **I** | Noruega vs. França | Boston Stadium | Preditivo | **1 x 3** | - | EV: 10.35 pts | **Baixa** | Ambas Classificadas (Poupa de Elenco) (w: 0.45) |
| **I** | Senegal vs. Iraque | Toronto Stadium | Preditivo | **3 x 0** | - | EV: 11.17 pts | **Baixa** | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **H** | Cabo Verde vs. Arábia Saudita | Houston Stadium | Preditivo | **2 x 0** | - | EV: 10.25 pts | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **H** | Uruguai vs. Espanha | Guadalajara Stadium | Preditivo | **0 x 3** | - | EV: 13.41 pts | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **G** | Egito vs. Irã | Seattle Stadium | Preditivo | **2 x 1** | - | EV: 9.11 pts | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **G** | Nova Zelândia vs. Bélgica | Vancouver Stadium | Preditivo | **0 x 3** | - | EV: 13.18 pts | **Baixa** | Duelo Direto Decisivo (w: 0.55) |
| **L** | Panamá vs. Inglaterra | New York New Jersey Stadium | Preditivo | **0 x 3** | - | EV: 15.55 pts | **Alta** | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **L** | Croácia vs. Gana | Philadelphia Stadium | Preditivo | **1 x 0** | - | EV: 7.42 pts | **Alta** | Duelo Direto Decisivo (w: 0.55) |
| **K** | Colômbia vs. Portugal | Miami Stadium | Preditivo | **1 x 2** | - | EV: 9.40 pts | **Média** | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **K** | RD Congo vs. Uzbequistão | Atlanta Stadium | Preditivo | **2 x 0** | - | EV: 9.37 pts | **Média** | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |
| **J** | Argélia vs. Áustria | Kansas City Stadium | Preditivo | **1 x 2** | - | EV: 8.04 pts | **Média** | Duelo Direto Decisivo (w: 0.55) |
| **J** | Jordânia vs. Argentina | Dallas Stadium | Preditivo | **0 x 4** | - | EV: 15.96 pts | **Alta** | Motivação Assimétrica (Misto de Titulares/Reservas) (w: 0.40) |

---

## 🔍 Análise Detalhada Jogo a Jogo

### **Grupo B**

*   **Suíça 1 x 2 Canadá**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Concluído (24/Jun) - Real: **2 x 1**
    *   **Justificativa:** A Suíça jogou de forma muito sólida em Vancouver e venceu o Canadá por 2 a 1, superando o favoritismo canadense projetado pelo modelo. Placar de 0 pontos no bolão.
    *   **Pontuação:** Pontuação obtida: 0 pts (Erro).
    *   **Nível de Confiança:** Média

*   **Bósnia e Herzegovina 2 x 1 Catar**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Concluído (24/Jun) - Real: **3 x 1**
    *   **Justificativa:** A Bósnia impôs sua superioridade técnica e física sobre o Catar, vencendo por 3 a 1. O palpite de 2x1 garantiu 15 pontos de vitória seca.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

### **Grupo C**

*   **Escócia 0 x 2 Brasil**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Concluído (24/Jun) - Real: **0 x 3**
    *   **Justificativa:** O Brasil teve atuação de gala sob calor em Miami e bateu a Escócia por 3 a 0. O palpite de 0x2 garantiu o acerto seco de vitória (15 pontos).
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

*   **Marrocos 2 x 0 Haiti**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Concluído (24/Jun) - Real: **4 x 2**
    *   **Justificativa:** Marrocos confirmou seu amplo favoritismo e venceu o Haiti por 4 a 2, gerando 15 pontos de vitória seca no bolão.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Alta

### **Grupo A**

*   **Tchéquia 0 x 2 México**
    *   **Estádio:** Mexico City Stadium (Temperatura: 20°C)
    *   **Status:** Concluído (24/Jun) - Real: **0 x 3**
    *   **Justificativa:** O México confirmou sua força como anfitrião e dominou a República Tcheca no Azteca, vencendo por 3 a 0. O palpite seco de vitória mexicana rendeu 15 pontos.
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Alta

*   **África do Sul 0 x 2 Coreia do Sul**
    *   **Estádio:** Monterrey Stadium (Temperatura: 30°C)
    *   **Status:** Concluído (24/Jun) - Real: **1 x 0**
    *   **Justificativa:** A África do Sul se defendeu bravamente e bateu a Coreia do Sul por 1 a 0, surpreendendo o favoritismo coreano e resultando em 0 pontos no bolão.
    *   **Pontuação:** Pontuação obtida: 0 pts (Erro).
    *   **Nível de Confiança:** Média

### **Grupo E**

*   **Equador 0 x 2 Alemanha**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Concluído (25/Jun) - Real: **2 x 1**
    *   **Justificativa:** Em confronto de motivação assimétrica, o Equador lutou intensamente e venceu a Alemanha (que já estava qualificada e poupou jogadores) por 2 a 1. Placar de 0 pontos.
    *   **Pontuação:** Pontuação obtida: 0 pts (Erro).
    *   **Nível de Confiança:** Alta

*   **Curaçao 0 x 3 Costa do Marfim**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Concluído (25/Jun) - Real: **0 x 2**
    *   **Justificativa:** A Costa do Marfim controlou o jogo e venceu Curaçao por 2 a 0. O palpite de 0x3 garantiu a vitória seca da seleção africana (15 pontos).
    *   **Pontuação:** Pontuação obtida: 15 pts (Acerto Vencedor Seco).
    *   **Nível de Confiança:** Média

### **Grupo F**

*   **Japão 3 x 1 Suécia**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (25/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.46 pts) sob o modelo Dixon-Coles recalibrado com Blending de 55% (Duelo Direto Decisivo). Médias de gols projetadas: Japão (2.88) vs. Suécia (1.41). Fatores Físicos: Japão viajou 1017 km com 5 dias de descanso; Suécia viajou 27 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Japão: 58.6% | Empate: 22.6% | Vitória Suécia: 18.8%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (8.24%), 2 x 1 (7.86%), 3 x 1 (7.55%)
    *   **Nível de Confiança:** Baixa

*   **Tunísia 0 x 4 Holanda**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (25/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 16.55 pts) sob o modelo Dixon-Coles recalibrado com Blending de 40% (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Tunísia (0.51) vs. Holanda (5.72). Fatores Físicos: Tunísia viajou 1583 km com 5 dias de descanso; Holanda viajou 10 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Tunísia: 2.5% | Empate: 7.5% | Vitória Holanda: 90.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 5 (19.07%), 0 x 4 (16.68%), 0 x 3 (11.67%)
    *   **Nível de Confiança:** Alta

### **Grupo D**

*   **Turquia 0 x 4 EUA**
    *   **Estádio:** Los Angeles Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (25/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 12.53 pts) sob o modelo Dixon-Coles recalibrado com Blending de 40% (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Turquia (0.27) vs. EUA (4.18). Fatores Físicos: Turquia viajou 605 km com 6 dias de descanso; EUA viajou 56 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Turquia: 16.0% | Empate: 16.0% | Vitória EUA: 68.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 4 (14.06%), 0 x 3 (13.47%), 0 x 5 (11.74%)
    *   **Nível de Confiança:** Média

*   **Paraguai 1 x 1 Austrália**
    *   **Estádio:** San Francisco Bay Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (25/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.04 pts) sob o modelo Dixon-Coles recalibrado com Blending de 55% (Duelo Direto Decisivo). Médias de gols projetadas: Paraguai (0.92) vs. Austrália (1.39). Fatores Físicos: Paraguai viajou 10 km com 6 dias de descanso; Austrália viajou 47 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Paraguai: 27.5% | Empate: 36.5% | Vitória Austrália: 36.0%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (17.13%), 0 x 0 (13.84%), 0 x 1 (9.37%)
    *   **Nível de Confiança:** Alta

### **Grupo I**

*   **Noruega 1 x 3 França**
    *   **Estádio:** Boston Stadium (Temperatura: 20°C)
    *   **Status:** Preditivo (26/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.35 pts) sob o modelo Dixon-Coles recalibrado com Blending de 45% (Ambas Classificadas (Poupa de Elenco)). Médias de gols projetadas: Noruega (1.08) vs. França (3.17). Fatores Físicos: Noruega viajou 994 km com 4 dias de descanso; França viajou 34 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Noruega: 17.9% | Empate: 23.7% | Vitória França: 58.4%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (9.57%), 1 x 3 (7.10%), 2 x 2 (7.09%)
    *   **Nível de Confiança:** Baixa

*   **Senegal 3 x 0 Iraque**
    *   **Estádio:** Toronto Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (26/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 11.17 pts) sob o modelo Dixon-Coles recalibrado com Blending de 40% (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Senegal (3.24) vs. Iraque (0.92). Fatores Físicos: Senegal viajou 539 km com 4 dias de descanso; Iraque viajou 655 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Senegal: 63.0% | Empate: 22.3% | Vitória Iraque: 14.7%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (9.55%), 3 x 0 (7.92%), 2 x 0 (7.33%)
    *   **Nível de Confiança:** Baixa

### **Grupo H**

*   **Cabo Verde 2 x 0 Arábia Saudita**
    *   **Estádio:** Houston Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (26/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 10.25 pts) sob o modelo Dixon-Coles recalibrado com Blending de 55% (Duelo Direto Decisivo). Médias de gols projetadas: Cabo Verde (2.10) vs. Arábia Saudita (0.68). Fatores Físicos: Cabo Verde viajou 1276 km com 5 dias de descanso; Arábia Saudita viajou 234 km com 5 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto. 
    *   **Probabilidades:** Vitória Cabo Verde: 54.7% | Empate: 25.8% | Vitória Arábia Saudita: 19.6%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.26%), 2 x 0 (11.13%), 1 x 0 (9.50%)
    *   **Nível de Confiança:** Média

*   **Uruguai 0 x 3 Espanha**
    *   **Estádio:** Guadalajara Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (26/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.41 pts) sob o modelo Dixon-Coles recalibrado com Blending de 55% (Duelo Direto Decisivo). Médias de gols projetadas: Uruguai (0.29) vs. Espanha (3.69). Fatores Físicos: Uruguai viajou 1705 km com 5 dias de descanso; Espanha viajou 2387 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Uruguai: 11.1% | Empate: 15.9% | Vitória Espanha: 73.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (14.77%), 0 x 4 (13.61%), 0 x 2 (12.01%)
    *   **Nível de Confiança:** Média

### **Grupo G**

*   **Egito 2 x 1 Irã**
    *   **Estádio:** Seattle Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (27/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.11 pts) sob o modelo Dixon-Coles recalibrado com Blending de 55% (Duelo Direto Decisivo). Médias de gols projetadas: Egito (1.50) vs. Irã (1.00). Fatores Físicos: Egito viajou 368 km com 6 dias de descanso; Irã viajou 1735 km com 6 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto. 
    *   **Probabilidades:** Vitória Egito: 48.0% | Empate: 29.4% | Vitória Irã: 22.6%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (14.05%), 1 x 0 (10.75%), 0 x 0 (9.93%)
    *   **Nível de Confiança:** Média

*   **Nova Zelândia 0 x 3 Bélgica**
    *   **Estádio:** Vancouver Stadium (Temperatura: 18°C)
    *   **Status:** Preditivo (27/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 13.18 pts) sob o modelo Dixon-Coles recalibrado com Blending de 55% (Duelo Direto Decisivo). Médias de gols projetadas: Nova Zelândia (0.88) vs. Bélgica (3.03). Fatores Físicos: Nova Zelândia viajou 1907 km com 6 dias de descanso; Bélgica viajou 210 km com 6 dias de descanso. 
    *   **Probabilidades:** Vitória Nova Zelândia: 8.8% | Empate: 17.1% | Vitória Bélgica: 74.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (9.73%), 0 x 2 (9.62%), 1 x 3 (8.57%)
    *   **Nível de Confiança:** Baixa

### **Grupo L**

*   **Panamá 0 x 3 Inglaterra**
    *   **Estádio:** New York New Jersey Stadium (Temperatura: 22°C)
    *   **Status:** Preditivo (27/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.55 pts) sob o modelo Dixon-Coles recalibrado com Blending de 40% (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Panamá (0.13) vs. Inglaterra (3.85). Fatores Físicos: Panamá viajou 539 km com 4 dias de descanso; Inglaterra viajou 1754 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Panamá: 5.0% | Empate: 11.4% | Vitória Inglaterra: 83.6%
    *   **Top 3 Placares mais Prováveis:** 0 x 3 (19.15%), 0 x 4 (18.45%), 0 x 2 (14.91%)
    *   **Nível de Confiança:** Alta

*   **Croácia 1 x 0 Gana**
    *   **Estádio:** Philadelphia Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 7.42 pts) sob o modelo Dixon-Coles recalibrado com Blending de 55% (Duelo Direto Decisivo). Médias de gols projetadas: Croácia (0.70) vs. Gana (1.15). Fatores Físicos: Croácia viajou 202 km com 4 dias de descanso; Gana viajou 378 km com 4 dias de descanso. O modelo aplicou o ajuste de Resiliência Defensiva para o bloco baixo deste confronto. 
    *   **Probabilidades:** Vitória Croácia: 34.2% | Empate: 31.7% | Vitória Gana: 34.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 0 (16.00%), 1 x 0 (15.24%), 1 x 1 (13.22%)
    *   **Nível de Confiança:** Alta

### **Grupo K**

*   **Colômbia 1 x 2 Portugal**
    *   **Estádio:** Miami Stadium (Temperatura: 28°C)
    *   **Status:** Preditivo (27/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.40 pts) sob o modelo Dixon-Coles recalibrado com Blending de 40% (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Colômbia (1.19) vs. Portugal (2.55). Fatores Físicos: Colômbia viajou 2432 km com 4 dias de descanso; Portugal viajou 86 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória Colômbia: 21.6% | Empate: 25.8% | Vitória Portugal: 52.5%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (11.01%), 1 x 2 (7.90%), 2 x 2 (7.25%)
    *   **Nível de Confiança:** Média

*   **RD Congo 2 x 0 Uzbequistão**
    *   **Estádio:** Atlanta Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 9.37 pts) sob o modelo Dixon-Coles recalibrado com Blending de 40% (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: RD Congo (2.04) vs. Uzbequistão (0.94). Fatores Físicos: RD Congo viajou 1127 km com 4 dias de descanso; Uzbequistão viajou 2 km com 4 dias de descanso. 
    *   **Probabilidades:** Vitória RD Congo: 50.7% | Empate: 27.0% | Vitória Uzbequistão: 22.3%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.86%), 2 x 0 (8.97%), 2 x 1 (8.44%)
    *   **Nível de Confiança:** Média

### **Grupo J**

*   **Argélia 1 x 2 Áustria**
    *   **Estádio:** Kansas City Stadium (Temperatura: 24°C)
    *   **Status:** Preditivo (27/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 8.04 pts) sob o modelo Dixon-Coles recalibrado com Blending de 55% (Duelo Direto Decisivo). Médias de gols projetadas: Argélia (1.21) vs. Áustria (1.96). Fatores Físicos: Argélia viajou 65 km com 5 dias de descanso; Áustria viajou 2297 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Argélia: 29.5% | Empate: 27.3% | Vitória Áustria: 43.2%
    *   **Top 3 Placares mais Prováveis:** 1 x 1 (12.57%), 2 x 1 (8.22%), 1 x 2 (8.14%)
    *   **Nível de Confiança:** Média

*   **Jordânia 0 x 4 Argentina**
    *   **Estádio:** Dallas Stadium (Temperatura: 26°C)
    *   **Status:** Preditivo (27/Jun) [Modelo Calibrado com 56 Jogos]
    *   **Justificativa:** Palpite otimizado por Valor Esperado (EV: 15.96 pts) sob o modelo Dixon-Coles recalibrado com Blending de 40% (Motivação Assimétrica (Misto de Titulares/Reservas)). Médias de gols projetadas: Jordânia (0.09) vs. Argentina (5.61). Fatores Físicos: Jordânia viajou 2607 km com 5 dias de descanso; Argentina viajou 741 km com 5 dias de descanso. 
    *   **Probabilidades:** Vitória Jordânia: 5.7% | Empate: 11.3% | Vitória Argentina: 83.0%
    *   **Top 3 Placares mais Prováveis:** 0 x 5 (25.39%), 0 x 4 (22.65%), 0 x 3 (16.16%)
    *   **Nível de Confiança:** Alta
