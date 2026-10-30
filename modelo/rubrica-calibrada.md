# Rubrica calibrada v1: critérios com teto 10 que reproduzem as notas reais

Retrato de 2026-10-30. Aplicação e conferência: `python3 ferramentas/rubrica_calibrada.py`.

Objetivo: critérios de correção em que cada nota vai até 10 e que, aplicados por nós às cinco provas reais,
reproduzam exatamente as notas exibidas. Resultado: **G, A, T e nota online batem nas cinco provas (20 de 20)**.

Aviso de método. São 5 provas, e algumas regras foram acrescentadas justamente para acertar uma prova específica
(seção 5). Acertar as cinco era, em parte, garantido pela construção. O teste real são as previsões da seção 6,
registradas antes dos envios.

## 1. Gramática (teto 10)

G = arred₀,₁(10 × (1 − n ÷ W))

- **n** = apontamentos de erro gramatical + 1,5 × erros de ortografia.
- **W** = palavras dentro dos primeiros 2.000 caracteres.

| Prova | Apontamentos (plataforma) | Ortografia (minha contagem) | W | G previsto | G real |
|---|---|---|---|---|---|
| 001 | 4 | 0 | 281 | 9,9 | 9,9 |
| 002 | 7 | 0 | 266 | 9,7 | 9,7 |
| 003 | 0 | 6 (inpulso, quicições, estração, obsjetos, empregradaos, compar) | 252 | 9,6 | 9,6 |
| 004 | 1 | 0 | 290 | 10,0 | 10,0 |
| 005 | 2 | 0 | 298 (o texto passa de 2.000) | 9,9 | 9,9 |

Para tirar 10: nenhum erro de ortografia e nenhuma construção que o corretor aponte. Com cerca de 300 palavras, um
apontamento ainda dá 10,0, mas dois já derrubam para 9,9.

