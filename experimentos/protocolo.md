# Protocolo experimental — série 001 (tema "Descarte correto do lixo")

Previsões registradas em 2026-10-16, **antes** de qualquer resultado. Não edite as previsões depois de ver os
resultados: anote o resultado na tabela do experimento e a comparação no `modelo/registro.md`.

- Textos prontos para submissão: `experimentos/variantes/*.txt`.
- Mudanças exatas de cada variante: `experimentos/variantes/MUDANCAS.md` (gerado por `ferramentas/gerar_variantes.py`).

## Regras de execução

1. **Mesma proposta, mesmo método.** Submeta todas as variantes contra a mesma proposta (mesmo tema e enunciado) e
   pelo mesmo caminho (mesma tela, mesmo navegador, colando o texto da mesma forma).
   - Se a plataforma trocar o tema a cada tentativa, pare e registre o fato: a comparação entre variantes deixa de ser
     controlada.
2. **Verifique antes se as tentativas contam oficialmente.** Algumas plataformas limitam o número de tentativas ou
   consideram a última. Se houver risco, prefira um modo de simulado ou treino.
3. **Comece pelo X0.** Se as notas variarem no reteste, repita cada variante pelo menos 2 vezes e compare médias.
   Diferenças menores que a amplitude observada no X0 não contam como efeito.
4. **Registre tudo**, cada vez: os seis campos, o status textual, comentários e marcações, a contagem de caracteres
   exibida, a data e hora e o número da tentativa.
5. **Confira os fatos de X3 antes de submeter.** Se o avaliador punir erro factual, um fato errado confunde o teste.
   Os três fatos usados foram escolhidos por serem amplamente documentados:
   - o prazo de 2014 para a disposição final adequada (art. 54 da Lei 12.305/2010), prorrogado pela Lei 14.026/2020;
   - a reprodução do Aedes aegypti em água parada;
   - o acidente com o césio-137 em Goiânia, em 1987.

## Modelos sob teste

| ID | Modelo |
|---|---|
| M1 | nota online = trunc₀,₁((G + A + T)/3) |
| M4 | nota online = (G + A + T − 0,05·E)/3 |
| MG1 | G = 10 − 0,025·E |
| MG2 | G = arred₀,₁(10·(1 − E/palavras)) |
| H-A1 a H-A8 | hipóteses sobre a Abrangência (ver `relatorios/001-analise-inicial.md`, §3.2) |
| P-A5 / P-N7 / P-OUT | portões da Nota Final: zera se A < 5 / zera se nota online < 7 / causa externa às notas |

Premissa das previsões numéricas: o que a variante não muda permanece igual à base (G 9,9; A 3,0; T 7,1; E 4).

---

## X0 — Teste-reteste

| | |
|---|---|
| Hipótese | o avaliador é determinístico |
| Variável | nenhuma |
| Mudança | texto idêntico à base |
| Notas que podem mudar | todas, se o avaliador for estocástico |

Interpretação dos resultados:
- **Confirma:** notas idênticas em 2 ou mais repetições.
- **Enfraquece:** qualquer diferença. A amplitude observada vira o limiar de ruído para todos os outros experimentos.
  - Se a nota online variar, mas continuar igual a M1 calculada sobre as novas notas parciais, a fórmula ganha apoio e
    o ruído está nos critérios.
  - Se não continuar, M8 (nota holística) ganha apoio.

| Repetição | Nota Final | G | A | T | E | Nota online | Status/obs. |
|---|---|---|---|---|---|---|---|
| base | 0,00 | 9,90 | 3,00 | 7,10 | 4,00 | 6,60 | — |
| 1 | | | | | | | |
| 2 | | | | | | | |

## X1a / X1b — Dose-resposta de erros gramaticais

