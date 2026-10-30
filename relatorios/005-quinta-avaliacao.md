# Relatório 005 — quinta avaliação (lixo, texto C)

Retrato de 2026-10-30. Dados: `avaliacoes/005-descarte-lixo-c/`.

## O que foi observado

| G | A | T | E | Nota online | Nota Final |
|---|---|---|---|---|---|
| 9,90 | 2,80 | 9,00 | 2,00 | 6,90 | 0,00 |

O texto tem 403 palavras e 2.736 caracteres, acima do limite de 2.000. Repete a frase do tema na introdução e no
3º parágrafo e abre cada parágrafo com as palavras da sua pergunta: núcleo 0,93, palavras do tema 1,00, pares do
tema 12 de 12. É, de longe, o texto mais "colado" ao vocabulário da proposta entre as cinco avaliações.

## Teste do modelo v0.18

As fórmulas do v0.18 estavam publicadas no simulador antes desta avaliação, então a 005 é um teste fora da amostra.

| Grandeza | Previsto (v0.18) | Observado | Resultado |
|---|---|---|---|
| Nota online, a partir de G, A e T exibidos (M2a) | 0,4·9,9 + 0,4·2,8 + 0,2·9,0 = 6,88 → 6,9 | 6,9 | acertou |
| Tangenciamento (T-lex) | 4,91 + 3,09·1,00 + 0,87·1,00 = 8,9 | 9,0 | acertou (erro 0,1) |
| Abrangência (H-A9) | 0,60 + 3,89·0,93 = 4,2 | 2,8 | **errou por 1,4** |

## Conclusões

1. **M2a continua de pé** [IF]. Com 5 de 5, a faixa de pesos compatíveis estreitou: wA entre 38,7% e 40,7%.
2. **T-lex sai apoiada** [IF]. Reajustada com os cinco pontos: T = 4,94 + 2,96·(palavras do tema) + 1,05·(pares do
   tema), com erro máximo de 0,08. Com o tema completo, o T observado chega a 9,0. Não há dado sobre o que leva
   acima disso.
3. **H-A9 está refutada.** O vocabulário da proposta não move a Abrangência: com núcleo 0,93, a 005 teve 2,8, menos
   que a 001 (0,60 → 3,0) e a 002 (0,67 → 3,2). A ordem observada nas quatro primeiras avaliações era confundida com
   o tema.
4. **A Abrangência continua agrupada por tema** (lixo 3,0/3,2/2,8; consumo 2,4/2,4). Fatos, repertório, profundidade,
   extensão e vocabulário já foram descartados como explicação. Restam uma base por tema com variação pequena
   (H-A5) e ruído do avaliador (H-A8). O teste mais barato é reenviar um texto idêntico.
5. **Teto prático.** Com o que se sabe, a nota online máxima é por volta de 0,4·10 + 0,4·3,2 + 0,2·9,0 ≈ 7,1 no lixo
   e 0,4·10 + 0,4·2,4 + 0,2·9,0 ≈ 6,8 no consumo. O teto de 7,6 do simulador v0.18 vinha da fórmula refutada de A.
6. **Limite de caracteres.** Se o texto registrado é o que foi enviado, a plataforma aceitou 2.736 caracteres e
   avaliou normalmente. A Nota Final ficou 0,00, igual às quatro anteriores, então isso não ajuda a explicar o zero.

## Consequências

- O simulador passa ao modelo v0.19: A pela base do tema; T pela fórmula reajustada.
- As previsões da série 005 ganham uma revisão datada em `experimentos/protocolo-005-simulado-metodo.md`.
