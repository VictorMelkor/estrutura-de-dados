# Desafio #7DaysOfCode Alura - Estrutura de Dados
Este projeto faz parte dos meus estudos de Estruturas de Dados.

## Dia 1: Arrays - Lista de Compras
O desafio para o dia é implementar uma versão simplificada de uma lista de compras usando arrays. A lista deve permitir adicionar novos itens, remover itens e listar todos os itens.
Ao adicionar um novo item, o usuário deve inserir o nome do produto e a quantidade desejada. Ao remover um item, o usuário deve especificar o nome do produto. Por fim, ao listar todos os itens, a lista deve exibir o nome do produto e a quantidade em um formato legível.

• Solução do Orientador: https://github.com/alura-cursos/7daysofcode-estruturas-de-dados/blob/dia-01/arrays.py

• Minhas observações: Minha solução ficou extremamente maior. Embora eu tenha tentado criar uma ferramenta interativa mais complexa, no que tange à classe 'ListaDeCompras' meu código ficou repetitivo e extenso. Embora eu tenha tentado implementar algo mais completo, percebo que posso reduzir meu código e aplicar o DRY com a mesma efetividade.

## Dia 2: Listas Encadeadas - Lista de Pacientes
O desafio para o dia de hoje é implementar um sistema de gerenciamento de pacientes em um hospital usando listas simplesmente encadeadas.
Cada paciente deve ter um nome, um número de identificação e o estado de saúde atual do paciente, como “estável”, “em tratamento intensivo”, “em estado crítico”, entre outros.
O sistema deve permitir adicionar novos pacientes, remover pacientes e listar todos os pacientes em ordem de chegada.

• Solução do Orientador: https://github.com/alura-cursos/7daysofcode-estruturas-de-dados/tree/dia-02

• Minhas observações: Atividade difícil para meu nível de aprendizado, que serviu como introdução às listas encadeadas. Foi necessário pesquisar bastante para entender o funcionamento dos ponteiros e chegar a uma conclusão que funcionasse. Creio ter mantido o código mais limpo dessa vez, comparando com o código do Dia 1, mas assumo que a resolução das funções adicionar e remover pacientes ainda está confusa em minha cabeça. Fiz duas versões, conforme solicitado no desafio, sendo uma com head e tail, na qual usei o id do paciente como forma de afetar a lista para as remoções; e outra, apenas com head, usando o estado de saúde para a remoção de pacientes, pois achei que seria válido considerar isso também como regra de negócio, já que pacientes estáveis teoricamente estão prontos para serem dispensados.

## Dia 3: Listas duplamente encadeadas - Controle de Estoque
O desafio para o dia é implementar um sistema de controle de estoque de uma loja usando listas duplamente encadeadas.
Cada produto deve ter um nome, um código de barras, um preço e uma quantidade em estoque.

• Solução do Orientador: 

• Minhas observações: Embora o nível de dificuldade tenha aumentado, meus estudos me trouxeram mais tranquilidade ao finalmente entender como manipular o ponteiro entre head e tail. Sinto-me orgulhoso de ter conseguido finalizar este exercício, ainda que tenha sido necessário várias pesquisas e tentativas. Reconheço a evolução, ainda que lenta e me sinto preparado (e ansioso) para o próximo desafio.