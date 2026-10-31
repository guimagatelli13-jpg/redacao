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
| 002 | Descarte correto do lixo (texto B) | 9,70 | 3,20 | 8,70 | 7,00 | 6,90 | 0,00 | avaliação externa | `relatorios/002-segunda-avaliacao.md` |
| 003 | Consumo e consumismo (texto A) | 9,60 | 2,40 | 8,50 | 0,00 | 6,50 | 0,00 | avaliação externa | `relatorios/003-terceira-avaliacao.md` |
| 004 | Consumo e consumismo (texto B) | 10,00 | 2,40 | 7,40 | 1,00 | 6,40 | 0,00 | avaliação externa | `relatorios/004-quarta-avaliacao.md` |
| 005 | Descarte correto do lixo (texto C) | 9,90 | 2,80 | 9,00 | 2,00 | 6,90 | 0,00 | avaliação externa; teste fora da amostra do modelo v0.18 | `relatorios/005-quinta-avaliacao.md` |

## 2. Dados de contexto informados depois da análise inicial

| Data | Informação | Fonte | Efeito no modelo |
|---|---|---|---|
| 2026-10-16 | limite máximo de 2.000 caracteres | informado pelo usuário (sem documento) | H-A4 enfraquecida; P-MAX não explica o zero; X3, X4, X5 e X8 refeitos para caber no limite |
| 2026-10-27 | instituição: Faculdades Pequeno Príncipe (FPP); a "Nota Final" tem a descrição "Exibe a nota final calculada para a inscrição" | tela da plataforma | a Nota Final é um campo da inscrição; P-OUT reforçada |
| 2026-10-27 | o simulador usa o mesmo sistema da prova oficial, e o tema é sorteado entre lixo, consumismo e clima; o tema real da prova será outro | informado pelo usuário | os envios no simulador são experimentos válidos para o sistema real; série 005 |
| 2026-10-30 | a avaliação 005 tem 2.736 caracteres e foi avaliada normalmente | `avaliacoes/005-descarte-lixo-c/` (a confirmar se o texto é exatamente o enviado) | o limite de 2.000 pode não ser bloqueado pela plataforma; a Nota Final continua 0,00, como nas quatro anteriores, então P-MAX segue sem explicar o zero |
| 2026-10-27 | orientações da professora de redação: uma pergunta por parágrafo, todas pertinentes ao recorte; dado tem de provar a afirmação (endividamento ≠ consumismo); nada de repertório de bolso; nenhuma ponta solta | `fontes/orientacoes-professora.md` (fonte humana, não documentação da plataforma) | convergem com T-lex, H-A9 e o método de amarração; a crítica ao endividamento atinge a 004 e o texto C1; o repertório de bolso atinge C1, X9, M2, M3 e M4 |
| 2026-10-27 | as avaliações 001 a 004 foram **provas reais**; na 004 o título foi digitado no campo da redação | informado pelo usuário | o 0,00 da Nota Final aparece em quatro provas reais com nota online de 6,4 a 6,9, acima do corte de 6,0 publicado no blog da FPP; a regra documentada não explica o zero |
| 2026-10-27 | plataforma da CRM Educacional (domínio na barra de endereço). Segundo a documentação: abrangência = "se o candidato entendeu e desenvolveu bem o tema proposto… de maneira completa e coerente"; gramática = "correção ortográfica e gramatical"; parâmetros ajustáveis pela instituição | tela da avaliação 004; artigo de suporte da CRM Educacional (trechos de busca) | os pesos 0,4/0,4/0,2 provavelmente são configuração da FPP; a gramática inclui ortografia |
| 2026-10-27 | a plataforma conta todos os caracteres, inclusive espaços e quebras: o contador mostrou 1.680 para 1.674 caracteres de texto mais 3 linhas em branco | tela de redação (avaliação 003) | confirma a transcrição; as quebras de parágrafo com linha em branco contam 2 |
| 2026-10-27 | redação online vale até 10; classificação com 6,0 ou mais, sem zerar nenhum critério; de 1.200 a 2.000 caracteres; resultado em até 48 horas úteis | blog oficial da FPP (Verão 2027) e Edital FPP 016 (Verão 2026), lidos por trechos de busca porque o domínio está bloqueado neste ambiente | P-N7 contradiz o documento; as notas online 6,6 e 6,9 classificariam; o zero não decorre das regras documentadas |