| | |
|---|---|
| Hipótese | E conta erros; G deriva de E (MG1 ou MG2); E não entra diretamente na nota online (M1 contra M4) |
| Variável | número de erros inequívocos inseridos: X1a +4 (crase, 2 de concordância verbal, acentuação); X1b +12 (inclui os 4 de X1a) |
| Mudança | `MUDANCAS.md`, seções X1a e X1b; a extensão fica praticamente constante |
| Notas que podem mudar | E e G; A e T só se o LLM avaliar de forma holística |

Previsões:

| | E | G (MG1) | G (MG2) | Nota online (M1) | Nota online (M4) |
|---|---|---|---|---|---|
| X1a | 8 | 9,8 | 9,7 | 6,6 (com MG2: 6,6 em aritmética exata, 6,5 se o sistema truncar em ponto flutuante) | 6,5 (com MG1) / 6,4 (com MG2) |
| X1b | 16 | 9,6 | 9,4 | 6,5 | 6,3 (com MG1) / 6,2 (com MG2) |

Interpretação dos resultados:
- **E = 4 + k** confirma que E é uma contagem.
- **E diferente de 4 + k:** E é outra coisa, ou o avaliador não detectou todos os erros (anote quantos detectou).
- **G no valor de MG1 ou de MG2** favorece esse modelo.
- **G = 9,9 com E maior** indica que G não deriva de E.
- **Nota online no valor de M4** mostra que E entra na média.
- **A ou T mudando** revela contaminação holística: a gramática afeta os outros critérios.

Limitação: a diferença entre MG1 e MG2 em X1a é de 0,1 ponto, do tamanho de um possível ruído. X1b separa os
modelos com folga maior.

| Variante | Nota Final | G | A | T | E | Nota online | Status/obs. |
|---|---|---|---|---|---|---|---|
| X1a | | | | | | | |
| X1b | | | | | | | |

## X2 — Eliminação dos possíveis falsos positivos

| | |
|---|---|
| Hipótese | os 4 apontamentos correspondem a trechos corretos marcados como erro (falsos positivos) |
| Variável | reescrita dos 5 trechos suspeitos: "Apesar de a", "embalagens abandonados", "isoladamente, não conseguem.", "o seu descarte", "Ao cidadão, compete" |
| Mudança | `MUDANCAS.md`, seção X2 (+0,2% de extensão) |
| Notas que podem mudar | E e G |

Previsões:
- **Se a hipótese estiver certa:** E entre 0 e 1; G = 10,0 (MG1 e MG2); nota online = trunc₀,₁((10 + 3 + 7,1)/3) = **6,7**
  (M1; M4 dá o mesmo valor).
- **Se E não mudar:** os apontamentos estão em outros trechos ou não são erros de norma.

Interpretação dos resultados: compare qual reescrita reduziu E. Se a plataforma mostrar as marcações, anote quais trechos estavam marcados.

| Variante | Nota Final | G | A | T | E | Nota online | Status/obs. |
|---|---|---|---|---|---|---|---|
| X2 | | | | | | | |

## X3, X4, X5 — O que a Abrangência mede (fatos, profundidade, extensão)

O trio funciona em conjunto. As três variantes acrescentam praticamente a mesma extensão (+18,3% a +19,8%). Assim,
diferenças de A entre elas não se explicam pela extensão.

| Variante | O que acrescenta | Onde | Δ extensão |
|---|---|---|---|
| X3 | 3 fatos verificáveis, sem raciocínio novo | P1 e P2 | +18,5% |
| X4 | 2 frases de raciocínio novo (mecanismo e exemplo), sem fatos | P3 | +19,8% |
| X5 | 2 frases redundantes, sem ideia nem fato novo (controle) | P3 | +18,3% |

Previsões de A, sem valores pontuais, apenas a ordem esperada:

| Hipótese | X3 | X4 | X5 | Padrão esperado |
|---|---|---|---|---|
| H-A3 (fatos) | sobe muito | ≈ | ≈ | X3 ≫ X4 ≈ X5 ≈ 3,0 |
| H-A2 (profundidade) | sobe pouco | sobe | ≈ | X4 > X3 > X5 ≈ 3,0 |
| H-A4 (extensão) | sobe | sobe | sobe | X3 ≈ X4 ≈ X5 > 3,0 |
| H-A1 (cobertura das perguntas) | ≈ | ≈ | ≈ | nada muda |
| H-A5 (gabarito de tópicos) | sobe se os fatos tocarem tópicos esperados | depende | ≈ | imprevisível sem o gabarito |
| H-A8 (ruído) | — | — | — | diferenças dentro da amplitude de X0 |

