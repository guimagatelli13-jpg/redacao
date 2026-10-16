# Registro acumulado do modelo

Documento vivo. Atualize a cada nova avaliação ou experimento; não recomece do zero.
- Detalhes da análise inicial: `relatorios/001-analise-inicial.md`.
- Dados brutos: `dados/avaliacoes.csv`.

Legenda de status das hipóteses:
- **ativa**: compatível e não testada;
- **apoiada**: acertou uma previsão em dado novo;
- **enfraquecida**: conflita com dados, mas não é impossível;
- **refutada**: incompatível com os dados;
- **confirmada**: documentada, ou apoiada por várias previsões independentes.

## 1. Avaliações

| ID | Tema | G | A | T | E | Online | Final | Tipo | Relatório |
|---|---|---|---|---|---|---|---|---|---|
| 001 | Descarte correto do lixo | 9,90 | 3,00 | 7,10 | 4,00 | 6,60 | 0,00 | linha de base | `relatorios/001-analise-inicial.md` |

## 2. Dados de contexto informados depois da análise inicial

| Data | Informação | Fonte | Efeito no modelo |
|---|---|---|---|
| 2026-10-16 | limite máximo de 2.000 caracteres | informado pelo usuário (sem documento) | H-A4 enfraquecida; P-MAX não explica o zero; X3, X4, X5 e X8 refeitos para caber no limite |

## 3. Hipóteses

### Nota online (agregação)

| ID | Hipótese | Classe | Status | Evidência | Teste |
|---|---|---|---|---|---|
| M1 | trunc₀,₁((G+A+T)/3) | H | ativa (melhor candidato) | reproduz 001 | X0, X1, X2, novas avaliações |
| M1b | média com arredondamento sobre valores internos ocultos | H | ativa | reproduz 001 se a soma interna ∈ [19,85; 19,95) | casos com fração ,x5–,x9 |
| M1c | média das notas exibidas com arredondamento a 0,1 ou 0,01 | — | **refutada** | dá 6,7 / 6,67 | — |
| M2 | pesos desiguais (faixa wG 0–54%, wA 10–48%, wT 0–90%) | H | ativa | reproduz 001 | perfis variados |
| M3 | 0,29G + 0,32A + 0,39T, exato | H | ativa (implausível) | reproduz 001 | qualquer avaliação nova |
| M4 | (G+A+T − 0,05E)/3 | H | ativa (ad hoc) | reproduz 001 | X1 |
| M5 | média incluindo E | — | **refutada** | dá 6,00 | — |
| M6 | média com T invertido | — | **refutada** | dá 5,27 | — |
| M7 | geométrica / harmônica / mediana / mínimo | — | **refutadas** | dão 5,95 / 5,22 / 7,10 / 3,00 | — |
| M8 | nota holística do LLM, sem fórmula | H | ativa | — | X0; coincidência com M1 em n avaliações |
| R-wA | wA > 0 em qualquer média ponderada | C (condicional) | — | 6,6 < min(G, T) | — |

### Critérios

