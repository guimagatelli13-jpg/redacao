# Engenharia reversa de um avaliador de redação por IA

Investigação do sistema de correção "Redação Online": quais critérios usa, em que escalas, com que pesos e qual
fórmula produz a nota. As notas observadas são tratadas como dados de comportamento, e cada conclusão é classificada
como confirmada, inferência forte ou hipótese exploratória.

## Estado atual

- **4 avaliações** (2 temas). Instituição: Faculdades Pequeno Príncipe; plataforma: CRM Educacional. Regras documentadas: nota até 10;
  classificação com 6,0 ou mais e nenhum critério zerado; 1.200 a 2.000 caracteres.
- **Melhor candidato para a nota online:** `arred₀,₁(0,4·Gramática + 0,4·Abrangência + 0,2·Tangenciamento)`.
  A média simples foi refutada; o peso da Abrangência está entre 38% e 42%.
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
| `modelo/registro.md` | registro vivo: hipóteses e seus status, previsões e resultados, questões em aberto |
| `modelo/rubrica-hibrida-enem.md` | critérios do ENEM adaptados à plataforma: correspondências, descritores por nível e cálculo da nota prevista e da nota ENEM equivalente |
| `experimentos/protocolo*.md` | experimentos controlados de cada série, com previsões registradas antes dos resultados |
| `experimentos/variantes/` | textos prontos para submissão e `MUDANCAS.md`, com o diff exato de cada um |
| `experimentos/textos/` | textos escritos do zero para experimentos (não gerados por substituição), como o X8 |
| `ferramentas/testar_modelos.py` | testa fórmulas, regras de arredondamento, faixas de pesos e regras da Nota Final contra todas as avaliações |
| `ferramentas/gerar_variantes.py` | gera as variantes a partir do texto-base por substituição exata |
| `ferramentas/sobreposicao_lexical.py` | mede quanto do vocabulário da proposta (tema e perguntas) aparece em cada redação avaliada |
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