Limites:
- Os apontamentos vêm da plataforma. Minha contagem própria de gramática bate com a 001 e a 004, mas não com a 002 (a
  plataforma apontou 7 marcas num texto quase limpo) nem com a 003 (0 apontamentos, apesar de "guiado" e "em si
  mesmo" estarem errados).
- Ler só os primeiros 2.000 caracteres é o que faz a 005 bater. Sem isso, ela daria 10,0.

## 2. Abrangência (teto 10 na nota bruta)

**Descoberta.** As cinco Abrangências são múltiplos de 0,2 (3,0; 3,2; 2,4; 2,4; 2,8). Se os décimos fossem
aleatórios, isso aconteceria cerca de 1 vez em 32. Divididas por 0,4, elas dão 7,5; 8; 6; 6; 7: notas redondas, do
tipo que um corretor dá a redações boas.

Hipótese **H-A-esc**: a plataforma exibe 0,4 × a nota bruta de Abrangência. O 0,4 coincide com o peso da Abrangência
na nota online, o que sugere que o peso é aplicado duas vezes.

Nota bruta = 10 menos os descontos:

| Desconto | Valor |
|---|---|
| Parágrafo sem evidência concreta e pertinente | −0,5 por parágrafo |
| Recorte do tema ausente da introdução | −1 |
| Dado ou argumento que não prova o que afirma (ex.: endividamento como prova de consumismo) | −2 cada |
| Dado vago usado como prova (sem número ou sem fonte precisa) | −1 cada |
| Repertório de bolso (Bauman, Freire, Jonas, Kant, Platão, "modernidade líquida"…) | −1 cada |

O que conta como evidência concreta:
- dado com número e fonte;
- fato identificado (lugar e data);
- lei ou política nomeada;
- no parágrafo de propostas, um órgão específico nomeado como agente (Ministério da Educação, por exemplo).
  "Escolas", "prefeituras", "poder público", "governo" e "empresas" são genéricos e não contam.

Repertório de bolso e dado que não prova a afirmação não contam como evidência.

| Prova | Descontos | Bruta | × 0,4 | Real |
|---|---|---|---|---|
| 001 | §2, §3 e §4 sem evidência (−1,5); introdução sem educação nem conscientização (−1) | 7,5 | 3,0 | 3,0 |
| 002 | os 4 parágrafos sem evidência (−2) | 8,0 | 3,2 | 3,2 |
| 003 | os 4 parágrafos sem evidência (−2); "Além do endividamento" (−2) | 6,0 | 2,4 | 2,4 |
| 004 | §1 só tem Bauman e §2 só tem o dado da CNC (−1); CNC como prova de consumismo (−2); Bauman (−1) | 6,0 | 2,4 | 2,4 |
| 005 | §1 sem evidência e §3 só com Freire (−1); Panorama "milhões de toneladas" (−1); Freire (−1) | 7,0 | 2,8 | 2,8 |

Para tirar 10:
- cada parágrafo com um dado, fato, lei ou órgão que prove exatamente o que o parágrafo afirma;
- o recorte do tema na introdução;
- nenhum dado vago, nenhum dado fora do ponto e nenhum repertório de bolso.

É o método da professora.

**Consequência, se H-A-esc estiver certa:**
- a Abrangência exibida vai no máximo a 4,0;
- a nota online vai no máximo a 0,4 × 10 + 0,4 × 4 + 0,2 × 10 = **7,6**.

A nota pelo critério (com a Abrangência bruta) continua indo a 10.

## 3. Tangenciamento (teto 10)

T = arred₀,₁(10 − descontos)

| Desconto | Valor |
|---|---|
| Palavras da frase do tema ausentes do texto | −3 × fração ausente |
| Pares de palavras da frase do tema ausentes | −0,8 × fração ausente |
| Palavras da frase do tema ausentes da introdução | −0,25 × fração ausente |
| Último parágrafo sem a frase do tema completa e literal | −1,05 |

| Prova | Palavras / pares / introdução / conclusão | T previsto | T real |
|---|---|---|---|
| 001 | 0,67 / 0,17 / 0,17 / não | 7,1 | 7,1 |
| 002 | 1,00 / 0,83 / 0,67 / não | 8,7 | 8,7 |
| 003 | 1,00 / 0,55 / 0,50 / não | 8,5 | 8,5 |
| 004 | 0,67 / 0,45 / 0,67 / não | 7,4 | 7,4 |
| 005 | 1,00 / 1,00 / 1,00 / não | 9,0 | 9,0 |

**O último desconto é hipótese (H-T-conc).** Nenhuma prova tinha a frase do tema completa no último parágrafo, e
nenhuma passou de 9,0. Pus nele o ponto que falta para o teto 10. O texto M6 tem a frase completa no último parágrafo
e vai testar isso.

## 4. Nota online e nota pelo critério

- Nota online (plataforma) = arred₀,₁(0,4·G + 0,4·A exibida + 0,2·T). Bate 5 de 5.
- Nota pelo critério = arred₀,₁(0,4·G + 0,4·A bruta + 0,2·T). Vai até 10. Nas cinco provas: 8,4; 8,8; 7,9; 7,9; 8,6.

## 5. Critérios testados no caminho

| # | Critério | Resultado |
|---|---|---|
| 1 | A pelo vocabulário da proposta (H-A9) | refutado pela 005 (previu 4,2; deu 2,8) |
| 2 | A pela base do tema | reproduz as notas, mas não tem teto 10 nem diz como subir; descartado como critério |
| 3 | A pela rubrica híbrida, que premia dados e repertório | ordem invertida: a 004 (com dados) e a 005 (com lei) teriam mais que a 002 (sem nada) |
| 4 | Descontos sem exigir pertinência da evidência | 004 = 6,5 (deu 6,0); corrigido exigindo que a evidência prove a afirmação |
| 5 | Sem o desconto de dado vago | 005 = 8,0 (deu 7,0); desconto incluído por causa da 005 |
| 6 | Sem o desconto do recorte fora da introdução | 001 = 8,5 (deu 7,5); desconto incluído por causa da 001 |
| 7 | T pela fórmula anterior (4,94 + 2,96·tema + 1,05·pares) | 002 daria 8,8 (deu 8,7); acrescentado o termo da introdução |
| 8 | G com os apontamentos e o texto inteiro | 005 daria 10,0 (deu 9,9); incluído o corte em 2.000 caracteres |
| 9 | G com peso 1 ou 2 para a ortografia | 003 daria 9,8 ou 9,5 (deu 9,6); peso 1,5 |

Os descontos 5 e 6 e o peso da ortografia vêm, cada um, de uma única prova. São as partes mais frágeis.

## 6. Previsões registradas antes do envio (série 005)

| Texto | G | A bruta | A exibida | T | Nota online | Nota pelo critério |
|---|---|---|---|---|---|---|
| D2 (lixo) | 10,0 | 10 | 4,0 | 9,0 | 7,4 | 9,8 |
| C2 (consumo) | 10,0 | 9,5 (§1 sem evidência) | 3,8 | 8,9 | 7,3 | 9,6 |
| M6 (clima) | 10,0 | 9,5 (§4 com agentes genéricos) | 3,8 | 10,0 (H-T-conc) | 7,5 | 9,8 |

G supõe nenhum apontamento; cada apontamento a mais pode tirar 0,1.

Como ler o resultado:
- **A de 3,6 a 4,0** apoia a rubrica e H-A-esc.
- **A de 2,4 a 3,2** (a base do tema) refuta a rubrica de Abrangência.
- **A acima de 4,0** refuta H-A-esc e o teto de 7,6.
- **Qualquer A em décimo ímpar** (2,9, 3,3…) refuta a escala de 0,2.
- **T do M6 perto de 10** apoia H-T-conc; perto de 9,0, a refuta.
