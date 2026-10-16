# Protocolo experimental — série 001 (tema "Descarte correto do lixo")

Previsões registradas em 2026-10-16, **antes** de qualquer resultado. Não edite as previsões depois de ver os
resultados: anote o resultado na tabela do experimento e a comparação no `modelo/registro.md`.

Revisão 2 (2026-10-16, ainda antes de qualquer resultado): foi informado o limite máximo de 2.000 caracteres. As
versões anteriores de X3, X4, X5 e X8 passavam do limite e foram refeitas; as previsões abaixo valem para as versões
novas.

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
5. **Confira os fatos de X3 e X8 antes de submeter.** Se o avaliador punir erro factual, um fato errado confunde o
   teste. Os fatos usados foram escolhidos por serem amplamente documentados:
   - Abrelpe (2022): cerca de 4% dos materiais com potencial de reciclagem são reciclados no Brasil;
   - Constituição Federal, art. 225, § 1º, VI: o poder público deve promover a educação ambiental e a conscientização
     pública;
   - a reprodução do Aedes aegypti em água parada;
   - o acidente com o césio-137 em Goiânia, em 1987;
   - a limpeza das escolas pelos próprios alunos no Japão.
6. **Limite de 2.000 caracteres.** Todas as variantes cabem nele contando espaços e quebras de parágrafo;
   `ferramentas/gerar_variantes.py` recusa gerar qualquer variante que passe do limite.

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

O trio funciona em conjunto. As três variantes acrescentam praticamente a mesma extensão (+4,9% a +5,2%, cerca de
90 caracteres). Assim, diferenças de A entre elas não se explicam pela extensão.

| Variante | O que acrescenta | Onde | Δ extensão |
|---|---|---|---|
| X3 | 1 dado com fonte (Abrelpe, 4%), sem raciocínio novo | P1 | +5,2% |
| X4 | 1 frase de raciocínio novo (efeito multiplicador da escola), sem fatos | P3 | +5,2% |
| X5 | 1 frase redundante, sem ideia nem fato novo (controle) | P3 | +4,9% |

Com o limite de 2.000 caracteres, a base só tinha 156 caracteres de folga. Por isso cada variante muda uma única
frase. O efeito esperado é menor que nas versões anteriores, e a chance de ele ficar dentro do ruído é maior: repita
cada variante se o X0 mostrar variação.

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
- **X5:** sobe se T medir a proporção de menções ao recorte. Na contagem por palavras-chave, X4 e X5 ficam iguais
  (37% dos caracteres, contra 34% na base), então T-prop prevê X4 ≈ X5, e o desenvolvimento substantivo prevê X4 > X5.
- **X3:** T tende a ficar igual ou a cair, porque a parte sobre o assunto amplo cresce (recorte em 32%).

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

## X8 — Versão otimizada para a rubrica v0.1 (controle positivo, várias variáveis)

| | |
|---|---|
| Hipótese | a rubrica v0.1 aponta corretamente o que eleva as notas: recorte na tese e em todos os parágrafos (T), fatos com fonte, mecanismo e exemplo (A), ausência das construções propensas a falso positivo (G) |
| Variável | **várias ao mesmo tempo**: texto reescrito. Um ganho não identifica qual mudança o causou; o objetivo é testar a rubrica como um todo e o portão da Nota Final |
| Texto | `experimentos/textos/X8-otimizada.txt` (escrito a partir da rubrica, não gerado pelo script de variantes) |
| Notas que podem mudar | todas |

Medidas do texto, comparadas com a base:

