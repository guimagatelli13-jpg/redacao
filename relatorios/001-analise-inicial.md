# Relatório 001 — Engenharia reversa do avaliador "Redação Online"

- **Base empírica:** 1 avaliação (n = 1), tema "Descarte correto do lixo".
- **Documentação oficial da plataforma localizada:** nenhuma.
- **Status da rubrica:** parcial e provisória (v0.1).

Legenda de classificação:
- **[C]** confirmado (demonstrado pelos dados ou por aritmética sobre eles);
- **[IF]** inferência forte;
- **[H]** hipótese exploratória.

Quando cabe, o rótulo traz um grau de confiança (alta/média/baixa). Os números citados podem ser reproduzidos com `python3 ferramentas/testar_modelos.py` e `python3 ferramentas/gerar_variantes.py`.

---

## 1. Resumo executivo

1. **Não há documentação pública da plataforma.** Busquei os nomes exatos dos campos ("Nota do Tangenciamento (Fuga)", "Nota da Abrangência da Redação Online", "Apontamento de erro gramatical", "Nota Final da Redação Online") e o enunciado da proposta. Não encontrei manual, edital nem descrição do sistema. Tudo o que segue é inferido do comportamento observado, com n = 1, e nada da rubrica está confirmado por documento.

2. **A nota online é reproduzida exatamente pela média simples com truncamento** [H, confiança média]:
   trunc₀,₁((9,90 + 3,00 + 7,10) / 3) = trunc₀,₁(6,667) = **6,6**.
   - Com arredondamento comum, a mesma média dá 6,7.
   - O arredondamento só fica compatível se as notas exibidas forem arredondamentos de valores internos cuja soma esteja em [19,85; 19,95).
   - A média truncada é o melhor candidato por parcimônia, e não por identificação.

3. **A fórmula não é identificável com uma observação.**
   - Numa grade de pesos com passo de 0,05, 5 vetores reproduzem 6,60 com truncamento e 6 com arredondamento.
   - Com pesos contínuos, o conjunto compatível é uma faixa: wG ∈ [0; 0,54], wA ∈ [0,10; 0,48], wT ∈ [0; 0,90].
   - Único resultado robusto: se a nota online é uma média ponderada de G, A e T, **a Abrangência tem peso positivo (≥ ~10%)**, porque 6,6 é menor que G e T [C, condicional ao modelo de média].

4. **O "Apontamento de erro gramatical" (4,00) não é necessário para reproduzir a nota online** [IF, média].
   - O único modelo exato que o inclui exige um coeficiente ad hoc (−0,05 por apontamento).
   - É o único campo sem a palavra "Nota" no nome, e a formatação com duas casas é genérica (até o zero aparece como "0,00").
   - Leitura mais provável: contagem de 4 ocorrências apontadas [H].
   - Se ele alimenta a Gramática, cada apontamento custa ~0,025–0,036 ponto em G: G = 10 − 0,025·E = 9,9, ou G = 10·(1 − E/281 palavras) = 9,86 → 9,9.

5. **"Nota Final" (0,00) e "Nota Final da Redação Online" (6,60) não são a mesma grandeza** [C], ou pelo menos uma não é cópia da outra no momento observado.
   - O zero não sai da fórmula das notas parciais: é um portão de eliminação ou um campo de outro nível, como o processo seletivo ou um status [IF].
   - Não bastam, sozinhas, como explicação: "Nota Final = nota online", "zera se algum critério = 0", "zera só por fuga total" e "zera se nota online < 5 ou < 6".
   - Continuam compatíveis:
     - nota mínima global acima de 6,6 (ex.: 7,0);
     - nota mínima por critério (a Abrangência, com 3,0, é o único critério abaixo de 5);
     - campo do processo ainda não consolidado;
     - verificação de autoria ou integridade;
     - outra etapa pendente.

6. **A principal discrepância é a Abrangência = 3,0.** O texto responde, em ordem, às quatro perguntas orientadoras, com um parágrafo por pergunta. Se "abrangência" medisse a cobertura das perguntas, a nota seria alta. Logo, há três possibilidades [H para todas]:
   - o critério mede outra coisa (profundidade, fatos e repertório, extensão ou aderência a um gabarito de tópicos);
   - ele usa outra escala;
   - o avaliador é instável.

7. **O Tangenciamento = 7,1 tem explicação textual concreta** [IF, média]:
   - o recorte do tema ("a importância da educação e da conscientização") não aparece na introdução nem na tese;
   - "educação" surge pela primeira vez no caractere 1.050, aos 57% do texto;
   - o parágrafo do núcleo temático (P3) é o mais curto: 346 caracteres (18,8%), em 2 frases;
   - 55,9% do texto (P1 + P2) trata do assunto amplo (o problema e suas consequências).

   É o padrão clássico de tangenciamento parcial.

