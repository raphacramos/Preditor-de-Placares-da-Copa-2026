# Plano de Implementação: Recalibração para a 2ª Rodada da Copa 2026 (Ajuste de Gols e Maior Posição de Rodada 1)

Este plano descreve o ajuste e sintonização do modelo preditivo para a **2ª Rodada** da Copa do Mundo FIFA 2026. A partir do feedback do usuário de que o modelo subestimou a quantidade de gols na primeira rodada, e da necessidade de dar maior peso ("pertinência") aos resultados reais da primeira rodada (24 jogos concluídos), propomos:

1.  **Redução de L2 Regularization (`reg_lambda`):** De `5.0` para `1.5`, permitindo que o modelo responda de forma muito mais dinâmica ao desempenho real e atual das seleções na 1ª rodada.
2.  **Inclusão do Parâmetro de Volume Global de Gols (`mu`):** Adicionaremos um multiplicador de escala global para os gols esperados no resolvedor Dixon-Coles, otimizando-o com base nos 75 gols em 24 jogos da 1ª rodada (média de 3.125 gols por jogo).
3.  **Mapeamento de Rest Day Dinâmico e Novas Sedes da Rodada 2:** Mapear os dias de descanso das 48 seleções com base em suas datas de jogo na 1ª rodada e adicionar as coordenadas das novas sedes (Vancouver, Guadalajara, San Francisco Bay Area).
4.  **Geração do Relatório da 2ª Rodada:** Criar o novo documento `palpites_copa_2026_rodada2.md` com os novos palpites otimizados por Valor Esperado (EV) sob as regras do bolão.

---

## Proposed Changes

### Modelo Preditivo e Componentes de Simulação

#### [MODIFY] [modelo_avancado_copa.py](file:///Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/scratch/modelo_avancado_copa.py)
*   Modificar a classe `DixonColesModel`:
    *   No construtor, inicializar `self.mu = 1.35` (e aceitar `reg_lambda=1.5` como padrão).
    *   No método `fit`, expandir o vetor de parâmetros `initial_params` para tamanho `2 * self.num_teams + 3` para incluir `mu`.
    *   Em `negative_log_likelihood`:
        *   Resgatar `mu` como `params[-1]`.
        *   Multiplicar `lambda_a` e `lambda_b` pelo fator `mu`.
        *   Adicionar restrição de média igual a 1.0 para os coeficientes de defesa (`betas`) no cálculo do `constraint_penalty`, garantindo a identificação perfeita do modelo e que `mu` represente a média global de gols de forma limpa.
    *   Atualizar o método `predict_probabilities` para multiplicar os gols esperados pelo valor ajustado de `self.mu`.

#### [MODIFY] [recalibrador_placares.py](file:///Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/scratch/recalibrador_placares.py)
*   Ajustar a função `recalibrar_confronto` para multiplicar os lambdas por `model.mu` para consistência analítica total.

#### [MODIFY] [simulador_campeao_copa.py](file:///Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/scratch/simulador_campeao_copa.py)
*   Atualizar o construtor `DixonColesModel` para usar `reg_lambda=1.5`.
*   Ajustar a função `simular_partida` para multiplicar os lambdas por `model.mu` para que a simulação de gols reflita a tendência de alta quantidade de gols do torneio real.

---

### Pipeline e Relatório da 2ª Rodada

#### [NEW] [aplicar_novos_palpites_rodada2.py](file:///Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/scratch/aplicar_novos_palpites_rodada2.py)
*   Criar o script wrapper específico para a 2ª rodada:
    *   Inserir o dicionário `ULTIMO_JOGO` mapeando a data da 1ª rodada para cada equipe.
    *   Definir os 24 confrontos da 2ª rodada com suas datas de jogo (de 18 a 23 de junho), estádios e temperaturas estimadas.
    *   Adicionar as coordenadas ausentes em `ESTADIOS` (Vancouver, Guadalajara, San Francisco).
    *   Calcular distâncias e dias de descanso (`dia_jogo - ULTIMO_JOGO[time]`) dinamicamente.
    *   Treinar o modelo sintonizado com `reg_lambda=1.5` sobre `JOGOS_CONCLUIDOS`.
    *   Calcular previsões otimizadas por EV do bolão (30 pts placar exato, 20 pts vencedor + gol do vencedor).
    *   Escrever os resultados em um novo arquivo Markdown (`palpites_copa_2026_rodada2.md`).

#### [NEW] [palpites_copa_2026_rodada2.md](file:///Users/raphaelramos/.gemini/antigravity/brain/a77bb963-70eb-4548-8861-b9634d4cd31e/palpites_copa_2026_rodada2.md)
*   Relatório estruturado com a tabela de palpites sugeridos para a 2ª rodada, análise individual por partida e a justificativa metodológica baseada na fadiga, distância de viagem e no ajuste global de gols.

---

## Verification Plan

### Automated Tests
*   Rodar `aplicar_novos_palpites_rodada2.py` e validar que as previsões foram calculadas sem erros e salvas em `palpites_copa_2026_rodada2.md`.
*   Validar que o valor ótimo de `mu` obtido após o `fit` reflete uma taxa de gols esperados mais alta (espera-se `mu` > 1.30, indicando maior volume de gols por jogo).

### Manual Verification
*   Verificar se os palpites sugeridos para seleções muito ofensivas (ex: Alemanha vs. Costa do Marfim, Brasil vs. Haiti) refletem placares mais elásticos (ex: 2-0, 3-0 ou 3-1 em vez de 1-0 ou 2-0 conservadores).
*   Garantir que a tabela rápida e os detalhes jogo-a-jogo em `palpites_copa_2026_rodada2.md` estão formatados corretamente.