| Indicador | Base (001) | X8 |
|---|---|---|
| Caracteres com espaços / sem espaços | 1.841 / 1.564 | 1.974 / 1.666 (1.977 contando as quebras) |
| Palavras / parágrafos / frases | 281 / 4 / 14 | 312 / 4 / 13 |
| Primeira menção ao recorte | 57% do texto | 4,0% |
| Frases sobre o recorte | 4/14 (34% dos caracteres) | 8/13 (69%) |
| Parágrafos que retomam o recorte | 2 de 4 | 4 de 4 |
| Parágrafo do núcleo (importância da educação) | 2 frases | 4 frases, com mecanismo e exemplo |
| Fatos verificáveis | 1 | 5 (CF art. 225; Abrelpe, 4%; Aedes aegypti; Goiânia 1987; escolas japonesas), 1 com fonte nomeada além da própria Constituição |
| Construções propensas a falso positivo | 5 | 0 |

Avaliação pela rubrica v0.1, feita antes de qualquer resultado real:

| Critério | Nota pela rubrica | Fundamento | Confiança |
|---|---|---|---|
| Gramática | 10,0 (faixa 9,9–10,0) | nenhum desvio inequívoco encontrado; E previsto de 0 a 2. Possíveis apontamentos de estilo: "recicla … reciclagem", "Aedes aegypti" sem itálico (impossível em texto puro) | média |
| Tangenciamento | 9–10 | cumpre o descritor ≥ 9: recorte nomeado na tese e retomado nos 4 parágrafos; o P2 trata do assunto amplo (28%), mas fecha ligando-o à falta de informação | baixa (só a âncora 7,1 foi observada) |
| Abrangência | ≥ 7, sem valor pontual | não cumpre nenhuma condição da faixa baixa; cumpre a hipótese de trabalho da faixa alta em 3 dos 4 aspectos. A pergunta 4 (ações) não traz fato nem exemplo que sustente a eficácia das medidas. Pela H-A5, faltam tópicos possivelmente esperados: redução do consumo, logística reversa, aterro sanitário, a Política Nacional de Resíduos Sólidos e o papel dos catadores na reciclagem (o corte para 2.000 caracteres tirou os dois últimos) | baixa |
| Nota online (M1) | 8,6 a 10,0 | trunc₀,₁((10 + ≥7 + 9 a 10)/3) | baixa |
| Nota online se a Abrangência continuar 3,0 | 7,3 a 7,6 | trunc₀,₁((10 + 3 + 9 a 10)/3) | — |

O que cada resultado significaria:
- **A alta (≥ 7) e T ≥ 9:** a rubrica v0.1 aponta na direção certa, sem identificar qual componente pesou. Os experimentos X3 a X7 separam os componentes.
- **A continuar baixa (< 5):** H-A2, H-A3 e H-A4 ficam enfraquecidas em conjunto; H-A5 (gabarito) ou H-A8 (ruído) ganham peso.
- **T sem subir:** T-tese e T-prop ficam enfraquecidas.
- **Portão:** em todos os cenários a nota online fica acima de 7, então P-N7 prevê Nota Final diferente de zero. Se A ficar abaixo de 5 e a Nota Final continuar 0,00, P-N7 fica refutada e P-A5 (ou P-OUT) ganha apoio; se a Nota Final passar a valer a nota online com A abaixo de 5, P-A5 fica refutada.

Aviso de circularidade: a avaliação acima foi feita por quem escreveu o texto e a rubrica. Ela mostra que a rubrica é aplicável, mas não que é válida. Validação exige um avaliador que não conheça a intenção do texto: a plataforma real, ou uma sessão nova de um LLM que receba só a proposta, o texto e os nomes dos critérios.

| Variante | Nota Final | G | A | T | E | Nota online | Status/obs. |
|---|---|---|---|---|---|---|---|
| X8 | | | | | | | |

---

## Matriz do portão da Nota Final

Preencha ao longo dos experimentos. Cada linha observada elimina as regras incompatíveis.

| Observação | A | Nota online | Nota Final | P-A5 prevê | P-N7 prevê | P-OUT prevê |
|---|---|---|---|---|---|---|
| base | 3,0 | 6,6 | 0,00 | 0 | 0 | 0 |
| | | | | | | |