8. **Onde está o maior ganho possível.**
   - Sob pesos iguais, a Gramática pode somar no máximo 0,03 ponto à nota online, o Tangenciamento até 0,97 e a Abrangência até 2,33.
   - Em todo o conjunto de pesos compatíveis, o ganho máximo por A vai de 0,7 a 3,4 pontos, e o por G nunca passa de 0,05.
   - Conclusão robusta: **a gramática quase não pesa para melhorar esta nota; o ganho possível está em Abrangência e Tangenciamento.**

9. **Próximos passos mais informativos e baratos:**
   - (a) obter o edital ou regulamento e o status textual que acompanha a "Nota Final";
   - (b) submeter o mesmo texto de novo (teste-reteste).

   Se o avaliador é um LLM estocástico, todo experimento de uma variável precisa de repetições, e o reteste mostra quantas.

---

## 2. Inventário dos dados observados

### 2.1 Identificação e proposta

| Item | Valor |
|---|---|
| Identificação | avaliação 001; instituição, plataforma, data e número da tentativa não informados |
| Título da proposta | DESCARTE CORRETO DO LIXO |
| Tema (recorte) | "a importância da educação e da conscientização sobre o descarte correto do lixo" |
| Gênero | texto dissertativo |
| Exigências explícitas | (1) dissertativo; (2) mínimo de 1.200 caracteres; (3) linguagem formal; (4) "apresentando argumentos e **fatos** que comprovem seu ponto de vista" |
| Elemento facultativo | plano de texto com 4 perguntas ("Você **poderá** pensar…"): sugestão, não obrigação |
| Não especificado | máximo de caracteres; contagem com ou sem espaços; título obrigatório; proposta de intervenção obrigatória; escala; nota mínima; regra de eliminação |

### 2.2 Características observáveis da redação

| Medida | Valor |
|---|---|
| Caracteres com espaços | 1.841 (1.844 contando as 3 quebras de parágrafo), 153% do mínimo |
| Caracteres sem espaços | 1.564, 130% do mínimo |
| Palavras | 281 |
| Parágrafos / frases | 4 / 14 (média de 20,1 palavras por frase) |
| P1: situação atual (pergunta 1) | 521 caracteres (28,3%), 3 frases |
| P2: implicações (pergunta 2) | 509 caracteres (27,6%), 4 frases |
| P3: importância da educação (pergunta 3, núcleo do tema) | 346 caracteres (18,8%), 2 frases |
| P4: ações (pergunta 4) e conclusão | 465 caracteres (25,3%), 5 frases |
| Primeira menção a "educação"/"conscientização" | caractere 1.050 (57% do texto) |
| Frases sobre o recorte (educação/conscientização) | 4 de 14 (33,9% dos caracteres), 2 delas na conclusão |
| Fatos verificáveis | 1 (Política Nacional de Resíduos Sólidos, 2010); nenhum número, estatística, fonte ou caso concreto |
| Título | ausente no texto fornecido; não se sabe se a plataforma tinha campo próprio |

### 2.3 Notas e indicadores

| Campo (nome exato) | Valor | Natureza provável | Classificação |
|---|---|---|---|
| Nota Final | 0,00 | resultado de outro nível (processo ou status), ou nota após portão de eliminação | [IF] distinta da nota online |
| Nota de Gramática da Redação Online | 9,90 | nota de critério, escala 0–10 | [IF] |
| Nota da Abrangência da Redação Online | 3,00 | nota de critério; escala 0–10 se a média estiver certa | [H] |
| Nota do Tangenciamento (Fuga) | 7,10 | nota de critério, 0–10, **maior = mais aderente** | [IF] |
| Apontamento de erro gramatical | 4,00 | indicador auxiliar, provavelmente uma contagem | [H] |
| Nota Final da Redação Online | 6,60 | nota agregada de G, A e T | [IF] |

O que a nomenclatura sugere (evidência fraca, mas gratuita):
- Três campos têm o sufixo "da Redação Online" e três não têm. O sufixo não coincide com os campos que entram na média: T não tem o sufixo e parece entrar. Portanto, a nomenclatura não define o cálculo.
- "Apontamento de erro gramatical" é o único campo sem a palavra "Nota", o que reforça que não é uma nota.
- "Nota Final", sem qualificador e listada em primeiro lugar, sugere o resultado do processo, e não da redação.
- Todos os valores são múltiplos de 0,1, inclusive o 4,00: a precisão provável é 0,1, exibida com duas casas [IF].

### 2.4 Informações ausentes que impedem a reconstrução

| Ausência | O que fica sem resposta |
|---|---|
| Edital, regulamento ou manual | escalas, pesos, nota mínima e regra de eliminação documentados |
| Status textual junto da nota (aprovado, reprovado, eliminado, em análise) | o motivo do 0,00 |
| Trechos apontados e comentários do avaliador | o que é o 4,00 e o que a Abrangência pune |
| Outras avaliações (outros textos, temas, candidatos) | pesos, regra de arredondamento e portões |
| Contagem de caracteres da plataforma, campo de título, número da tentativa, data | regras de extensão e de tentativa |
| Se a "Nota Final" inclui outras provas (objetiva, ENEM) | se o 0,00 é falta de outro componente |