## 3. Hipóteses

### Nota online (agregação)

| ID | Hipótese | Classe | Status | Evidência | Teste |
|---|---|---|---|---|---|
| M1 | trunc₀,₁((G+A+T)/3) | — | **refutada** pela 002 (dá 7,2; observado 6,9), inclusive com precisão oculta | reproduzia 001 | — |
| M1b | média com arredondamento sobre valores internos ocultos | — | **refutada** pela 002 | — | — |
| M1c | média das notas exibidas com arredondamento a 0,1 ou 0,01 | — | **refutada** | dá 6,7 / 6,67 | — |
| M2 | pesos desiguais; com as 5 avaliações, a faixa compatível (passo 0,001, arredondando) é wG 37,1–41,7%, **wA 38,7–40,7%**, wT 17,6–24,2% | IF | ativa | reproduz as 5 | perfis variados |
| M2a | arred₀,₁(0,4G + 0,4A + 0,2T) = (2G + 2A + T)/5 | IF | **apoiada**: acertou três avaliações seguidas fora da amostra (003: 6,50; 004: 6,44 → 6,4; 005: 6,88 → 6,9) | 6,58 → 6,6; 6,90 → 6,9; 6,50 → 6,5 | caso em que arredondar e truncar divirjam |
| M2b | trunc₀,₁((5G + 5A + 3T)/13) | H | ativa (menos simples); também acerta a 003 e a 005 (6,96 → 6,9) | 6,60; 6,97 → 6,9; 6,58 → 6,5 | casos em que arredondar e truncar divergem |
| M3 | 0,29G + 0,32A + 0,39T, exato | — | **refutada** pela 002 | — | — |
| M4 | (G+A+T − 0,05E)/3 | — | **refutada** pela 002 (dá 7,08) | — | — |
| M5 | média incluindo E | — | **refutada** | dá 6,00 | — |
| M6 | média com T invertido | — | **refutada** | dá 5,27 | — |
| M7 | geométrica / harmônica / mediana / mínimo | — | **refutadas** | dão 5,95 / 5,22 / 7,10 / 3,00 | — |
| M8 | nota holística do LLM, sem fórmula | H | ativa | — | X0; coincidência com M1 em n avaliações |
| R-wA | wA > 0 em qualquer média ponderada | C (condicional) | — | 6,6 < min(G, T) | — |

### Critérios

