# Protocolo — série 002 (tema "Consumo e consumismo", simulado de treinamento)

Previsões registradas em 2026-10-16, antes de qualquer resultado.
- Proposta: `propostas/002-consumo-consumismo.md`.
- Texto: `experimentos/textos/C1-consumo-hibrida.txt`.
- Rubrica aplicada: `modelo/rubrica-hibrida-enem.md` (v0.3).

## Por que esta série é informativa

1. **Primeiro teste fora do tema em que a rubrica foi construída.** As âncoras vêm só do tema do lixo. Se as notas
   caírem dentro das faixas previstas, a rubrica ganha apoio como modelo geral da plataforma. Se não caírem,
   ganha força H-A5 (Abrangência medida contra um gabarito de tópicos de cada tema).
2. **Segunda observação para a fórmula.** Qualquer resultado com G, A e T diferentes do 001 testa a média truncada
   (M1) fora da amostra que a gerou.
3. **Simulado de treinamento.** Sem risco de gastar uma tentativa oficial. A Nota Final do simulado também ajuda a
   separar as hipóteses do portão: se ela vier preenchida, compare com a nota online; se vier 0,00 ou vazia com nota
   online acima de 7, ganha apoio P-OUT (campo de processo seletivo, e não da redação).

## O recorte deste tema

- **Assunto amplo:** consumo e consumismo.
- **Recorte:** *como estabelecer o limite* entre o necessário e o exagero.

Pelo modelo de Tangenciamento (T-tese, T-prop), um texto que só descreve o consumismo e suas consequências ficaria
no assunto amplo. Por isso a tese do C1 propõe um critério explícito para o limite: a finalidade da compra, avaliada
por necessidade real e orçamento. O parágrafo central transforma esse critério em perguntas aplicáveis.

## Medidas do texto C1

| Indicador | Valor |
|---|---|
| Caracteres com espaços / sem espaços | 1.986 / 1.670 (1.989 contando as quebras; limite de 2.000) |
| Palavras / parágrafos / frases | 320 / 4 / 12 |
| Recorte | nomeado na 2ª frase (11% do texto); retomado nos 4 parágrafos |
| Perguntas da proposta | P1: diferença (Bauman); P2: consequências (endividamento, ambiente); P3: como estabelecer o limite; P4: ações |
| Repertórios e fatos | Zygmunt Bauman, *Vida para consumo* (introdução e conclusão); Serasa: 81,2 milhões de inadimplentes no fim de 2025, 49,7% dos adultos; Global Footprint Network: consumo equivalente a ~1,7–1,8 planeta; BNCC: educação financeira e educação para o consumo entre os temas contemporâneos transversais; Lei 14.181/2021 (Lei do Superendividamento) |
| Proposta de intervenção | agente (Ministério da Educação), ação (tornar efetiva a educação financeira e para o consumo), meio (aulas práticas de orçamento doméstico e de análise crítica de propagandas), finalidade (distinguir necessidade de desejo), detalhamento (desde o ensino fundamental); segunda proposta: Procons |
| Construções propensas a falso positivo | 0 |

Confira antes de submeter, como no protocolo 001: os números da Serasa e da Global Footprint Network são de
reportagens que citam essas fontes, e as datas de referência podem ter sido atualizadas.

## Avaliação pela rubrica híbrida e previsões

| Critério híbrido | Nota | Fundamento |
|---|---|---|
| H1 norma (C1) | 10 | nenhum desvio encontrado; nenhuma construção de risco |
| H2 recorte (C2, tema) | 10 | critério do limite na tese e retomado em todos os parágrafos |
| H3a repertório (C2) | 10 | repertório legitimado e produtivo na introdução e em cada desenvolvimento; dois dados com fonte |
| H3b desenvolvimento (C3) | 10 | a introdução anuncia os eixos (publicidade e crédito apagam o limite; educação o restabelece). Ponto mais frágil: BNCC e Lei do Superendividamento mostram reconhecimento institucional, e não eficácia |
| H4 coesão (C4) | 10 | "Desse modo", "Em primeiro lugar", "Em segundo lugar", "Portanto", "Não por acaso", "por sua vez"; nenhum conectivo repetido |
| H5 intervenção (C5) | 10 | 5 elementos na primeira proposta |
| **ENEM equivalente** | **1000** | estimativa do autor da rubrica |