---

## 3. Ficha técnica de cada critério

### 3.1 Gramática (G = 9,90)

- **a) Definição provável.** Adesão à norma-padrão escrita (ortografia, acentuação, concordância, regência, crase e pontuação), com desconto pequeno por ocorrência apontada [IF, média].
- **b) Dimensões a investigar.**
  - ortografia e acentuação;
  - morfossintaxe (concordância, regência, crase, colocação pronominal);
  - pontuação;
  - possivelmente estilo (repetição, redundância, elipse).

  Não há evidência sobre vocabulário ou complexidade sintática.
- **c) Indicadores.** Número e talvez densidade (por palavra) dos desvios; talvez a gravidade de cada um.
- **d) Evidências na redação.** Não encontrei erro inequívoco de norma-padrão. Há, porém, cinco trechos corretos que verificadores automáticos costumam apontar como erro (falsos positivos típicos):
  1. "**Apesar de a** separação do lixo ser…": não contrair a preposição antes do sujeito de um infinitivo é a forma prescrita, mas corretores costumam sugerir "da".
  2. "entulho e embalagens **abandonados**": o masculino plural com núcleos de gêneros diferentes está correto; corretores podem sugerir "abandonadas" (concordância atrativa).
  3. "**Ao cidadão, compete** separar…": a vírgula depois do complemento anteposto é aceitável, mas pode ser marcada como "vírgula entre verbo e complemento".
  4. "algo que multas e fiscalização, isoladamente, **não conseguem**.": elipse do complemento ("não conseguem fazer"), questão de estilo.
  5. "**o seu** descarte": possessivo redundante, questão de estilo.

  A presença de 4 ou 5 trechos "apontáveis" é consistente com E = 4 ser uma contagem de apontamentos [H, baixa].
- **e) Escala.** Valor observado de 9,9; escala provável de 0 a 10 com passo de 0,1 [IF]. O mínimo e um eventual piso são desconhecidos.
- **f) Regras de pontuação compatíveis com n = 1.**
  - G = 10 − 0,025·E (exato);
  - G = 10·(1 − E/palavras) = 9,858 → 9,9, com arredondamento (com truncamento daria 9,8);
  - G holístico, independente de E.

  Fica refutada G = 10 − 0,1·E, que daria 9,6. Em qualquer modelo derivado de E, um apontamento custa ~0,025–0,036 ponto em G e no máximo 0,012 na nota online. **A Gramática quase não reage a erros nessa faixa.**
- **g) Interações.** Sob a média sem E, os erros não são contados duas vezes. Se o LLM avaliar de forma holística, um texto com muitos erros pode perder também em Tangenciamento ou Abrangência (o experimento X1 testa isso).
- **h) Confiança.** Escala: média. Relação com E: baixa.

### 3.2 Abrangência (A = 3,00)

**a) Definição provável.** Indeterminada. As hipóteses concorrentes são:

| ID | O que A mediria | Ajuste ao dado | Status |
|---|---|---|---|
| H-A1 | cobertura das 4 perguntas orientadoras (0–10) | o texto cobre 4/4, de forma explícita e em ordem, então a previsão seria ≥ 7 | **enfraquecida** |
| H-A1' | contagem de perguntas cobertas (0–4), "3 de 4" | conflita com a média: com A reescalado para 7,5, a média seria 8,17, e não 6,6 | **enfraquecida** |
| H-A2 | profundidade e desenvolvimento de cada aspecto | P3 tem 2 frases e as afirmações não são demonstradas; plausível | ativa |
| H-A3 | fundamentação factual e repertório (o comando exige "argumentos e **fatos**") | 1 fato, nenhum dado, nenhuma fonte; plausível | ativa |
| H-A4 | extensão em relação a um alvo | qualquer constante livre ajusta n = 1 (ex.: trunc(1.841/600) = 3,0), então a coincidência não é evidência | ativa, sem apoio |
| H-A5 | aderência a um gabarito de tópicos esperados | faltam reciclagem explícita, 3Rs, aterro sanitário, logística reversa, compostagem, resíduos perigosos e eletrônicos | ativa |
| H-A6 | diversidade de dimensões (ambiental, saúde, econômica, social) | o texto cobre as quatro, então a previsão seria alta | **enfraquecida** |
| H-A7 | níveis discretos (A = 3,00 é o único valor inteiro do conjunto) | compatível; precisa de mais observações | ativa |
| H-A8 | instabilidade ou erro do avaliador | compatível; o reteste testa | ativa |

**b) Dimensões a investigar.** Número de aspectos tratados; desenvolvimento por aspecto (quantidade de frases e mecanismos causais); fatos, dados e exemplos concretos; extensão; tópicos esperados.

**c) O que provavelmente elevaria A** (se H-A2 ou H-A3 estiverem certas):
- fatos verificáveis com fonte;
- exemplos concretos;
- mecanismos causais explicados, e não só afirmados;
- equilíbrio de extensão entre os aspectos.

