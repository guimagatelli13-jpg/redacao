# Relatório 002 — Segunda avaliação (texto B, mesmo tema)

Base empírica: 2 avaliações (001 e 002), as duas com a proposta "Descarte correto do lixo". Dados em
`avaliacoes/002-descarte-lixo-b/` e `dados/avaliacoes.csv`. Os números podem ser reproduzidos com
`python3 ferramentas/testar_modelos.py`.

## 1. Dados

| | 001 | 002 (texto B) |
|---|---|---|
| Gramática | 9,90 | 9,70 |
| Abrangência | 3,00 | 3,20 |
| Tangenciamento | 7,10 | 8,70 |
| Apontamentos | 4,00 | 7,00 |
| Nota online | 6,60 | 6,90 |
| Nota Final | 0,00 | 0,00 |
| Caracteres com espaços / palavras | 1.841 / 281 | 1.831 / 266 |
| Primeira menção ao recorte (educação/conscientização) | 57% do texto | 17% (na tese) |
| Fatos verificáveis / fontes | 1 (PNRS, 2010) / 0 | 0 / 0 |

## 2. Fórmula da nota online

- **A média simples está refutada.** (9,7 + 3,2 + 8,7)/3 = 7,2, e não 6,9. Isso vale também com truncamento,
  arredondamento ou precisão oculta. A escolha de M1 no relatório 001 foi por parcimônia, e a segunda observação a
  derrubou.
- **Só uma combinação da grade de 0,05 sobrevive:** 0,4·G + 0,4·A + 0,2·T, com arredondamento a 0,1. Ela dá 6,58 →
  6,6 e 6,90 → 6,9. Em forma equivalente: (2G + 2A + T)/5.
- **Com pesos contínuos, a faixa compatível é estreita:** wG de 37% a 46%, **wA de 38% a 42%** e wT de 13% a 25%.
  O peso da Abrangência está praticamente identificado (≈ 40%) qualquer que seja a regra de arredondamento.
- **Arredondar ou truncar ainda não está decidido.** (5G + 5A + 3T)/13 com truncamento também reproduz os dois casos.
- **O apontamento de erro não entra na média.** Todos os modelos que o incluíam foram refutados.

Consequência prática: cada ponto de Abrangência vale cerca de 0,4 na nota online; cada ponto de Tangenciamento, cerca
de 0,2. No texto B, o Tangenciamento subiu 1,6 em relação ao 001 e acrescentou só cerca de 0,3 à nota.

## 3. Gramática

G = arred₀,₁(10·(1 − apontamentos/palavras)) acerta os dois casos:
- 001: 10·(1 − 4/281) = 9,86 → 9,9;
- 002: 10·(1 − 7/266) = 9,74 → 9,7.

A hipótese foi formulada antes da segunda avaliação, então este é o primeiro acerto preditivo do modelo. A
alternativa linear (10 − 0,025 por apontamento) previa 9,8 e foi refutada. Nessa escala, cada apontamento custa ~0,037
em G e ~0,015 na nota online.

Trechos do texto B que podem ter sido apontados (hipótese, porque a plataforma não mostra as marcações):
- "seja pela falta de informação **ou** pela ausência…", correlação que a norma prescreve como "seja… seja";
- gerúndios, alguns ambíguos: "colocando em risco", "**contribuindo** para a preservação", que parece dizer que o
  desperdício contribui para a preservação, e "mostrando que…";
- repetição de "descarte".

## 4. Abrangência: quase não se mexe

Os dois textos são muito diferentes em dados e fontes (o 001 tem 1 fato, o B nenhum), mas tiveram notas quase iguais
(3,0 e 3,2), e o texto sem fatos teve a nota maior.
- **Fatos e repertório (H-A3):** enfraquecida.
- **Notas inteiras (H-A7):** enfraquecida.

O que os dois têm em comum:
- os dois cobrem as 4 perguntas da proposta;
- têm cerca de 1.830 caracteres;
- usam argumentos genéricos, afirmados sem desenvolvimento.

Continuam abertas: profundidade (H-A2), gabarito de tópicos (H-A5) e ruído (H-A8). As redações X8, X9 e M1–M5
continuam sendo o melhor teste, porque mudam exatamente essas dimensões.

## 5. Tangenciamento: primeiro apoio, ainda não controlado

O texto B nomeia o recorte na tese ("a educação e a conscientização ambiental são fundamentais…") e dedica um
parágrafo inteiro a ele. Teve 8,7, contra 7,1 do 001, que só menciona o recorte aos 57% do texto. Isso é compatível
com T-tese e T-prop, mas os textos diferem em muitas outras coisas.

## 6. Nota Final 0,00

- A tela agora descreve o campo: **"Exibe a nota final calculada para a inscrição."**
- Regras documentadas pela FPP: redação online até 10 pontos; classificação com **6,0 ou mais, sem zerar nenhum
  critério**.
- As duas notas online (6,6 e 6,9) são maiores que 6,0, e nenhum critério foi zerado. Pelas regras documentadas, as
  duas inscrições seriam classificadas.

Logo, o 0,00 não decorre das regras de nota. A explicação mais provável é de status da inscrição (P-OUT): a nota ainda
não foi calculada ou homologada, ou o envio foi treino, ou a inscrição está incompleta. A pergunta que resolve isso:
esses envios foram inscrições reais ou simulados? A página mostrava algum status?

## 7. Previsões revisadas para os textos já escritos

Com M2a e G = 10, para os textos X8, X9, C1 e M1–M5:

| Abrangência | T = 9 | T = 10 |
|---|---|---|
| 3,1 (nível dos dois textos reais) | 7,0 | 7,2 |
| 5 | 7,8 | 8,0 |
| 7 | 8,6 | 8,8 |
| 10 | 9,8 | 10,0 |

As previsões registradas nos protocolos foram calculadas com M1, que agora está refutada. Elas ficam registradas como
foram feitas; a comparação com resultados futuros deve usar esta tabela e anotar a mudança de modelo.

## 8. Fontes

- [Blog FPP: Vestibular de Verão 2027](https://fpp.edu.br/blog/vestibular-verao-2027-fpp/) (nota até 10; corte 6,0;
  nenhum critério zerado)
- [Edital FPP 016, Verão 2026](https://fpp.edu.br/wp-content/uploads/2025/09/Edital-FPP-016-Demais-cursos_-verao-2026.pdf)
  (classificação pela nota da redação; 1.200 a 2.000 caracteres)
- [Edital FPP 009/2026, Inverno 2026](https://fpp.edu.br/wp-content/uploads/2026/04/Edital-FPP-009_2026-Demais-cursos_inverno-2026.pdf)
- [Formas de ingresso FPP](https://fpp.edu.br/formas-de-ingresso-graduacao-fpp/)

O domínio fpp.edu.br está bloqueado na rede deste ambiente. Os trechos acima vieram de resultados de busca; o PDF
completo não foi lido.
