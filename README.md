
Como rodar o código:
    1. Abra a pasta no VsCode selecione e rode o arquivo Mochila.py
    2. Não é necessário digitar os dados de entrada, eles já estão configurados para texte no código. Caso seja necessário alterar os dados de entrada eles necessitam ser alterados diretamente no código.

Como funciona o programa

Uma população inicial é criada aleatoriamente (função `criar_individuo()`).
A função `fitness()` calcula o valor total dos itens selecionados. (se o peso total exceder o limite, o fitness é zero)
A função `selecao()` escolhe indivíduos para reprodução. (indivíduos com maior fitness têm mais chances de serem selecionados.)
A função `cruzamento()` combina dois pais para criar um filho. ( usa o método de cruzamento de ponto único.)
A função `mutacao()` introduz pequenas alterações aleatórias nos indivíduos. (aAjuda a manter a diversidade genética e explorar novas soluções.)
O processo de seleção, cruzamento e mutação é repetido por várias gerações.
Em cada geração, uma nova população é criada.
O melhor indivíduo de cada geração é armazenado.
No final, os 5 melhores resultados únicos são retornados.

Como o algoritmo resolve o problema
Ao criar soluções aleatórias e combiná-las, o algoritmo explora diferentes combinações de itens. A função de fitness avalia quão boa é cada solução, considerando o valor total e o limite de peso. Através da seleção, as melhores soluções têm mais chances de passar seus "genes" para a próxima geração. O cruzamento combina boas soluções, potencialmente criando soluções ainda melhores. A mutação permite pequenas variações, evitando que o algoritmo fique preso em máximos locais. Ao longo das gerações, o algoritmo tende a convergir para soluções que maximizam o valor total dentro do limite de peso. Ao manter e retornar vários resultados únicos, o algoritmo fornece diferentes opções de alta qualidade. A saída do programa é uma lista das melhores soluções encontradas pelo algoritmo genético onde o primeiro número representa o valor total dos itens selecionados para esta solução.  A lista de 0 e 1 representa quais itens foram selecionados para serem colocados na mochila:
   - 1 significa que o item foi selecionado (está na mochila)
   - 0 significa que o item não foi selecionado (não está na mochila)
E por último o peso médio dos itens que foram colocados na mochila.

As soluções estão ordenadas da melhor (maior valor total) para a pior (menor valor total) entre as 5 melhores encontradas.