**d) Evidências na redação.**
- "grande parte da população brasileira ainda não descarta os resíduos de forma adequada": afirmação sem dado; responde à pergunta 1 sem comprovar.
- "Embora a Política Nacional de Resíduos Sólidos, instituída em 2010…": o único fato verificável do texto.
- "a educação e a conscientização são ferramentas fundamentais, uma vez que mudam hábitos de forma duradoura": a tese central do tema aparece como asserção, sem exemplo, dado ou mecanismo.
- P2 lista quatro consequências (enchentes, contaminação, dengue, perda de renda) com uma oração para cada: amplitude sem profundidade.

**e) Escala.** De 0 a 10, se a média estiver correta [H]. Não há outra âncora.

**f) Regras de pontuação.** Não inferíveis com os dados atuais.

**g) Interações.** O P3 curto reduz ao mesmo tempo a profundidade (A) e a centralidade do recorte (T). Se houver nota mínima por critério, A seria o critério que zera a Nota Final.

**h) Confiança.** Baixa. É o critério menos compreendido e o que mais pesa no resultado.

### 3.3 Tangenciamento (Fuga) (T = 7,10)

- **a) Definição provável.** Grau de aderência ao recorte temático: 10 quando o recorte é o eixo do texto, 0 na fuga total. A orientação **"maior = melhor"** é uma inferência forte por dois motivos:
  - com T invertido, a média daria 5,27, e não 6,6;
  - um texto sobre o assunto não receberia 7,1 de 10 em "grau de fuga".
- **b) Dimensões.** Presença do tema; centralidade do recorte (educação e conscientização) frente ao assunto amplo (lixo e descarte); tese alinhada ao recorte; proporção do texto dedicada ao recorte.
- **c) Indicadores.** Tese na introdução que nomeie o recorte; parágrafos de desenvolvimento que o retomem; proporção de frases sobre ele.
- **d) Evidências na redação.**
  - A tese da introdução é "a existência de uma lei, por si só, não garante mudança de comportamento". É relacionada, mas não é a tese pedida (a importância da educação).
  - O recorte aparece pela primeira vez aos 57% do texto e ocupa 4 das 14 frases.
  - P1 e P2 (55,9%) tratam do assunto amplo.

  Seguir o plano facultativo da proposta leva justamente a essa distribuição: **o plano sugerido induz ao tangenciamento que o próprio avaliador pune** [H]. É preciso separar duas coisas: a deficiência real do texto é a tese não nomear o recorte; a exigência possivelmente específica do avaliador é a proporção do recorte.
- **e) Escala.** De 0 a 10, com passo de 0,1 [IF].
- **f) Regras de pontuação.** Desconhecidas. Pode existir um portão (T abaixo de um limiar conta como fuga e zera a nota), mas não há como saber se ele disparou.
- **g) Interações.** Compartilha com A a deficiência do P3.
- **h) Confiança.** Orientação: média-alta. Mecanismo: baixa a média.

### 3.4 Apontamento de erro gramatical (E = 4,00)

| Hipótese | Ajuste | Status |
|---|---|---|
| contagem de ocorrências apontadas (4) | coerente com G ≈ 10 e com os 4–5 trechos "apontáveis"; é o único campo sem "Nota" | mais provável [H] |
| nota de 0 a 10 de "erro" | incoerente com G = 9,9 medindo a mesma coisa | enfraquecida |
| penalidade em pontos subtraída da nota online | (G+A+T)/3 − 4 = 2,67 ≠ 6,6 | refutada |
| penalidade subtraída da Nota Final | 6,6 − 4 = 2,6 ≠ 0 | refutada |
| entra na nota online com coeficiente pequeno | (G+A+T − 0,05·E)/3 = 6,60 exato | compatível, mas o coeficiente é ad hoc [H, baixa] |
| código de categoria ou flag | compatível com tudo | não testável sem outras observações |

### 3.5 Nota Final da Redação Online (6,60) e Nota Final (0,00)

Ver as seções 4 e 5.

---

## 4. Escalas e distribuição de pontos

- **Precisão.** Todos os valores são múltiplos de 0,1, então a precisão exibida é de 0,1 [IF]. A precisão interna é desconhecida, e isso pesa na fórmula (seção 5).
- **Máximo.** 10 para G, T e a nota online [IF]: G = 9,9 está perto do teto e nenhum valor passa de 10. Para A, a escala de 0 a 10 só vale se a média estiver correta [H].
- **Distribuição.** Com pesos iguais, cada critério vale 1/3 da nota online (3,33 pontos). Nas alternativas compatíveis, wG ∈ [0; 0,54], wA ∈ [0,10; 0,48] e wT ∈ [0; 0,90].
- **O que vale para qualquer peso compatível.** wA > 0, porque 6,6 < min(G, T). Já G contribui pouco para a variação: no máximo +0,05.
- **Penalidades.** Nada indica penalidade aplicada à nota online fora dos três critérios. O zero da Nota Final aponta para uma regra de eliminação ou para um campo de outro nível.
- **Arredondamento.** O truncamento a 0,1 é a regra mais simples compatível com os dados. O arredondamento a 0,1 só é compatível se houver precisão interna oculta.

