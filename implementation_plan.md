# Plano de Implementação: Otimização Preditiva para a 3ª Rodada da Copa 2026

Este plano descreve a análise dos erros ocorridos na 2ª rodada e os ajustes técnicos propostos para a **3ª Rodada** da fase de grupos, com foco em aumentar a precisão dos palpites do bolão sob as dinâmicas de fim de grupo (poupa de titulares, motivação assimétrica e blocos defensivos baixos).

---

## 🔍 Análise Retrospectiva da 2ª Rodada

Na 2ª rodada, obtivemos uma excelente performance geral no bolão:
- **Pontuação:** **320 pontos** acumulados em 24 jogos (média de **13.33 pts por jogo**).
- **Aproveitamento de Desfecho:** **75%** (18 acertos seco/placar em 24 confrontos).
- **Acertos de Placar Exato:** 3 jogos (Alemanha 2x1 Costa do Marfim, Jordânia 1x2 Argélia, Panamá 0x2 Croácia).

### O que deu errado (Análise dos 6 Erros):
1. **Tchéquia 1 x 1 África do Sul** (Palpite: 2x0) - *Empate imprevisto*
2. **Turquia 0 x 1 Paraguai** (Palpite: 2x1) - *Derrota do favorito*
3. **Equador 0 x 0 Curaçao** (Palpite: 2x0) - *Empate sem gols*
4. **Bélgica 0 x 0 Irã** (Palpite: 2x1) - *Empate sem gols*
5. **Uruguai 2 x 2 Cabo Verde** (Palpite: 1x0) - *Empate com muitos gols*
6. **Inglaterra 0 x 0 Gana** (Palpite: 3x1) - *Empate sem gols*

**Padrão Identificado:** 4 dos 6 erros foram empates de "underdogs" defensivos que seguraram favoritos em blocos baixos (África do Sul, Curaçao, Irã, Gana), muitas vezes terminando em 0x0. O modelo superestimou a capacidade ofensiva do favorito ou a falta de resiliência dos azarões em duelos truncados.

---

## 🛠️ Ajustes Propostos para a 3ª Rodada

Para minimizar erros e capitalizar nas dinâmicas específicas da rodada final dos grupos, implementaremos as seguintes melhorias:

### 1. Pesos de Mesclagem de Odds Dinâmicos (`w_modelo`)
Em rodadas finais, a motivação e a escalação de times poupados são fatores cruciais que as estatísticas passadas não capturam sozinhas. As odds de mercado reais incorporam essas informações instantaneamente.
- **Duelos de Alta Disparidade e Motivação Assimétrica (Ex: Time qualificado vs. Time desesperado):** Reduziremos `w_modelo` para **0.40** (60% de peso para odds reais), permitindo que a cotação do mercado guie as tendências de poupa de elenco.
- **Duelos de Ambos Qualificados (Ex: França vs. Noruega):** Ajustaremos `w_modelo` para **0.45** (55% de peso para odds).
- **Duelos Diretos de Alta Tensão (Ambos buscando classificação):** Manteremos `w_modelo` em **0.55** (45% de peso para odds), onde a força estatística pura do modelo Dixon-Coles é mais relevante.

### 2. Ajuste de Resiliência de Bloco Baixo
Ajustaremos o **Disparity Boost** (fator de goleada) para jogos da 3ª rodada:
- Limitaremos o multiplicador máximo de disparidade a **1.30** (em vez de `1.50`), já que seleções qualificadas jogam de forma mais conservadora e seleções fracas se fecham completamente no fim.
- Aplicaremos um ajuste defensivo de **5% de redução no parâmetro beta** para underdogs notórios por retrancas eficientes (Irã, Curaçao, Gana, Cabo Verde, África do Sul).

---

## Proposed Changes

### Componente de Dados e Modelo

#### [MODIFY] [modelo_avancado_copa.py](file:///Users/raphaelramos/Documents/antigravity/peaceful-pasteur/repo-import/src/modelo_avancado_copa.py)
*   Integrar as 8 partidas restantes da 2ª rodada no banco de dados `JOGOS_CONCLUIDOS`.
*   Incrementar o parâmetro `dias_atras` de todas as partidas anteriores em `+2` dias para refletir o tempo real em relação ao dia 24/Jun.

#### [NEW] [aplicar_novos_palpites_rodada3.py](file:///Users/raphaelramos/Documents/antigravity/peaceful-pasteur/repo-import/src/aplicar_novos_palpites_rodada3.py)
*   Criar o script executor para a 3ª rodada.
*   Catalogar as odds de mercado reais e estimadas para os 24 confrontos finais.
*   Definir os confrontos com suas sedes, datas e temperaturas médias de 24 a 27 de Junho.
*   Implementar a classificação dinâmica e a lógica de pesos `w_modelo` dinâmicos.
*   Gerar o novo relatório em [palpites_copa_2026_rodada3.md](file:///Users/raphaelramos/Documents/antigravity/peaceful-pasteur/repo-import/relatorios/palpites_copa_2026_rodada3.md).

---

## Verification Plan

### Automated Tests
*   Executar `aplicar_novos_palpites_rodada3.py` e validar que as previsões foram computadas sem erros e gravadas no arquivo markdown.
*   Validar que o resolvedor Dixon-Coles ajustou os parâmetros de gols esperados utilizando o banco completo de 48 jogos da fase de grupos.

### Manual Verification
*   Verificar se jogos como **Tchéquia vs. México** ou **Equador vs. Alemanha** refletem o peso das odds reais do mercado em decorrência da classificação prévia do México e da Alemanha.
*   Garantir a consistência visual e o cálculo correto do EV da tabela do bolão.
