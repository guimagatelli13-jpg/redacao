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

## 2. Dados de contexto informados depois da análise inicial

| Data | Informação | Fonte | Efeito no modelo |
|---|---|---|---|
| 2026-10-16 | limite máximo de 2.000 caracteres | informado pelo usuário (sem documento) | H-A4 enfraquecida; P-MAX não explica o zero; X3, X4, X5 e X8 refeitos para caber no limite |
| 2026-10-27 | instituição: Faculdades Pequeno Príncipe (FPP); a "Nota Final" tem a descrição "Exibe a nota final calculada para a inscrição" | tela da plataforma | a Nota Final é um campo da inscrição; P-OUT reforçada |
| 2026-10-27 | o simulador usa o mesmo sistema da prova oficial, e o tema é sorteado entre lixo, consumismo e clima; o tema real da prova será outro | informado pelo usuário | os envios no simulador são experimentos válidos para o sistema real; série 005 |
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
| M2 | pesos desiguais; com 001 e 002 a faixa compatível encolheu para wG 37–46%, **wA 38–42%**, wT 13–25% | IF | ativa | reproduz 001 e 002 | perfis variados |
| M2a | arred₀,₁(0,4G + 0,4A + 0,2T) = (2G + 2A + T)/5 | IF | **apoiada**: acertou duas previsões seguidas (003: 6,50; 004: 6,44 → 6,4) | 6,58 → 6,6; 6,90 → 6,9; 6,50 → 6,5 | caso em que arredondar e truncar divirjam |
| M2b | trunc₀,₁((5G + 5A + 3T)/13) | H | ativa (menos simples); também acerta a 003 (6,58 → 6,5) | 6,60; 6,97 → 6,9; 6,58 → 6,5 | casos em que arredondar e truncar divergem |
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
| MG2' | G = arred₀,₁(10(1 − n/palavras)), com n = contagem interna de erros, que inclui ortografia | H | ativa: compatível com as três (n de 1–4, de 7–9 e de 9–11; no 003 há ≥ 9 erros reais) | X1a/X1b |
| MG3 | G = 10 − 0,1E | — | **refutada** (dá 9,6) | — |
| E-cont | E é a contagem de todos os erros | — | **enfraquecida**: E = 0 num texto com ≥ 9 erros reais | — |
| H-E2 | E conta só desvios gramaticais ou sintáticos, e não ortografia | H | ativa, frágil ("guiado" deveria contar) | X1a (erros de concordância e crase) |
| E-fp | os 4 apontamentos são falsos positivos nos 5 trechos listados | H | ativa | X2 |
| T-ori | T: maior = mais aderente | IF | ativa | X6, X7 |
| T-tese | T sobe quando a tese nomeia o recorte | H | **enfraquecida** pela 004: recorte na introdução ("o limite entre ambos"), mas T = 7,4 | X6 |
| T-lex | T acompanha a presença literal das palavras da frase do tema | H | **nova**: explica as 4 avaliações (todas as palavras → 8,5/8,7; 2/3 → 7,1/7,4; na 004 faltam "necessário" e "exagero") | L1 |
| T-prop | T acompanha a proporção do texto dedicada ao recorte | H | ativa | X4, X5, X7 |
| H-A1 | A = cobertura das perguntas (0–10) | H | **enfraquecida** | X7 |
| H-A1' | A = contagem de perguntas (0–4) | H | **enfraquecida** | — |
| H-A2 | A = profundidade de desenvolvimento | H | **fortemente enfraquecida**: 003 (genérico) e 004 (mecanismos e três dimensões de consequências) tiveram 2,4 as duas | — |
| H-A3 | A = fatos e repertório | H | **fortemente enfraquecida**: 004 (Bauman, CNC, ONU) e 003 (nada) tiveram 2,4 as duas; 002 (nada) superou 001 (1 fato) | — |
| H-A4 | A = extensão | H | **enfraquecida**: o texto usou 92% do máximo e teve A ≈ 3; e a 004, mais longa que a 003, teve a mesma nota | controle de extensão no L1 |
| H-A5 | A = gabarito de tópicos do tema | H | ativa: as notas se agrupam por tema (lixo 3,0/3,2; consumo 2,4/2,4) | L1; mais temas |
| H-A9 | A acompanha a cobertura lexical do núcleo da proposta (frase do tema + perguntas) | H | **nova**: mesma ordem nas 4 avaliações (0,44/0,50/0,60/0,67 → 2,4/2,4/3,0/3,2); confundida com o tema | L1 |
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