Ganho máximo possível na nota online por critério (levando cada um a 10):

| Pesos | G (+0,1) | A (+7,0) | T (+2,9) |
|---|---|---|---|
| iguais (1/3) | +0,03 | +2,33 | +0,97 |
| faixa compatível | 0 a +0,05 | +0,69 a +3,35 | 0 a +2,62 |

---

## 5. Reconstrução da fórmula da nota final

### 5.1 Nota Final da Redação Online

| # | Equação | Valores usados | Resultado | Observado | Diferença | Confiança | O que distinguiria |
|---|---|---|---|---|---|---|---|
| M1 | trunc₀,₁((G+A+T)/3) | 9,9; 3,0; 7,1 | 6,6667 → **6,6** | 6,60 | 0 | **média (melhor candidato)** | médias com fração entre ,x5 e ,x9, em que truncar e arredondar dão resultados diferentes |
| M1b | arred₀,₁((G*+A*+T*)/3), com G*, A*, T* internos não exibidos | soma interna ∈ [19,85; 19,95) | 6,6 | 6,60 | 0 | baixa a média | casos em que as notas exibidas sejam truncamentos; reteste |
| M1c | arred₀,₁ ou arred₀,₀₁ da média das notas exibidas | 9,9; 3,0; 7,1 | 6,7 / 6,67 | 6,60 | +0,1 / +0,07 | **refutada** | — |
| M2 | pesos desiguais com arredondamento ou truncamento (ex.: 0,35/0,35/0,30; 0,40/0,40/0,20; 0,20/0,25/0,55) | 9,9; 3,0; 7,1 | 6,58–6,65 → 6,6 | 6,60 | 0 | baixa | perfis com G, A e T muito diferentes entre si |
| M3 | 0,29G + 0,32A + 0,39T (únicos pesos inteiros em % que dão o valor exato sem arredondar) | 9,9; 3,0; 7,1 | 6,600 | 6,60 | 0 | muito baixa (pesos sem justificativa) | qualquer nova observação |
| M4 | (G + A + T − 0,05·E)/3 | E = 4 | 6,600 | 6,60 | 0 | baixa (coeficiente ad hoc) | X1: mais erros com A e T constantes |
| M5 | média de G, A, T e E | — | 6,00 | 6,60 | −0,60 | **refutada** | — |
| M6 | média com T invertido (10 − T) | — | 5,27 | 6,60 | −1,33 | **refutada** | — |
| M7 | média geométrica / média harmônica / mediana / mínimo | — | 5,95 / 5,22 / 7,10 / 3,00 | 6,60 | ≥ 0,5 | **refutadas** | — |
| M8 | nota holística gerada pelo LLM, sem fórmula (≈ média) | — | ≈ 6,6 | 6,60 | — | média | reteste; verificar se a nota online coincide com M1 em todas as observações |

**Por que não é possível escolher a fórmula verdadeira:**
- Uma equação com três pesos (dois livres, se a soma é 1) e uma única observação tem infinitas soluções.
- O arredondamento transforma cada observação numa faixa, e não num ponto.
- M1 é preferido apenas por parcimônia: pesos iguais e truncamento, regra comum em software.

O que seria necessário:
- **Para identificar os pesos:** pelo menos 2 observações adicionais com perfis (G, A, T) linearmente independentes do atual. Por causa do arredondamento, na prática são 5 a 10 observações com perfis variados para estreitar as faixas.
- **Para distinguir truncamento de arredondamento:** casos cuja média tenha fração entre ,x5 e ,x9.

### 5.2 Nota Final (0,00)

Modelo geral: **Nota Final = portão × nota online**, ou um campo independente.

| Regra candidata | Resultado com os dados atuais |
|---|---|
| Nota Final = nota online, sempre | **não explica** (6,6 ≠ 0) [C] |
| zera se algum critério = 0 | não explica (nenhum critério é 0) |
| zera só por fuga total (T = 0) | não explica (T = 7,1) |
| zera se nota online < 5 ou < 6 | não explica (6,6) |
| zera se nota online < 7 (nota mínima de aprovação 7,0) | compatível [H] |
| zera se Abrangência < 4 ou < 5, ou se algum critério < 5 | compatível [H]; A é o único critério abaixo de 5 |
| zera se T < limiar alto (ex.: 7,5) | compatível, pouco plausível |
| zera se apontamentos ≥ 4 | compatível, pouco plausível com G = 9,9 |
| campo do processo seletivo ainda não consolidado ou homologado, ou dependente de outra etapa (prova objetiva, revisão humana, ENEM) | compatível [H] |
| verificação de autoria ou similaridade (texto não autoral zera; regra comum em vestibulares online) | compatível; não avaliável com os dados [H] |
| extensão abaixo do mínimo | **muito improvável**: 1.564 a 1.844 caracteres em qualquer contagem usual |

