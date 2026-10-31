# Engenharia reversa de um avaliador de redação por IA

Investigação do sistema de correção "Redação Online": quais critérios usa, em que escalas, com que pesos e qual
fórmula produz a nota. As notas observadas são tratadas como dados de comportamento, e cada conclusão é classificada
como confirmada, inferência forte ou hipótese exploratória.

## Estado atual

- **5 avaliações** (2 temas). Instituição: Faculdades Pequeno Príncipe; plataforma: CRM Educacional. Regras documentadas: nota até 10;
  classificação com 6,0 ou mais e nenhum critério zerado; 1.200 a 2.000 caracteres.
- **Melhor candidato para a nota online:** `arred₀,₁(0,4·Gramática + 0,4·Abrangência + 0,2·Tangenciamento)`, que acertou
  as três avaliações posteriores a ela. A média simples foi refutada; o peso da Abrangência está entre 38,7% e 40,7%.
- **Tangenciamento:** acompanha as palavras e os pares da frase do tema presentes no texto; o máximo observado é 9,0.
- **Abrangência:** fica agrupada por tema (lixo 2,8 a 3,2; consumo 2,4) e não respondeu a fatos, repertório, tamanho
  nem vocabulário da proposta. Por isso a maior nota online observada é 6,9 e o teto prático é por volta de 7,0.
- **Rubrica calibrada v1** (`modelo/rubrica-calibrada.md`): critérios com teto 10 que reproduzem G, A, T e a nota
  online das 5 provas. Pista principal: a Abrangência exibida parece ser 0,4 × uma nota de 0 a 10; se for, a nota online
  da plataforma vai no máximo a 7,6. Previsões registradas para a série 005.
- **"Nota Final" e "Nota Final da Redação Online" são grandezas diferentes.** O 0,00 da primeira não sai das notas
  parciais.

Leia `relatorios/001-analise-inicial.md` para a análise completa e `modelo/registro.md` para o estado das hipóteses.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `dados/avaliacoes.csv` | base acumulada: uma linha por avaliação, com notas e medidas do texto |
| `avaliacoes/NNN-tema/` | proposta, redação exatamente como submetida e notas exatamente como exibidas |
| `propostas/` | propostas de tema ainda sem avaliação registrada |
| `relatorios/` | análises; cada relatório é um retrato do momento em que foi escrito |
| `fontes/` | fontes externas que não são da plataforma, como as orientações da professora |
| `modelo/registro.md` | registro vivo: hipóteses e seus status, previsões e resultados, questões em aberto |
| `modelo/roteiros-por-tema.md` | roteiros de preparação para os três temas sorteados (lixo, consumismo, clima), para o candidato escrever a própria redação |
| `modelo/rubrica-calibrada.md` | critérios com teto 10 calibrados para reproduzir as notas reais, com o histórico do que foi testado e as previsões |
| `modelo/rubrica-hibrida-enem.md` | critérios do ENEM adaptados à plataforma: correspondências, descritores por nível e cálculo da nota prevista e da nota ENEM equivalente |
| `experimentos/protocolo*.md` | experimentos controlados de cada série, com previsões registradas antes dos resultados |
| `experimentos/historico-simulador/` | as redações salvas no histórico do simulador, com previsões em `protocolo-006-historico.md` |
| `experimentos/variantes/` | textos prontos para submissão e `MUDANCAS.md`, com o diff exato de cada um |
| `experimentos/textos/` | textos escritos do zero para experimentos (não gerados por substituição), como o X8 |
| `simulador/simulador.html` | simulador de treino para os três temas, publicado como artefato: prevê os campos da plataforma (modelo v0.18), confere o método da professora, corrige por IA e guarda as tentativas com as notas oficiais registradas |
| `ferramentas/testar_modelos.py` | testa fórmulas, regras de arredondamento, faixas de pesos e regras da Nota Final contra todas as avaliações |
| `ferramentas/gerar_variantes.py` | gera as variantes a partir do texto-base por substituição exata |
| `ferramentas/sobreposicao_lexical.py` | mede quanto do vocabulário da proposta (tema e perguntas) aparece em cada redação avaliada |
| `ferramentas/rubrica_calibrada.py` | aplica a rubrica calibrada às avaliações reais e aos textos da série 005 e compara com as notas |
| `ferramentas/verificar_amarracao.py` | confere se cada elo de um texto (eixo, causa, proposta, repertório) aparece em todos os parágrafos esperados |

## Como registrar uma nova avaliação

1. Crie `avaliacoes/NNN-tema/` com:
   - `proposta.md`: o enunciado completo;
   - `redacao.txt`: o texto exatamente como submetido, um parágrafo por linha;
   - `notas.md`: os seis campos com os nomes exatos, além do status textual, comentários e marcações do avaliador,
     contagem de caracteres exibida, data e hora, número da tentativa e se foi variante de algum experimento.
2. Acrescente uma linha a `dados/avaliacoes.csv`.
3. Rode `python3 ferramentas/testar_modelos.py`. Modelos que deixarem de acertar todas as avaliações estão refutados
   ou precisam de revisão.
4. Se for um experimento, compare com a previsão em `experimentos/protocolo.md` e registre o resultado na seção 4 de
   `modelo/registro.md`.
5. Atualize os status das hipóteses no registro. Uma hipótese só passa a "apoiada" quando acerta uma previsão feita
   antes do dado.

Requisitos: Python 3, apenas biblioteca padrão.
