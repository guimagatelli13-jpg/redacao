# Protocolo 008 — três redações pelo método da professora, corrigidas até não sobrar falha

Registrado em 2026-10-31, antes de qualquer envio. Pedido do usuário: escrever uma redação por tema seguindo
principalmente as orientações da professora (`fontes/orientacoes-professora.md`), corrigir, achar falhas, reescrever
e repetir até não haver pontas soltas nem tangenciamento e haver abrangência. Use os textos **só no simulador**.

| Tema | Texto final | Caracteres (como a plataforma conta) | Elos de amarração |
|---|---|---|---|
| Descarte correto do lixo | `experimentos/textos/D4-lixo-professora.txt` | 1.913 | 12 de 12 |
| Consumo e consumismo | `experimentos/textos/C4-consumo-professora.txt` | 1.989 | 10 de 10 |
| Mudanças climáticas | `experimentos/textos/M8-clima-professora.txt` | 1.998 | 11 de 11 |

As versões intermediárias estão em `experimentos/textos/serie-008/` (lixo v1 a v6, consumo v1 a v5, clima v1 a v6).

## Critérios da correção

Da professora:
- **P1:** uma pergunta por parágrafo (no clima, cinco perguntas e cinco parágrafos).
- **P2:** cada resposta pertinente ao recorte.
- **P3:** o dado prova exatamente a afirmação.
- **P4:** nenhum repertório de bolso.
- **P5:** nenhuma lacuna nem ponta solta.

Do nosso método:
- abertura de cada parágrafo com as palavras da pergunta;
- frase do tema na introdução;
- conclusão que retoma a introdução;
- cada proposta com agente, ação, meio e finalidade, respondendo a um problema levantado no texto;
- norma sem erros e sem gerúndio solto;
- conectivos variados;
- fatos conferidos em fonte.

A parte mensurável foi conferida por duas ferramentas: `ferramentas/revisar_redacao.py` (criada para esta série) e
`ferramentas/verificar_amarracao.py`, com os elos em `*.elos.json`. O resto veio de leitura, rodada a rodada.

## Fatos conferidos

| Fato | Situação | Fonte |
|---|---|---|
| Ibope 2018: 39% dizem não separar o orgânico do reciclável; 66% sabem pouco ou nada sobre coleta seletiva | conferido em fontes secundárias. O "97%" usado antes aparece como 97% ou 98% conforme a fonte e foi retirado | pesquisa Ibope encomendada pela Ambev, maio de 2018 |
| Césio-137, Goiânia, 1987: quatro mortes | conhecido | — |
| Constituição, art. 225, § 1º, VI: promover a educação ambiental e a conscientização pública | conhecido | — |
| Fundação Ellen MacArthur (2017): produção de roupas quase dobrou em 15 anos; uso por peça caiu 36% | conferido em fontes secundárias | A New Textiles Economy |
| CDC, art. 49 (prazo de 7 dias) e art. 32 (peças de reposição) | conhecido | — |
| ONU, Monitor Global de Lixo Eletrônico 2024: 62 milhões de toneladas em 2022; 22,3% reciclados de forma documentada; vida útil mais curta como fator | conferido | UNITAR/ITU |
| OMM: 2024, ano mais quente já registrado | conhecido | — |
| Enchentes do RS, 2024: mais de 180 mortos (182 a 185 conforme o balanço) | conferido | Defesa Civil do RS |
| World Weather Attribution: o aquecimento tornou as chuvas do RS mais de duas vezes mais prováveis | conferido | WWA, junho de 2024 |
| Petrópolis, 2022: mais de 230 mortos (232 a 235 conforme a fonte) | conferido | Agência Brasil |
| Science, 2021 (Thiery e outros): até sete vezes mais ondas de calor extremas para quem nasceu em 2020, com as metas atuais | conferido; o estudo diz "até" | Science |
| SEEG: mudança de uso da terra foi 46% das emissões brutas do Brasil em 2023 | conferido | SEEG, relatório 12 |

## Rodadas

**Rodada 1 (v1).**

Revisão automática:
- lixo: palavras repetidas (saber, coleta seletiva, hábito, cada);
- consumo: duas frases com mais de 40 palavras;
- clima: núcleo 0,90 (faltavam "de que forma" e "são").