"Não explica" quer dizer que a regra não basta sozinha; ela ainda pode existir junto com outra causa.

---

## 6. Evidências extraídas da redação

| Elemento | Observação | Influência provável | Isolável agora? |
|---|---|---|---|
| Atendimento ao tema e ao comando | assunto amplo atendido; recorte tardio e minoritário | T (7,1) | não; X6 e X7 testam |
| Cobertura das perguntas | 4/4, em ordem, um parágrafo cada | se A medisse isso, seria alta; provavelmente não é o que A mede | não; X7 testa |
| Profundidade | asserções sem demonstração; P3 com 2 frases | A e T | não; X4 vs. X5 |
| Pertinência e especificidade | argumentos pertinentes, mas genéricos ("é comum encontrar…") | A | não |
| Fatos, exemplos e referências | 1 fato (PNRS, 2010); nenhum dado; nenhuma fonte; o comando pede "fatos" | A (H-A3) | não; X3 testa |
| Estrutura dissertativa | introdução, desenvolvimento e conclusão claros; conectivos adequados | provavelmente neutra (nenhum critério próprio visível) | — |
| Coesão e coerência | boas ("Nesse contexto", "Portanto", "Além disso") | provavelmente neutras | — |
| Norma-padrão | nenhum erro inequívoco; 5 trechos propensos a falso positivo | G (9,9) e E (4) | X1, X2 |
| Vocabulário e sintaxe | formal; frases de 20 palavras em média | sem evidência | — |
| Proposta de intervenção | agentes (escolas, prefeituras, cidadão) e ações, sem detalhar meio e finalidade de cada agente | nenhum critério visível; talvez A | não |
| Extensão | 153% do mínimo | possivelmente A (H-A4) | X5 |

**As notas são coerentes com o texto?**
- **G = 9,9:** coerente.
- **T = 7,1:** severa, mas defensável. Um corretor humano provavelmente veria "abordagem completa com desenvolvimento desigual", e não tangenciamento. O avaliador parece exigir que o recorte seja o eixo do texto.
- **A = 3,0:** **desproporcional** sob qualquer leitura convencional de "abrangência". Fica registrada como discrepância, sem descartar o dado. Hipóteses: o critério mede outra coisa (H-A2, H-A3, H-A5), usa escala ou níveis diferentes (H-A7), ou o avaliador é instável (H-A8).

---

## 7. Hipóteses alternativas e limitações

1. **Só há uma observação.** Toda reprodução exata é retrospectiva; nenhum modelo foi testado em previsão.
2. **Estocasticidade.** Se o avaliador é um LLM, a mesma redação pode receber notas diferentes, e diferenças pequenas entre variantes podem ser ruído.
3. **A nota online pode não vir de uma fórmula** (M8). Nesse caso, os "pesos" são uma descrição aproximada, e não um mecanismo.
4. **Precisão oculta.** Não se sabe se 9,9, 3,0 e 7,1 são valores exatos ou arredondados. Isso basta para tornar truncamento e arredondamento indistinguíveis.
5. **O significado de "Abrangência"** não tem âncora documental nem contraste com outro caso.
6. **O significado da "Nota Final".** Pode ser de outro nível (o processo seletivo), depender de prazo ou homologação, ou de uma regra de integridade. As notas sozinhas não distinguem essas causas.
7. **Tema fixo.** Todas as inferências sobre A e T valem só para esta proposta. A pode depender do gabarito de cada tema (H-A5).
8. **Experimentos no sistema real** podem contar como tentativas oficiais. Algumas plataformas limitam o número de tentativas ou trocam o tema a cada uma, o que impediria manter a proposta constante. Verifique as regras antes de submeter.

---

## 8. Experimentos controlados recomendados

- Os textos prontos estão em `experimentos/variantes/`, gerados por `ferramentas/gerar_variantes.py`. Cada variante difere da base só pelas substituições declaradas, listadas em `experimentos/variantes/MUDANCAS.md`.
- As hipóteses, as previsões numéricas (registradas **antes** de qualquer resultado) e as tabelas de resultado estão em `experimentos/protocolo.md`.

