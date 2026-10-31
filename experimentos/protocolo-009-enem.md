# Protocolo 009 — redações no padrão de nota mil do ENEM, começando por repertório

Registrado em 2026-10-31, antes de qualquer envio. Pedido do usuário, a partir da série 008:
- não abrir o texto repetindo o tema, mas com um repertório;
- tudo amarrado: parágrafos, frases e ideias;
- padrão de nota mil no ENEM.

Use os textos **só no simulador**.

| Tema | Texto final | Caracteres (como a plataforma conta) | Elos |
|---|---|---|---|
| Descarte correto do lixo | `experimentos/textos/D5-lixo-enem.txt` | 1.993 | 12 de 12 |
| Consumo e consumismo | `experimentos/textos/C5-consumo-enem.txt` | 1.989 | 12 de 12 |
| Mudanças climáticas | `experimentos/textos/M9-clima-enem.txt` | 1.984 | 12 de 12 |

As versões intermediárias (v1 a v7) estão em `experimentos/textos/serie-009/`.

## O que mudou em relação à série 008

- **Abertura por repertório**, retomado na conclusão:
  - lixo: o césio-137 em Goiânia (1987) → "a informação que faltou em Goiânia chegará a cada lar";
  - consumo: a Fundação Ellen MacArthur e as roupas → "roupas e aparelhos voltarão a ser comprados para durar";
  - clima: o recorde de calor de 2024 e as chuvas no RS → "o recorde de 2024 deixará de anunciar um futuro mais quente".
- **Projeto de texto do ENEM:** a introdução responde à 1ª pergunta e anuncia os argumentos; cada desenvolvimento
  responde a uma pergunta; a conclusão traz as propostas e volta ao repertório. No clima, as perguntas 3 e 4 ficam
  no mesmo parágrafo, ligadas por causa: as emissões que se acumulam comprometem as próximas gerações. Com 2.000
  caracteres, cinco parágrafos deixavam cada argumento raso.
- **Frases amarradas:** cada frase se prende à anterior por um conectivo ("Embora", "Isso porque", "Por isso",
  "Desse modo", "Em primeiro lugar", "Além disso") ou por uma retomada ("esse episódio", "essas implicações", "esse
  critério", "aquelas enchentes", "tais efeitos"). O mesmo vale para a 1ª frase de cada parágrafo.

## Ferramenta

`ferramentas/revisar_redacao.py` ganhou duas verificações:
- se a primeira frase traz um repertório;
- frases soltas: cada frase deve começar com um conectivo ou uma retomada.

Aplicada às redações da série 008, ela acusa 7 frases soltas na de lixo, o que confirma a crítica do usuário.

## Rodadas

| Rodada | Falhas encontradas (automáticas e de leitura) | Correção |
|---|---|---|
| v1 | 2.194 a 2.393 caracteres; frase-tese do lixo com mais de 40 palavras; no lixo, as palavras da 3ª pergunta não apareciam no parágrafo dela; três parágrafos sem conectivo na 2ª frase; "Além disso" e "Assim" repetidos | Clima passa a 4 parágrafos; conectivos e retomadas em todas as frases |
| v2 | Ainda 2.097 a 2.111 caracteres; quatro frases com mais de 40 palavras; "Goiânia" três vezes | Frases divididas; a retomada do césio fica só no §2 e no fim |
| v3 a v5 | Cortes até caber em 2.000 sem perder elos; "segundo" três vezes no consumo; "lixo" quatro vezes no §2 do lixo | Variação vocabular ("resíduos", "embalagens") |
| v6 | Leitura no padrão ENEM: "lixo" duas vezes na mesma frase-tese; "com deslizamentos em encostas com moradias" (dois "com"); "foram 62 milhões" (faltava o particípio); "persiste séculos no ar" | "os resíduos"; "ocupadas por"; "foram geradas"; "persiste por séculos" |
| v7 | Margem para digitação (o clima tinha 2.000 exatos); "a define", introduzido no corte, ficou ambíguo (podia ser "a família"); "Tal resíduo desperdiça" atribuía ao lixo inteiro o que vale para a parte não reciclada | De 1.984 a 1.993 caracteres; "define essa educação"; "O restante desperdiça" |

Ficaram de propósito:
- No lixo, o §2 não traz número: desenvolve as implicações pelo mecanismo e se ancora no repertório do césio.
- No consumo, "compra" aparece três vezes porque é o fio do argumento.

## Autoavaliação pela grade do ENEM

| Competência | Avaliação | Por quê |
|---|---|---|
| C1 (norma) | 200 | Nenhum desvio encontrado em duas leituras; sem gerúndio solto; regência ("chegar aonde"), crase e concordância conferidas |
| C2 (tema e repertório) | 200 | Tema completo e sem tangenciar; repertório legitimado, pertinente e produtivo, que abre o texto e volta na conclusão; nenhum repertório de bolso |
| C3 (projeto de texto) | 200 | Introdução que anuncia os argumentos; cada desenvolvimento defende uma ideia com prova; nenhuma ponta solta (todos os elos fecham) |
| C4 (coesão) | 200 | Conectivos entre todos os parágrafos e entre as frases, sem repetição; retomadas sem ambiguidade |
| C5 (intervenção) | 200 | Duas propostas por texto, a primeira com agente, ação, meio, finalidade e detalhamento, ligadas aos problemas discutidos |

Esta é uma autoavaliação. Corretores do ENEM divergem (o próprio Inep aceita até 100 pontos de diferença na nota
total antes de chamar um terceiro), então ninguém garante mil. O limite de 2.000 caracteres também deixa o texto mais
curto que uma redação típica do ENEM, o que exige desenvolvimento enxuto.

## Previsões na plataforma (modelo v0.25), registradas antes do envio

| Texto | G | A | T | Nota online |
|---|---|---|---|---|
| D5 (lixo) | 10,0 | 3,0 (2,8 a 3,2) | 8,7 (± 0,4) | 6,9 (6,7 a 7,1) |
| C5 (consumo) | 10,0 | 2,5 (2,4 a 2,7) | 8,6 (± 0,4) | 6,7 (6,6 a 6,9) |
| M9 (clima) | 10,0 | 2,8 (2,4 a 3,2) | 8,7 (± 0,4) | 6,9 (6,6 a 7,1) |

## Resultados

| Data | Tema | Texto | G | A | T | E | Nota online | Observações |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