Leitura:
- **Lixo**
  - "o erro nasce da falta de informação" afirmava uma causa que o dado não prova sozinho; passou a "esses números mostram que falta informação".
  - "Por isso, a Constituição" usava um conectivo de causa errado; virou "Não por acaso".
  - O aparelho do césio não foi "descartado", e sim "abandonado".
  - Havia duas teses sobre onde está a importância da educação; ficou uma só.
- **Consumo (falha grave)**
  - O lixo eletrônico era atribuído ao "aumento do consumo", o que prova consumo, não consumismo: o mesmo erro do endividamento que a professora apontou. O texto passou a citar a troca mais rápida de aparelhos e a fechar com "trocar um aparelho que ainda funciona".
  - "Principais consequências" tinha uma só; passaram a ser duas (desperdício e contaminação).
  - As propostas não respondiam ao problema do §3 (ponta solta); entrou a das peças de reposição.
  - O fecho "meio e não fim" não tinha base na introdução; a definição foi reescrita com meio e fim.
- **Clima**
  - A tese era fraca ("tornam urgente discutir"); passou a anunciar as duas propostas.
  - Os desastres não tinham prova de ligação com o clima; entrou o estudo de atribuição.
  - "Portanto" aparecia em dois parágrafos.

**Rodada 2 (v2).**
- **Lixo:** passou na revisão automática, mas faltava a dimensão econômica das implicações, e a proposta das
  prefeituras não tinha finalidade.
- **Consumo:** 2.022 caracteres e uma frase longa.
- **Clima:** 2.094 caracteres, e a proposta do Ibama perdeu a finalidade.

**Rodada 3 (v3 e v4).**
- **Lixo:** "Além disso" duas vezes.
- **Clima:** "essa aceleração" no §1 não tinha referente; virou "frear o aquecimento". "A fim de" duas vezes no §5 e
  ainda 2.034 caracteres.

**Rodada 4 (v5 e v6).**
- **Clima:** "segundo", "aquecimento" e "clima" três vezes cada; "puxada pelo desmatamento" é informal.
- **Lixo**
  - A pesquisa é declaratória: os 39% "dizem" não separar.
  - A renda dos catadores (§2) não voltava nas propostas; entrou a coleta seletiva com as cooperativas de
    reciclagem.
  - "Visitam as casas contra a dengue" tinha sentido torto; virou "no combate à dengue".
- **Consumo:** "Essa pausa" não tinha referente; virou "Esse exame".

**Rodada 5 (final).**
- **Lixo**
  - Havia uma frase de 43 palavras e duas conclusões seguidas ("Assim…", "Dessa forma…"); viraram uma frase só.
  - O anúncio das implicações seguia outra ordem; passou a seguir a do desenvolvimento (ambiente, cidade, saúde,
    renda).

Ficou de propósito: no consumo, "compra" e "uso" aparecem três vezes cada. É o fio do argumento (definição →
critério → conclusão).

## Previsões registradas antes do envio (modelo v0.25)

Na plataforma, a Abrangência e o Tangenciamento não acompanharam a qualidade do texto até agora (avaliação 006). Por
isso, a previsão é modesta mesmo para textos sem falhas:

| Texto | G | A | T | Nota online |
|---|---|---|---|---|
| D4 (lixo) | 10,0 | 3,0 (2,8 a 3,2) | 8,7 (± 0,4) | 6,9 (6,7 a 7,1) |
| C4 (consumo) | 10,0 | 2,5 (2,4 a 2,7) | 8,7 (± 0,4) | 6,7 (6,6 a 6,9) |
| M8 (clima) | 10,0 | 2,8 (2,4 a 3,2) | 8,7 (± 0,4) | 6,9 (6,6 a 7,1) |

Pela rubrica (nota pelo critério do simulador), os três tiram 10.

Como ler:
- **A acima de 3,2:** pela primeira vez a qualidade do texto teria movido a Abrangência.
- **A dentro da faixa:** reforça que ela depende do tema, e não do texto.
- **Envio idêntico ao de outro dia:** serve também como reteste (X0).

## Resultados

| Data | Tema | Texto | G | A | T | E | Nota online | Observações |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
