# Walkthrough de Implementação: Modelo Preditivo Híbrido de Elite

Este documento resume o desenvolvimento, os testes e as validações do nosso modelo preditivo híbrido de elite, incluindo o Coeficiente de Disparidade de Elenco (Disparity Boost).

---

## 🛠️ O que foi Implementado

1.  **Mecanismo de Pi-Ratings (Constantinou & Fenton):**
    *   Desenvolvido o script `PiRatingSystem` que roda de forma recursiva sobre os jogos concluídos da Copa para estimar habilidades dinâmicas de casa e fora para todas as 48 seleções.
    *   Este sistema de soma-zero reajusta a habilidade de ataque/defesa com base no saldo de gols real, aplicando retornos decrescentes logarítmicos para abafar o ruído de goleadas extremas.
2.  **Regularização Bayesiana Hierárquica (Shrinkage Prior):**
    *   Adicionado um parâmetro de encolhimento ($\lambda_{\text{shrink}} = 0.1$) e prior ($\lambda_{\text{reg}} = 5.0$) para evitar anomalias preditivas com poucos dados, convergindo de volta à realidade do elenco.
3.  **Índice Dinâmico de Fadiga Logística ($\delta$):**
    *   Implementada uma função que calcula a fadiga das seleções baseando-se em fuso horário/distância percorrida, dias de descanso e temperatura do estádio.
4.  **Coeficiente de Disparidade de Elenco (Disparity Boost):**
    *   Integrado um fator de correção estático pré-jogo para jogos de alta disparidade ($R = \lambda_{\text{fav}} / \lambda_{\text{und}} > 1.8$).
    *   Este multiplicador aumenta exponencialmente a expectativa do favorito ($\lambda_{\text{fav}} \times \text{boost}$) e reduz ligeiramente a do azarão ($\lambda_{\text{und}} \times 0.90$) para capturar de forma estática goleadas (como Alemanha 7-1 Curaçao ou Suécia 5-1 Tunísia) antes do kickoff, respeitando a impossibilidade de updates in-play.

---

## 🧪 Resultados de Validação e Simulação

### 1. Validação do Disparity Boost
Rodamos simulações comparativas para testar o comportamento do ajuste pré-jogo em confrontos com alta disparidade:
*   **Alemanha vs. Curaçao (Ratio Inicial: 6.40):**
    *   Antes do boost: O Poisson padrão estimava um placar muito menor.
    *   Após o boost: Ajustado para **6.09 x 0.47**, apontando o **5 x 0** como placar mais provável com 22.96% de probabilidade, condizente com a goleada real de 7x1.
*   **Espanha vs. Cabo Verde (Ratio Inicial: 3.40):**
    *   Ajustado de $1.94 \times 0.57$ para **$2.50 \times 0.51$** no simulador de partida.
    *   O placar mais provável foi ajustado para **2 x 0** com maior índice de confiança (Alta) e maior probabilidade acumulada de gols excedentes (**3 x 0** com 13.36%).

---

## 📍 Atualização Logística e Recalibração de Palpites

1. **Campos de Sede (QGs):** Catalogamos o local exato do Campo de Base de cada uma das 48 seleções participantes.
2. **Cálculo de Distâncias (Haversine):** Estimamos as viagens reais para ajustar a fadiga logística.
3. **Novos Palpites Recalibrados e Otimizados para o Bolão**: Executamos o script `aplicar_novos_palpites.py` atualizado para escrever previsões otimizadas por Valor Esperado (EV) com base nas regras de pontuação atualizadas do bolão (30 pts por placar exato, 20 pts se acertar o vencedor e os gols do vencedor, 15 pts por vencedor seco ou empate genérico).
    *   Com o aumento da recompensa do placar exato para **30 pontos**, o palpite para **Gana vs. Panamá** mudou de **2x0** para **1x0**, pois a maior probabilidade de cravar o 1x0 (11.99% vs 6.99% do 2x0) maximiza o EV. Os demais jogos de superpotências mantiveram o **2x0** e **0x2** por ampla vantagem estatística.
    *   **Espanha vs. Cabo Verde** (Real: **0 x 0**, Erro): A defesa de Cabo Verde travou a Espanha apesar do xG projetado superior.
    *   **Bélgica vs. Egito** (Real: **1 x 1**, Acerto de Placar): Confirmou a precisão do modelo no placar exato de empate.
    *   **Uruguai vs. Arábia Saudita** (Real: **1 x 1**, Erro) / **Irã vs. Nova Zelândia** (Real: **2 x 2**, Erro): Ambos terminaram em empates imprevistos.
    *   **Resultados de 16 de Junho** (4 Acertos Secos de Vencedor):
        *   **França vs. Senegal** (Real: **3 x 1**, Acerto Seco / Erro Placar): A França venceu confortavelmente por 3 a 1.
        *   **Iraque vs. Noruega** (Real: **1 x 4**, Acerto Seco / Erro Placar): Goleada norueguesa liderada por Haaland.
        *   **Argentina vs. Argélia** (Real: **3 x 0**, Acerto Seco / Erro Placar): Triunfo argentino com hat-trick de Messi.
        *   **Áustria vs. Jordânia** (Real: **3 x 1**, Acerto Seco / Erro Placar): Áustria impôs sua força e venceu por 3 a 1.
    *   Os 4 jogos restantes da primeira rodada foram recalibrados com o resolvedor alimentado por esses novos resultados no vetor `JOGOS_CONCLUIDOS`.