| ID | Hipótese | Classe | Status | Teste |
|---|---|---|---|---|
| G-esc | G em 0–10, passo 0,1 | IF | ativa | novas avaliações |
| MG1 | G = 10 − 0,025E | — | **refutada** pela 002 (dá 9,8; observado 9,7) | — |
| MG2 | G = arred₀,₁(10(1 − E/palavras)), com E = apontamentos exibidos | — | **refutada** pela 003: E = 0, mas G = 9,6 (acertara a 002) | — |
| MG2' | G = arred₀,₁(10(1 − n/palavras)), com n = contagem interna de erros, que inclui ortografia | H | ativa: compatível com as cinco (na 005, 403 palavras e G = 9,9 dão n de 3 a 6; E = 2 daria 9,95 → 10,0) | X1a/X1b |
| MG4 | G = arred₀,₁(10(1 − (E + 1,5·S)/W)), S = erros de ortografia, W = palavras nos primeiros 2.000 caracteres | H | **nova**: reproduz as 5; o peso 1,5 vem só da 003 e o corte em 2.000 só da 005 | novas provas com erros de ortografia |
| MG3 | G = 10 − 0,1E | — | **refutada** (dá 9,6) | — |
| E-cont | E é a contagem de todos os erros | — | **enfraquecida**: E = 0 num texto com ≥ 9 erros reais | — |
| H-E2 | E conta só desvios gramaticais ou sintáticos, e não ortografia | H | ativa, frágil ("guiado" deveria contar) | X1a (erros de concordância e crase) |
| E-fp | os 4 apontamentos são falsos positivos nos 5 trechos listados | H | ativa | X2 |
| T-ori | T: maior = mais aderente | IF | ativa | X6, X7 |
| T-tese | T sobe quando a tese nomeia o recorte | H | **enfraquecida** pela 004: recorte na introdução ("o limite entre ambos"), mas T = 7,4 | X6 |
| T-lex | T acompanha a presença literal das palavras da frase do tema | H | **apoiada**: a fórmula do v0.18 (4,91 + 3,09·palavras do tema + 0,87·pares) previu 8,9 para a 005, que teve 9,0. Reajustada com 5 pontos: T = 4,94 + 2,96·palavras do tema + 1,05·pares (erro máximo 0,08; deixando um ponto de fora, 0,13). Teto aparente: 9,0 com o tema completo e todos os pares; não se sabe o que leva acima disso | L1 |
| T-R1 | T = 10 − 3·(palavras do tema ausentes) − 0,8·(pares ausentes) − 0,25·(palavras do tema ausentes da introdução) − 1,05·(sem a frase do tema completa no último parágrafo) | H | **nova**: reproduz as 5 exatamente; o último termo nunca foi observado (H-T-conc) | M6 tem a frase no último parágrafo: previsão 10,0 |
| T-prop | T acompanha a proporção do texto dedicada ao recorte | H | ativa | X4, X5, X7 |
| H-A1 | A = cobertura das perguntas (0–10) | H | **enfraquecida** | X7 |
| H-A1' | A = contagem de perguntas (0–4) | H | **enfraquecida** | — |
| H-A2 | A = profundidade de desenvolvimento | H | **fortemente enfraquecida**: 003 (genérico) e 004 (mecanismos e três dimensões de consequências) tiveram 2,4 as duas | — |
| H-A3 | A = fatos e repertório | H | **fortemente enfraquecida**: 004 (Bauman, CNC, ONU) e 003 (nada) tiveram 2,4 as duas; 002 (nada) superou 001 (1 fato); 005 (lei, Panorama, Freire) teve 2,8, abaixo da 002 | — |
| H-A4 | A = extensão | H | **enfraquecida**: a 005, a mais longa (403 palavras), teve 2,8, abaixo da 001 e da 002; dentro do lixo, os textos mais curtos tiveram A maior (266 → 3,2; 281 → 3,0; 403 → 2,8), o que é pouco para concluir | controle de extensão no L1 |
| H-A5 | A = gabarito de tópicos do tema, ou base fixa por tema | H | **reforçada**: as notas continuam agrupadas por tema (lixo 3,0/3,2/2,8; consumo 2,4/2,4), com variação de ±0,2 dentro do tema | mais temas; clima |
| H-A9 | A acompanha a cobertura lexical do núcleo da proposta (frase do tema + perguntas) | — | **refutada** pela 005: a fórmula do v0.18 (0,60 + 3,89·núcleo) previu 4,2 para núcleo 0,93; observado 2,8, abaixo das 001 e 002, que tinham núcleo 0,60 e 0,67 | — |
| H-A-esc | A exibida = 0,4 × nota bruta de 0 a 10 (em meios pontos); teto exibido 4,0 e nota online máxima 7,6 | H | **nova**: as cinco A são múltiplos de 0,2 (chance de ~1/32 por acaso) e A ÷ 0,4 = 7,5 / 8 / 6 / 6 / 7 | série 005: A > 4,0 refuta; décimo ímpar refuta |
| A-R1 | nota bruta = 10 − 0,5 por parágrafo sem evidência concreta e pertinente − 1 se o recorte falta na introdução − 2 por dado ou argumento que não prova − 1 por dado vago − 1 por repertório de bolso (`modelo/rubrica-calibrada.md`) | H | **nova**: reproduz as 5 (7,5; 8; 6; 6; 7), mas três descontos foram ajustados a uma prova cada | previsões D2 4,0; C2 3,8; M6 3,8 |
| H-A6 | A = diversidade de dimensões | H | **enfraquecida** | — |
| H-A7 | A em níveis discretos | — | **enfraquecida**: A = 3,2 não é inteiro | — |
| H-A8 | A instável | H | ativa | X0 |
| A-corr | a plataforma é mais exigente que a régua do ENEM na Abrangência (original: régua 6, observado 3,0): deslocamento de −3 ou razão de 0,5 | H | ativa | X8, X9 |

