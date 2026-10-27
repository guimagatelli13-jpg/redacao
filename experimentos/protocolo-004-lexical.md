# Protocolo — experimento L1: sobreposição lexical com a proposta

Previsões registradas em 2026-10-27, antes de qualquer resultado.

## Hipóteses testadas

- **H-A9:** a Abrangência acompanha quanto do vocabulário central da proposta (frase do tema e perguntas) aparece no
  texto. Nas quatro avaliações, a cobertura do núcleo e a Abrangência têm a mesma ordem: 0,44 → 2,4; 0,50 → 2,4;
  0,60 → 3,0; 0,67 → 3,2. Ao mesmo tempo, dados, fontes, profundidade e extensão não mudaram a nota: as redações 003
  e 004 diferem muito nesses aspectos e tiveram 2,4 as duas.
- **T-lex:** o Tangenciamento acompanha a presença literal das palavras da frase do tema. Os textos com todas elas
  tiveram 8,5 e 8,7; os com 2/3 delas, 7,1 e 7,4. Isso explica a 004 melhor que T-tese: a 004 tem o recorte na
  introdução ("Estabelecer o limite entre ambos"), mas sem as palavras "necessário" e "exagero", e teve 7,4.

## Variável única

Texto-base: redação 004 (`avaliacoes/004-consumo-b/redacao.txt`), **com o título na primeira linha, como foi
submetido**. Variante: `experimentos/textos/L1-004-lexical.txt`, com o mesmo título.
Três frases foram trocadas por versões que repetem palavras da proposta, sem mudar nenhuma ideia:

| Antes | Depois |
|---|---|
| Estabelecer o limite entre **ambos** é, portanto, um desafio urgente. | Estabelecer o limite entre **o necessário e o exagero** é, portanto, um desafio urgente. |
| Além dos prejuízos financeiros, o consumismo desenfreado **causa** graves danos ambientais. | Além dos prejuízos financeiros, entre as **principais consequências** do consumismo desenfreado estão graves danos ambientais. |
| Portanto, é preciso estimular o consumo consciente. | Portanto, são necessárias **ações que contribuem para que a população possa consumir de forma consciente**. |

Efeitos medidos pelas ferramentas:
- cobertura do núcleo: de 0,50 para 1,00;
- palavras do tema presentes: de 0,67 para 1,00;
- extensão: 1.808 → 1.914 caracteres com o título (+5,9%; 1.922 com linhas em branco), dentro do limite.

Atenção: as quatro avaliações foram provas reais. Submeta a L1 apenas em modo de simulado ou treino da mesma
plataforma, se houver; não gaste uma inscrição real com um experimento.

## Previsões

| Campo | Se H-A9 e T-lex estiverem certas | Se não estiverem (hipótese nula) |
|---|---|---|
| Abrangência | sobe para algo entre 3 e 5 (extrapolando a tendência; a cobertura 1,00 está fora da faixa observada) | fica perto de 2,4 |
| Tangenciamento | sobe para 8,5 ou mais | fica perto de 7,4 |
| Gramática | 10 (nenhum erro inserido) | 10 |
| Nota online (M2a) | 6,9 a 7,7 | cerca de 6,4 |

Interpretação dos resultados:
- **A e T sobem:** a plataforma mede, ao menos em parte, a sobreposição de vocabulário com a proposta. Isso também
  explicaria por que fatos e profundidade não mexeram na Abrangência.
- **Só T sobe:** T-lex fica apoiada e H-A9 enfraquece.
- **Nada muda:** as duas hipóteses enfraquecem, e a dependência do tema fica sem explicação (gabarito por tema, H-A5,
  ou ruído, H-A8).
- **Limitação:** a extensão também aumenta 6%. Pelos dados até aqui, a extensão não move a Abrangência (a 004 é mais
  longa que a 003 e teve a mesma nota), mas um texto de controle com +6% de frases sem palavras da proposta separaria
  os dois efeitos.

## Resultado

| Texto | Nota Final | G | A | T | E | Nota online | Observações |
|---|---|---|---|---|---|---|---|
| 004 (base) | 0,00 | 10,00 | 2,40 | 7,40 | 1,00 | 6,40 | observado |
| L1 | | | | | | | |