| Campo da plataforma | Previsão |
|---|---|
| Gramática | 10,0 (faixa 9,9–10,0) |
| Tangenciamento | 9–10 |
| Abrangência | 5–10 (régua 10; 7 com deslocamento; 5 com razão) |
| Nota online | 8,0–10,0, por trunc₀,₁((10 + A + T)/3) |
| Apontamento de erro gramatical | 0 a 2 |

O que cada resultado significaria:
- **Tudo dentro das faixas:** primeira previsão bem-sucedida fora do tema de origem. Ainda é fraca, porque as faixas
  são largas, mas é a primeira evidência preditiva.
- **Abrangência abaixo de 5:** a régua do ENEM não descreve a Abrangência, nem com correção. Ganham peso H-A5
  (gabarito do tema) e H-A8 (ruído). Peça ou anote qualquer comentário do avaliador sobre o que faltou.
- **Tangenciamento abaixo de 9:** o critério do limite não foi lido como tese do recorte. T pode exigir a expressão
  literal do tema, o que é testável com uma variante que repita "como estabelecer limite entre o necessário e o
  exagero" na tese.
- **Nota online diferente de trunc₀,₁((G + A + T)/3):** M1 fica refutada; rode `ferramentas/testar_modelos.py` com a
  nova linha no CSV.

Aviso de circularidade: rubrica, texto e avaliação são do mesmo autor.

## Texto C2: C1 reescrito pelo método da professora (2026-10-27)

`experimentos/textos/C2-consumo-metodo.txt` (1,982 caracteres; 1,988 como a plataforma conta, com as linhas em
branco; 331 palavras). Elos: `experimentos/textos/C2-consumo-metodo.elos.json` (11 de 11).

| Regra | Como o C2 cumpre | Problema do C1 que foi corrigido |
|---|---|---|
| Uma pergunta por parágrafo, aberta com as palavras dela | P1 "A diferença entre consumo e consumismo…"; P2 "Para estabelecer limite entre o necessário e o exagero ao consumir…"; P3 "Entre as principais consequências de um consumismo desenfreado…"; P4 "…ações contribuem para que a população possa consumir produtos de forma mais consciente" | o C1 organizava por eixos próprios |
| Cada resposta serve ao recorte | todo parágrafo fecha no limite entre o necessário e o exagero | — |
| O dado prova a afirmação | P2: o art. 49 do CDC (prazo de reflexão) prova que a lei reconhece decisões que merecem ser repensadas; P3: a queda de 36% no uso das roupas antes do descarte (Fundação Ellen MacArthur) prova compra além do uso; o lixo eletrônico (ONU) cresce, entre outros fatores, pelo consumo e pela falta de conserto | o C1 usava a inadimplência (Serasa) como sinal de consumismo |
| Nada de repertório de bolso | nenhum autor de bolso; só uma lei e dois dados específicos | o C1 usava Bauman |
| Vocabulário da proposta | cobertura do núcleo 1,00; todas as palavras do tema; 10 de 11 pares de palavras do tema | C1: núcleo 0,50 |
| Propostas ligadas às causas | educação para o consumo (orçamento e propagandas, do P2); peças e conserto acessíveis (falta de conserto, do P3) | — |

Previsões (M2a; registradas antes de qualquer resultado):

| Campo | H-A9 e T-lex certas | Hipótese nula |
|---|---|---|
| Gramática | 10 (nenhum erro encontrado) | 10 |
| Tangenciamento | 8,5 a 9,5 | 8,5 a 9,5 (todas as palavras do tema estão presentes, como no 003) |
| Abrangência | 3 a 5 | cerca de 2,4 |
| Nota online | 6,9 a 7,9 | cerca de 6,7 |

Use só em simulado. Numa prova real, a decisão é do candidato.

## Resultado

| Texto | Nota Final | G | A | T | E | Nota online | Status/obs. |
|---|---|---|---|---|---|---|---|
| C1 | | | | | | | |
| C2 | | | | | | | |