Previsões de T:
- **X4:** sobe se T medir o desenvolvimento substantivo do recorte.
- **X5:** sobe se T medir a proporção de menções ao recorte. Na contagem por palavras-chave, X5 tem *mais* menções
  (44% dos caracteres) que X4 (35%).
- **X3:** T tende a ficar igual ou a cair, porque a parte sobre o assunto amplo cresce.

Portão da Nota Final:
- Se alguma variante levar A a 5 ou mais, mantendo a nota online abaixo de 7, uma Nota Final diferente de zero apoia
  P-A5 e enfraquece P-N7.
- Se a Nota Final continuar zero, P-A5 fica enfraquecida.

| Variante | Nota Final | G | A | T | E | Nota online | Status/obs. |
|---|---|---|---|---|---|---|---|
| X3 | | | | | | | |
| X4 | | | | | | | |
| X5 | | | | | | | |

## X6 — Tese que nomeia o recorte

| | |
|---|---|
| Hipótese | T mede se a tese (introdução) nomeia o recorte "educação e conscientização" |
| Variável | apenas a última frase do P1, que passa a afirmar que educação e conscientização são indispensáveis |
| Mudança | `MUDANCAS.md`, seção X6 (+5,8% de extensão); a primeira menção ao recorte passa de 57% para 27% do texto |
| Notas que podem mudar | T, principalmente |

Previsões:
- **Se a hipótese estiver certa:** T sobe claramente, acima do ruído de X0. A, G e E ficam iguais.
- **Nota online (M1):** a cada 0,3 ponto de aumento em T, sobe 0,1. Exemplo: T = 8,0 dá trunc₀,₁((9,9 + 3 + 8)/3) = 6,9.
- **Se T não mudar:** T não depende da tese, mas da proporção ou do desenvolvimento do recorte (compare com X4 e X7).

| Variante | Nota Final | G | A | T | E | Nota online | Status/obs. |
|---|---|---|---|---|---|---|---|
| X6 | | | | | | | |

## X7 — Cobertura das perguntas com extensão constante

| | |
|---|---|
| Hipótese | A mede a cobertura das perguntas orientadoras (H-A1) |
| Variável | o parágrafo das implicações (pergunta 2) é trocado por outro de extensão semelhante sobre educação, sem fatos novos; a cobertura cai de 4 para 3 perguntas |
| Mudança | `MUDANCAS.md`, seção X7 (−1,7% de extensão). Remover o P2 sem reposição deixaria o texto com ~1.140 caracteres sem espaços, abaixo do mínimo. |
| Notas que podem mudar | A e T |

Previsões:
- **H-A1:** A cai.
- **H-A4 (extensão):** A fica igual.
- **H-A3 (fatos):** A fica igual (o P2 original não tinha fatos verificáveis).
- **T:** sobe se medir a proporção do recorte, que passa de 34% para 52–61% do texto.
- **Se A subir:** A premia a concentração no recorte, ou seja, mede algo próximo de T. Nesse caso, investigue a
  redundância entre os dois critérios.

| Variante | Nota Final | G | A | T | E | Nota online | Status/obs. |
|---|---|---|---|---|---|---|---|
| X7 | | | | | | | |

---

## Matriz do portão da Nota Final

Preencha ao longo dos experimentos. Cada linha observada elimina as regras incompatíveis.

| Observação | A | Nota online | Nota Final | P-A5 prevê | P-N7 prevê | P-OUT prevê |
|---|---|---|---|---|---|---|
| base | 3,0 | 6,6 | 0,00 | 0 | 0 | 0 |
| | | | | | | |
