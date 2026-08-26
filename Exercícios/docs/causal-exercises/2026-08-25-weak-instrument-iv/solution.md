# Solução — Vidalife Balance Encouragement Email (DGP-06, Weak Instrument)

> ⚠️ **NÃO ABRIR até terminar sua análise.** Contém método e efeito verdadeiro.

## Método correto

**Instrumental Variables (2SLS)**, com diagnóstico de instrumento fraco.

- Instrumento (`received_email`): atribuído aleatoriamente (Bernoulli 0.5), então é
  exógeno por construção.
- Tratamento endógeno (`enrolled_program`): depende do instrumento **e** de uma
  motivação de saúde não observada (`U`), que também afeta o desfecho diretamente
  — por isso é endógeno e não pode ser usado diretamente numa regressão OLS.
- Desfecho (`annual_spending`).

## Efeito verdadeiro

**LATE = -10.0** (mil dólares de redução de gasto médico, entre os *compliers*
— membros que se matriculam no programa *porque* receberam o e-mail, mas não se
matriculariam sem ele).

## A complicação: instrumento fraco

O coeficiente de primeiro estágio é pequeno (`0.3` no índice logístico), gerando
um **F-estatístico de primeiro estágio em torno de 5** — abaixo do limiar
convencional de 10. Isso significa:

- 2SLS fica **viesado na direção do OLS** (que por sua vez é viesado pela
  confundidora `U`).
- Os intervalos de confiança do 2SLS convencional são **não confiáveis** sob
  instrumento fraco — testes robustos a instrumento fraco (Anderson-Rubin) são
  mais defensáveis aqui.
- A estimativa pontual pode variar bastante entre replicações/amostras.

## O que uma análise ingênua faria de errado

- **Confiar apenas no p-valor/significância do primeiro estágio** sem checar o
  F-estatístico robusto — um coeficiente "significante" não implica instrumento
  forte.
- **Reportar o 2SLS como se fosse tão preciso quanto o first stage sugere**,
  ignorando que o IC do 2SLS deveria ser mais largo / usar inferência robusta a
  instrumento fraco.
- **Confundir instrumento fraco com instrumento inválido** — aqui a exclusion
  restriction e a independência SE MANTÊM (o e-mail é aleatório e não afeta gasto
  além de via matrícula). O problema é só de força estatística, não de validade.

## Diagnósticos que teriam pegado

1. **F-estatístico robusto de primeiro estágio** (`linearmodels` reporta isso
   automaticamente, ou `statsmodels` com `HC1`) — deveria aparecer bem abaixo de 10.
2. **Comparação OLS vs. 2SLS**: se os dois estimadores derem valores parecidos e
   ambos distantes do LATE real, é sinal de viés de instrumento fraco puxando o
   2SLS para o OLS.
3. **Anderson-Rubin confidence set**: dá um IC válido mesmo com instrumento fraco,
   ao contrário do IC padrão do 2SLS.

## Sobre o LATE

O efeito de -10 vale **apenas para os compliers** (quem se matricula por causa do
e-mail, não por causa própria). Não é o ATE da população inteira — isso é uma
limitação de interpretação que o aluno deve mencionar, independentemente da força
do instrumento.
