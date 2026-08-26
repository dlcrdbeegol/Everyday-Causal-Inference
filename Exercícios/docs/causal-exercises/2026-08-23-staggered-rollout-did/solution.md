# Solução — Staggered Policy Rollout (DGP-04)

> ⚠️ **NÃO ABRIR até terminar sua análise.** Contém método e efeitos verdadeiros.

## Método correto

**Staggered Difference-in-Differences** com estimador robusto a heterogeneidade
temporal — Callaway & Sant'Anna (2021) ou Sun & Abraham (2020). TWFE ingênuo com
`treated * post` é enviesado quando efeitos variam entre coortes, porque unidades
tratadas cedo entram como "controle implícito" para tratadas tarde.

Em Python, o pacote canônico é `diff-diff` (import: `diff_diff`):

```python
from diff_diff import CallawaySantAnna
# gname = cohort_month (0 = never-treated), tname = month
```

Em R: `did::att_gt` com `control_group = "nevertreated"`.

## Efeitos verdadeiros

O ATT depende da coorte e cresce com o tempo desde o tratamento (`month - g`):

| Coorte | Início | ATT base | Ramp por período |
|--------|--------|----------|------------------|
| 1      | month 7  | **200** | +2 por mês       |
| 2      | month 13 | **150** | +1.5 por mês     |
| 3      | month 19 | **100** | +1 por mês       |
| —      | never    | 0       | —                |

Portanto o "ATT global" ponderado ficará em torno de **~170–180** dependendo
dos pesos, mas o número certo de reportar é a **decomposição por coorte** ou o
**event study** (dinâmica pós-tratamento).

## O que uma análise ingênua faria de errado

- **OLS `orders ~ treated * post`** ignora a estrutura escalonada; combina três
  efeitos diferentes num único coeficiente e pode ainda usar tratadas cedo como
  controle para tratadas tarde → viés de agregação de Goodman-Bacon.
- **TWFE com dummy única de tratamento** sofre do mesmo problema quando os
  efeitos crescem com o tempo (dynamic effects).

## Diagnósticos que teriam pegado

1. **Event study pré-tratamento** (leads negativos): devem ser ~0 e não são
   estatisticamente diferentes de zero — as tendências paralelas se sustentam
   nesta DGP.
2. **Comparar TWFE simples vs. Callaway-Sant'Anna**: a diferença exposição a
   viés de heterogeneidade.
3. **Bacon decomposition** (`bacondecomp` em R, ou manual em Python): quantifica
   quanto do coeficiente TWFE vem de comparações "tratada tarde vs. tratada
   cedo" (as problemáticas).

## Sobre a lesson do plugin

Ver `references/lessons.md` (linhas 82–107): em Python use
`diff_diff.CallawaySantAnna` com `control_group="never_treated"` e
`base_period="universal"`. Não roll-your-own TWFE por coorte — é a fonte do
viés que este exercício testa detectar.