| # | Hipótese testada | Variável única | Δ extensão | Previsões que discriminam |
|---|---|---|---|---|
| X0 | o avaliador é determinístico | nenhuma (mesmo texto) | 0% | notas idênticas indicam determinismo; variação mede o ruído (≥ 2 repetições) |
| X1a | E conta erros; G deriva de E; E fica fora da média | +4 erros inequívocos (crase, 2 de concordância verbal, acentuação) | −0,1% | E = 8; G = 9,8 (10 − 0,025E) ou 9,7 (densidade); nota online 6,6 (M1) ou 6,5/6,4 (M4) |
| X1b | dose-resposta | +12 erros inequívocos | −0,3% | E = 16; G = 9,6 ou 9,4; nota online 6,5 (M1) ou 6,3/6,2 (M4) |
| X2 | E corresponde aos falsos positivos dos 5 trechos | reescrita dos 5 trechos | +0,2% | E cai para 0–1 e G sobe a 10, levando a nota online a 6,7; se E não mudar, os apontamentos estão em outro lugar |
| X3 | A mede fatos (H-A3) | +3 fatos verificáveis em P1 e P2: prazo de 2014 da PNRS prorrogado em 2020; Aedes aegypti; césio-137 em Goiânia (1987) | +18,5% | H-A3: A sobe bem mais que em X5; H-A4: A sobe tanto quanto em X5; H-A1: A não muda |
| X4 | A mede profundidade (H-A2); T mede centralidade | +2 frases de raciocínio no P3, sem fatos | +19,8% | H-A2: A sobe mais que em X5; T sobe |
| X5 | A mede extensão (H-A4); controle de X3 e X4 | +2 frases redundantes no P3, sem ideia nova | +18,3% | H-A4: A sobe; nas outras hipóteses, A fica igual ou cai |
| X6 | T mede se a tese nomeia o recorte | a última frase do P1 passa a nomear educação e conscientização | +5,8% | T sobe; A fica igual |
| X7 | A mede cobertura das perguntas (H-A1) | troca o P2 (implicações) por um parágrafo de mesma extensão sobre educação | −1,7% | H-A1: A cai; H-A4: A fica igual; T sobe (o recorte passa de 34% para 52–61% do texto, conforme o critério de contagem) |

**Teste do portão da Nota Final.** Registre a Nota Final em cada variante. A matriz de regras da seção 5.2 se resolve se alguma variante produzir A ≥ 5 com nota online < 7, ou A < 5 com nota online ≥ 7.

**Ordem sugerida:** X0, X2, X3/X4/X5, X6, X7 e, por fim, X1. O X1 deixa o texto propositalmente pior, por isso fica por último, para não gastar com ele uma tentativa que possa contar oficialmente.

**Limitação comum.** Cada experimento muda uma única característica do ponto de vista de quem escreve, mas um LLM avalia o texto como um todo. Acrescentar fatos (X3), por exemplo, também aumenta a extensão; é por isso que o X5 existe como controle de extensão.

---

## 9. Rubrica reconstruída v0.1 (parcial e provisória)

Nenhum item é documentado. As **âncoras** correspondem ao único ponto observado; os descritores fora da âncora são hipóteses de trabalho, ainda não observadas.

### Gramática

| Campo | Conteúdo | Status |
|---|---|---|
| Definição operacional | desvios de norma-padrão apontados, com desconto pequeno por ocorrência | [IF] |
| Escala e máximo | 0–10, passo 0,1 | [IF] |
| Peso na nota online | 1/3 (M1); faixa compatível de 0 a 54% | [H] |
| Subcritérios | ortografia, acentuação, concordância, regência, crase, pontuação; talvez estilo | [H] |
| Âncora observada | 9,9 com 4 apontamentos em 281 palavras (≈ 1 a cada 70 palavras), sem erro inequívoco | [C] |
| Descritores baixo/intermediário | sem dado | — |
| Penalidade | ~0,025–0,036 por apontamento, se G deriva de E | [H] |
| Confiança | média (escala), baixa (regra) | — |

### Abrangência

| Campo | Conteúdo | Status |
|---|---|---|
| Definição operacional | indeterminada; candidatas principais: profundidade de desenvolvimento (H-A2) e fundamentação factual (H-A3) | [H] |
| Escala | 0–10 se M1; possivelmente níveis discretos (H-A7) | [H] |
| Peso | 1/3 (M1); faixa compatível de 10 a 48% (o peso ser maior que 0 é robusto) | [H] / [C condicional] |
| Âncora observada | **3,0** = 4/4 perguntas respondidas, com um parágrafo cada; 1 fato verificável (lei e ano); nenhum dado quantitativo; parágrafo do núcleo com 2 frases; 1.841 caracteres | [C] |
| Descritor "baixo" (hipótese de trabalho) | aspectos enunciados, mas apenas afirmados; no máximo 1 fato; núcleo com até 2 frases | [H] |
| Descritores intermediário/alto | sem dado; hipótese de trabalho: fatos verificáveis com fonte, mecanismo explicado e exemplo concreto em cada aspecto | [H] |
| Condições especiais | possivelmente é a regra que zera a Nota Final (A < 5?) | [H] |
| Confiança | baixa | — |

### Tangenciamento (Fuga)

