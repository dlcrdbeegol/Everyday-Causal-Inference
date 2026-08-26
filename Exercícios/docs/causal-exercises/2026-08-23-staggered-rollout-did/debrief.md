# Debrief — QuickBite Kiosk Rollout (DGP-04)

## Método usado pelo aluno
Callaway-Sant'Anna staggered DiD (`diff_diff.CallawaySantAnna`), `control_group="never_treated"`.
Escolha correta desde o início — evitou a armadilha do TWFE ingênuo.

## Estimativas do aluno vs. efeito real

| | Estimado | Real (média pós-tratamento) |
|---|---|---|
| Coorte mês 7 (early) | ~215 | 217.0 |
| Coorte mês 13 (mid) | não reportado | 158.2 |
| Coorte mês 19 (late) | ~100 | 102.5 |
| ATT geral ponderado | 177.95 [167.6, 188.6] | ~178 |

Gap: ruído amostral. Método e suposições corretamente validados.

## Pontos fortes da análise
- Verificou pré-tendências via event study (`plot_event_study`) — corretamente concluiu que
  não há diferença pré-tratamento relevante.
- Identificou heterogeneidade por coorte sem que isso fosse pedido explicitamente
  (`res.aggregate("group")`), percebendo que o efeito diminui para coortes tardias.
- Recomendação final corretamente condicionada a custo de adoção (ROI), não apenas
  significância estatística — trata a expansão para as 50 lojas restantes como uma decisão
  de breakeven, não como certeza de replicar o ATT médio.

## Lição de causal inference reforçada
Rollouts escalonados com efeitos heterogêneos/crescentes ao longo do tempo exigem
estimador robusto (Callaway-Sant'Anna / Sun-Abraham). TWFE ingênuo (`treated*post`)
usaria coortes tratadas cedo como controle implícito para coortes tratadas tarde,
introduzindo viés (Goodman-Bacon decomposition).

## Score
Excelente. Método, diagnóstico de suposição e leitura de heterogeneidade — todos corretos.