| ID | Hipótese | Classe | Status | Teste |
|---|---|---|---|---|
| G-esc | G em 0–10, passo 0,1 | IF | ativa | novas avaliações |
| MG1 | G = 10 − 0,025E | H | ativa | X1a/X1b |
| MG2 | G = arred₀,₁(10(1 − E/palavras)) | H | ativa | X1a/X1b |
| MG3 | G = 10 − 0,1E | — | **refutada** (dá 9,6) | — |
| E-cont | E é uma contagem de apontamentos | H | ativa | X1, X2 |
| E-fp | os 4 apontamentos são falsos positivos nos 5 trechos listados | H | ativa | X2 |
| T-ori | T: maior = mais aderente | IF | ativa | X6, X7 |
| T-tese | T sobe quando a tese nomeia o recorte | H | ativa | X6 |
| T-prop | T acompanha a proporção do texto dedicada ao recorte | H | ativa | X4, X5, X7 |
| H-A1 | A = cobertura das perguntas (0–10) | H | **enfraquecida** | X7 |
| H-A1' | A = contagem de perguntas (0–4) | H | **enfraquecida** | — |
| H-A2 | A = profundidade de desenvolvimento | H | ativa | X4 vs. X5 |
| H-A3 | A = fatos e repertório | H | ativa | X3 vs. X5 |
| H-A4 | A = extensão | H | **enfraquecida**: o texto usou 92% do máximo de 2.000 caracteres; se A fosse proporcional à fração usada, valeria ~9, e não 3 | X3, X4, X5 vs. base; X7 |
| H-A5 | A = gabarito de tópicos do tema | H | ativa | novos temas |
| H-A6 | A = diversidade de dimensões | H | **enfraquecida** | — |
| H-A7 | A em níveis discretos | H | ativa | novas avaliações (A é sempre inteiro?) |
| H-A8 | A instável | H | ativa | X0 |
| A-corr | a plataforma é mais exigente que a régua do ENEM na Abrangência (original: régua 6, observado 3,0): deslocamento de −3 ou razão de 0,5 | H | ativa | X8, X9 |

### Nota Final

| ID | Hipótese | Status |
|---|---|---|
| F≠O | Nota Final e nota online são grandezas distintas | **confirmada** (6,6 ≠ 0 na mesma redação) |
| P-ID | Nota Final = nota online | **refutada** |
| P-Z0 / P-FT / P-N5 / P-N6 | zera se algum critério = 0 / se T = 0 / se nota online < 5 / se nota online < 6, como explicação suficiente | **refutadas como explicação única** |
| P-N7 | zera se nota online < 7 | ativa |
| P-A5 | zera se A < 5 (ou algum critério < 5) | ativa |
| P-OUT | causa externa às notas (status do processo, integridade, etapa pendente) | ativa |
| P-EXT | zera por extensão abaixo do mínimo | muito improvável (1.564 a 1.844 caracteres) |
| P-MAX | zera por exceder o máximo de 2.000 caracteres | **não explica**: 1.844 caracteres, contando as quebras |

## 4. Previsões registradas e resultados

As previsões numéricas estão em `experimentos/protocolo.md`. Registre aqui cada comparação.

| Data | Experimento | Previsão (modelo) | Observado | Acertou? | Consequência |
|---|---|---|---|---|---|
| | | | | | |

## 5. Questões em aberto

1. O que a Abrangência mede, e se o 3,0 é estável.
2. Por que a Nota Final é 0,00: regra de nota mínima, campo de outro nível ou causa externa.
3. Se o "Apontamento de erro gramatical" é uma contagem e se alimenta a Gramática.
4. Truncamento ou arredondamento; precisão interna das notas.
5. Se o avaliador é determinístico.
6. Se o tema muda o comportamento de A (gabarito por tema). A série 002 é o primeiro teste.

## 6. Histórico de alterações

| Versão | Data | Mudança |
|---|---|---|
| v0.1 | 2026-10-16 | modelo inicial a partir da avaliação 001; rubrica parcial em `relatorios/001-analise-inicial.md`, §9 |
| v0.2 | 2026-10-16 | limite de 2.000 caracteres incorporado: H-A4 enfraquecida, P-MAX acrescentada, X3–X5 e X8 refeitos dentro do limite |
| v0.3 | 2026-10-16 | rubrica híbrida com os critérios do ENEM (`modelo/rubrica-hibrida-enem.md`); hipótese A-corr; X9 escrito para a rubrica híbrida |
| v0.4 | 2026-10-16 | série 002 (tema "Consumo e consumismo", simulado): texto C1 escrito para a rubrica híbrida e previsões em `experimentos/protocolo-002-consumo.md`; primeiro teste da rubrica fora do tema de origem |
| v0.5 | 2026-10-16 | série 003 (tema "Mudanças climáticas", simulado): texto M1 e previsões em `experimentos/protocolo-003-clima.md`; testa se tratar causas e soluções como subordinadas ao recorte é lido como aderência ou como cobertura incompleta |