| Campo | Conteúdo | Status |
|---|---|---|
| Definição operacional | proporção e centralidade do recorte (educação e conscientização) frente ao assunto amplo (lixo e descarte) | [IF] |
| Escala | 0–10, passo 0,1, maior = mais aderente | [IF] |
| Peso | 1/3 (M1); faixa compatível de 0 a 90% | [H] |
| Âncora observada | **7,1** = assunto amplo integralmente atendido; recorte ausente da tese; primeira menção aos 57% do texto; 4 de 14 frases (34%) sobre o recorte | [C] |
| Descritores (hipótese de trabalho) | ≥ 9: recorte nomeado na tese da introdução e retomado em todos os parágrafos de desenvolvimento; ~7: recorte presente, mas restrito a um parágrafo e ausente da tese (âncora); ≤ 4: recorte só na conclusão ou ausente; 0: fuga | [H], exceto a âncora |
| Confiança | média | — |

### Nota online e Nota Final

- **Nota online:** M1 = trunc₀,₁((G+A+T)/3) [H, melhor candidato].
- **Nota Final:** portão de eliminação ou campo de outro nível; as regras compatíveis estão na seção 5.2.

**Validade preditiva.** A rubrica só passa a ter validade preditiva quando acertar previsões sobre observações que não foram usadas para ajustá-la. As previsões estão registradas em `experimentos/protocolo.md`.

---

## 10. Próximos dados mais úteis (em ordem de valor por custo)

1. **Nome da instituição ou plataforma e o edital ou regulamento do processo.** Resolveria de uma vez escala, nota mínima e regras de eliminação. Com o nome, dá para fazer uma busca documental dirigida.
2. **O status textual exibido junto da Nota Final** (aprovado, reprovado, eliminado, em análise) e qualquer comentário ou marcação do avaliador, como os trechos apontados.
3. **Outras avaliações já existentes**, de outros textos ou temas e até de outras pessoas, com os seis campos. Vale especialmente qualquer uma com Nota Final diferente de 0, porque revelaria o portão.
4. **O teste-reteste (X0).**
5. A contagem de caracteres mostrada pela plataforma, a existência de campo de título, o número da tentativa, a data e se houve revisão humana.
6. Os experimentos X2, X3/X4/X5, X6, X7 e X1, nessa ordem.

---

## Apêndice A — Auditoria (Etapa 8)

| Verificação | Resultado |
|---|---|
| As notas foram transcritas corretamente? | sim: 0,00 / 9,90 / 3,00 / 7,10 / 4,00 / 6,60, conferidas com a entrada e registradas em `dados/avaliacoes.csv` e `avaliacoes/001-descarte-lixo/notas.md` |
| Os indicadores auxiliares foram separados das notas? | sim: E é tratado como indicador e a Nota Final como grandeza distinta |
| A nota online pode ser reproduzida matematicamente? | sim, por vários modelos, mas a fórmula não é identificável |
| As hipóteses são compatíveis com os dados? | as incompatíveis estão marcadas (M1c, M5, M6, M7 e as regras de portão que "não explicam") |
| Há conclusão apoiada em suposição não declarada? | M1 supõe T com orientação positiva e A em 0–10; ambas as suposições estão declaradas |
| Pesos e escalas foram identificados ou apenas estimados? | apenas estimados; as faixas estão reportadas |
| Há explicações alternativas igualmente compatíveis? | sim: M1b, M2, M4 e M8 |
| Quais observações adicionais dariam mais informação? | seção 10 |
| A rubrica prevê resultados não usados na sua construção? | ainda não testado; previsões registradas em `experimentos/protocolo.md` |

## Apêndice B — Fontes consultadas

Nenhuma das fontes abaixo descreve esta plataforma. Elas mostram práticas comuns em correção de redação: zeramento por fuga, teto de nota por tangenciamento e exigência de autoria em provas online. As regras desta plataforma continuam desconhecidas. Parte do conteúdo foi lido apenas nos trechos dos resultados de busca.

- [UNIFIMES: critérios de correção da redação (tangenciamento como faixa do critério de gênero)](https://unifimes.edu.br/filemanager_uploads/files/documentos/vestibular/Provas_Medicina_OLD/2024_1/Trindade-Crit%C3%A9rios%20de%20corre%C3%A7%C3%A3o%20Reda%C3%A7%C3%A3o.pdf)
- [Comperve/UFRN: expectativa de resposta (o tangenciamento limita a nota do critério)](https://comperve.ufrn.br/conteudo/concursos/ufrn_202111/gabaritos/expectativa_redacao_superior.pdf)
- [UEA: critérios de avaliação da redação (a fuga completa impede a correção dos demais aspectos)](https://selecao1.uea.edu.br/xfiles/data/xselecao/6713.pdf)
- [Unoeste EAD: sobre a prova (limites de caracteres e exigência de texto autoral)](https://unoeste.br/site/vestibular/EAD/SobreProva.aspx)
- [Faculdade Nepuga: regras de correção do vestibular online (zeramento por critério; página inacessível na verificação)](https://faculdadenepuga.edu.br/regras-correcao-vestibular-online/)
- [Redação Online: fuga ao tema e tangenciamento no ENEM](https://redacaonline.com.br/blog/fuga-ao-tema-e-tangenciamento-diferenca)