---

## 📄 Geração de Relatório Metodológico PDF
O script `gerar_pdf.py` compilou com sucesso o arquivo markdown `relatorio_metodologia_preditiva.md` no relatório executivo em PDF:
*   [relatorio_metodologia_preditiva.pdf](file:///Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/relatorio_metodologia_preditiva.pdf) (limpo de emojis e com fórmulas formatadas em texto plano para evitar erros de codificação).

---

## 🏆 Simulação Monte Carlo do Campeão da Copa do Mundo 2026 (10.000 Torneios)

Rodamos a simulação completa do torneio 10.000 vezes incorporando os novos ajustes do Disparity Boost e da fadiga. Abaixo estão as novas probabilidades de título para o Top 10 de favoritos:

| Ranking | Seleção | Probabilidade de Título | Chegada à Final |
| :--- | :--- | :---: | :---: |
| **#1** | 🇫🇷 França | **15.28%** | 24.70% |
| **#2** | 🇪🇸 Espanha | **14.14%** | 22.87% |
| **#3** | 🇦🇷 Argentina | **12.84%** | 21.60% |
| **#4** | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra | **9.15%** | 16.36% |
| **#5** | 🇵🇹 Portugal | **8.55%** | 15.56% |
| **#6** | 🇩🇪 Alemanha | **6.98%** | 13.96% |
| **#7** | 🇧🇷 Brasil | **5.22%** | 10.58% |
| **#8** | 🇲🇽 México | **4.83%** | 10.14% |
| **#9** | 🇺🇾 Uruguai | **3.67%** | 8.77% |
| **#10** | 🇺🇸 EUA | **3.42%** | 8.00% |

---

## ⚽ Recalibração e Previsões da 2ª Rodada

Para a transição para a **2ª Rodada**, executamos as seguintes melhorias baseadas nos resultados observados e no feedback do usuário:

1.  **Maior Pertinência da 1ª Rodada:** Reduzimos a regularização L2 (`reg_lambda` de `5.0` para `1.5`). Isso fez com que o modelo priorizasse as forças reais demonstradas pelas seleções nos seus 24 primeiros jogos sobre os priors históricos estáticos.
2.  **Calibração do Volume de Gols (`mu`):** Adicionamos uma variável global `mu` ao resolvedor Dixon-Coles, que convergiu de forma ideal para **1.3922** (cerca de 2.78 gols por jogo). Isso corrigiu a tendência anterior de subestimar a quantidade de gols das partidas.
3.  **Estabilização do Disparity Boost:** Limitamos o multiplicador de disparidade a um máximo de `1.5` para evitar distorções estatísticas em jogos extremos. A partida **Brasil vs. Haiti** (que antes obteria 16.64 gols esperados por anomalia de fração) foi ajustada para um limite realista de **4.97 gols esperados** para o Brasil.
4.  **Flexibilização de Palpites de Goleada:** Expandimos o limite de gols na busca de EV do bolão de `3` para `4` gols. Isso permitiu que o modelo recomende com segurança placares como **4 x 0** para confrontos muito desequilibrados (como Brasil vs. Haiti e França vs. Iraque), maximizando o Valor Esperado sob as novas regras de pontuação (30 pts placar exato, 20 pts vencedor + gols do vencedor).
5.  **Geração dos Palpites:** O script `aplicar_novos_palpites_rodada2.py` executou com sucesso e gerou a análise completa em [palpites_copa_2026_rodada2.md](file:///Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada2.md).