### Nota Final

| ID | Hipótese | Status |
|---|---|---|
| F≠O | Nota Final e nota online são grandezas distintas | **confirmada** (6,6 ≠ 0 na mesma redação) |
| P-ID | Nota Final = nota online | **refutada** |
| P-Z0 / P-FT / P-N5 / P-N6 | zera se algum critério = 0 / se T = 0 / se nota online < 5 / se nota online < 6, como explicação suficiente | **refutadas como explicação única** |
| P-N7 | zera se nota online < 7 | **enfraquecida**: o corte documentado é 6,0 |
| P-A5 | zera se A < 5 (ou algum critério < 5) | ativa, mas não documentada (o documento fala só em "zerar" um critério) |
| P-OUT | causa externa às notas (status do processo, integridade, etapa pendente) | **reforçada**: campo "calculado para a inscrição"; pelas regras documentadas, 6,6 e 6,9 classificariam |
| P-DOC | regra documentada: classificado com nota ≥ 6,0 e nenhum critério zerado | **documentada** (FPP); não explica o 0,00 |
| P-ED | o corte da edição dessas provas é diferente do publicado para Verão 2027 (por exemplo, 7,0) | ativa: explicaria as quatro; depende do edital da edição |
| P-CAMPO | a "Nota Final" é um campo genérico da inscrição, usado em outra modalidade (por exemplo, ENEM), e fica 0 na redação online | ativa: explicaria as quatro sem afetar o resultado |
| P-ETAPA | a Nota Final só é calculada depois de uma etapa posterior (o botão "Continuar" sugere um fluxo em andamento) | ativa |
| P-E | zera por apontamentos (≥ 4, ou = 0 como "critério zerado") | **não explica**: E = 4, 7 e 0, sempre com Nota Final 0 |
| P-EXT | zera por extensão abaixo do mínimo | muito improvável (1.564 a 1.844 caracteres) |
| P-MAX | zera por exceder o máximo de 2.000 caracteres | **não explica**: 1.844 caracteres, contando as quebras |

## 4. Previsões registradas e resultados

As previsões numéricas estão em `experimentos/protocolo.md`. Registre aqui cada comparação.

| Data | Experimento | Previsão (modelo) | Observado | Acertou? | Consequência |
|---|---|---|---|---|---|
| 2026-10-30 | avaliação 005 (fora da amostra) | v0.18: A = 0,60 + 3,89·0,93 = 4,2 | 2,8 | não | H-A9 refutada; o simulador passa a usar a base do tema para A |
| 2026-10-30 | avaliação 005 (fora da amostra) | v0.18: T = 4,91 + 3,09·1,00 + 0,87·1,00 = 8,9 | 9,0 | sim (erro 0,1) | T-lex apoiada e reajustada |
| 2026-10-30 | avaliação 005 (fora da amostra) | M2a com as notas parciais exibidas: 6,88 → 6,9 | 6,9 | sim | M2a: 5 de 5; faixa de wA estreita para 38,7–40,7% |

## 5. Questões em aberto

