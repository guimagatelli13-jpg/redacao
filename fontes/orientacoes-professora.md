# Orientações da professora de redação

Fonte: mensagens de áudio repassadas pelo usuário em 2026-10-27, com a transcrição automática feita pelo aplicativo
de mensagens. A transcrição pode ter erros ("Claudio"/"Cláudio" é o assistente). As capturas de tela não foram
guardadas no repositório porque contêm dados pessoais. Uma terceira mensagem aparece cortada ("…penalização, porque
precisamos…"); falta o texto completo.

## Transcrição

**Áudio 1 (0:32):**
> "É pedir para o Claudio responder às quatro perguntas divididas nos quatro parágrafos, mas que não pode ser uma
> resposta para cada pergunta de forma não pertinente. Então não adianta falar de consumo e consumismo e trazer o
> endividamento das famílias, porque muitas vezes o endividamento não é por consumismo. É por necessidade de itens
> básicos, então tem que relacionar. Pedir pro Cláudio não trazer modernidade líquida e nenhum outro repertório tido
> como repertório de bolso no Enem."

**Áudio 2 (0:18):**
> "Não pode deixar nenhuma lacuna, nenhuma ponta solta na argumentação. Toda argumentação tem que estar relacionada às
> perguntas que foram feitas na proposta. E todas elas precisam explicar como a proposta… as perguntas devem
> responder à questão que está sendo tratada."

## Orientações, uma a uma, comparadas com os dados da plataforma

| # | Orientação | O que os dados da plataforma dizem | Conclusão |
|---|---|---|---|
| P1 | Responder às quatro perguntas, uma em cada parágrafo | As quatro provas seguem mais ou menos esse plano. Os textos que usam as palavras do tema e das perguntas tiveram Tangenciamento e Abrangência maiores (T-lex, H-A9) | **Converge.** Enfraquece a afirmação do relatório 001 de que seguir o plano induz ao tangenciamento: o 7,1 da 001 se explica melhor pela falta das palavras do tema |
| P2 | Cada resposta precisa ser pertinente à questão central, e não uma resposta solta | A Tangenciamento sobe quando o texto retoma a frase do tema | **Converge.** Cada parágrafo deve responder à sua pergunta *em função do* recorte |
| P3 | O dado precisa provar a afirmação. Exemplo: endividamento não prova consumismo, porque muitas famílias se endividam com itens básicos | A plataforma não pune isso de forma visível: a 004 usou o dado da CNC e teve a mesma Abrangência da 003 | **Falha lógica real** (um corretor humano e o ENEM cobram na C3). Atinge a redação 004 e o texto C1 do assistente, que usa a inadimplência da Serasa como sinal de consumismo ("revela parte desse problema") |
| P4 | Não usar "modernidade líquida" nem outro repertório de bolso do ENEM | A 004 (com Bauman) e a 003 (sem repertório) tiveram a mesma Abrangência, 2,4: o repertório de bolso não deu vantagem | **Converge na prática:** para a plataforma não ajuda; para a professora, pesa contra. Atinge textos do assistente: C1 (Bauman), X9 (Paulo Freire), M3 e M4 (Hans Jonas), M2 (*Laudato Si'*) |
| P5 | Nenhuma lacuna, nenhuma ponta solta; toda a argumentação ligada às perguntas | Coincide com o método de amarração (`ferramentas/verificar_amarracao.py`) | **Converge** |

## O que muda no método

1. **Estrutura:** um parágrafo por pergunta da proposta, cada um aberto com as palavras da própria pergunta e
   fechado com a ligação ao recorte. Isso atende à professora (P1, P2) e às hipóteses lexicais da plataforma
   (H-A9, T-lex).
2. **Prova:** cada dado deve demonstrar exatamente a afirmação que sustenta. Antes de usar um número, pergunte: este
   dado prova *isto*, ou prova algo vizinho? (P3)
3. **Repertório:** nada de repertório de bolso (Bauman, Freire, Jonas, Kant, Platão, "modernidade líquida"…). Use só
   referências específicas do problema, ou nenhuma. A plataforma não recompensa repertório; a professora o
   penaliza. (P4)