1. O que a Abrangência mede. Já não acompanham A: fatos, repertório, profundidade, extensão e vocabulário da proposta.
   O que sobra: base por tema com variação pequena (H-A5) ou ruído do avaliador (H-A8). O teste mais barato é reenviar
   um texto idêntico (X0).
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
| v0.6 | 2026-10-17 | série 003: texto paralelo M2, escrito do zero, sem repertório em comum com o M1 e com a mesma nota pela rubrica; o par testa o que a rubrica não captura |
| v0.7 | 2026-10-17 | série 003: texto M3, de amarração máxima, com mapa de ligações verificado por `ferramentas/verificar_amarracao.py` |
| v0.8 | 2026-10-17 | série 003: revisão de coesão do M3 e texto M4 (premissa do acúmulo, transições temáticas, concessão com dados do SEEG e da EPE, proposta 2 alinhada ao diagnóstico) |
| v0.9 | 2026-10-17 | série 003: M5, segunda redação do Claude, escrita sem ver o texto do usuário, para comparação |
| v0.10 | 2026-10-17 | série 003: M5 revisado (coesão) e fortalecido (déficit habitacional da FJP como premissa da proposta 1; oposição norma × prática na tese) |
| v0.11 | 2026-10-27 | avaliação 002 (texto B, mesmo tema): média simples refutada; pesos ~0,4/0,4/0,2; MG2 apoiada; instituição e regras documentadas (FPP) |
| v0.12 | 2026-10-27 | avaliação 003 (consumo): M2a acerta a previsão; MG2 com apontamentos refutada (vira MG2' com contagem interna); H-E2; T-tese com mais apoio; contagem de caracteres da plataforma |
| v0.13 | 2026-10-27 | avaliação 004: M2a acerta de novo; a Abrangência não responde a fatos, profundidade nem extensão; hipóteses lexicais H-A9 e T-lex; plataforma identificada (CRM Educacional) e definições do fornecedor; experimento L1 |
| v0.14 | 2026-10-27 | as quatro avaliações foram provas reais; título da 004 incluído no texto (T continua na mesma ordem dos pares de palavras do tema: 2, 5, 6, 10 → 7,1; 7,4; 8,5; 8,7); hipóteses P-ED, P-CAMPO e P-ETAPA para a Nota Final |
| v0.15 | 2026-10-27 | orientações da professora registradas e comparadas com os dados; o relatório 001 dizia que seguir o plano induz ao tangenciamento, e isso fica enfraquecido |
| v0.16 | 2026-10-27 | C2: o C1 reescrito pelo método da professora (uma pergunta por parágrafo, dado que prova a afirmação, sem repertório de bolso), com cobertura do núcleo 1,00 e previsões registradas |
| v0.17 | 2026-10-27 | a proposta é sorteada entre três temas (lixo, consumismo, clima); roteiros de preparação por tema em `modelo/roteiros-por-tema.md` |
| v0.18 | 2026-10-27 | série 005: D2 (lixo), C2 (consumo) e M6 (clima) pelo método, com cobertura do núcleo 1,00 e previsões registradas; ferramenta de sobreposição aceita um texto avulso e inclui o tema clima |
| v0.19 | 2026-10-30 | avaliação 005: M2a acerta de novo; T-lex apoiada e reajustada; H-A9 refutada; o simulador passa a estimar A pela base do tema (lixo 3,0, consumo 2,4) e o teto dele cai de 7,6 para cerca de 7,0 |
| v0.20 | 2026-10-30 | simulador: a nota principal passa a ser a nota pelo critério (meta 10), pela rubrica híbrida v0.4; a previsão da plataforma fica como referência. Na rubrica, H3b deixa de tratar a ordem das perguntas como defeito (método da professora) |
| v0.21 | 2026-10-30 | rubrica calibrada v1 (`modelo/rubrica-calibrada.md`, `ferramentas/rubrica_calibrada.py`): critérios com teto 10 que reproduzem G, A, T e a nota online das 5 provas; H-A-esc (A exibida = 0,4 × bruta; teto online 7,6), A-R1, T-R1, MG4; previsões da série 005 registradas |
| v0.22 | 2026-10-31 | simulador passa à rubrica calibrada v1: nota pelo critério (teto 10), previsão da plataforma com a Abrangência × 0,4, card "O que falta para 10" com cada desconto; a prévia sem IA reproduz A e T das 5 provas |
