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

• Solução do Orientador: https://github.com/alura-cursos/7daysofcode-estruturas-de-dados/tree/dia-03

• Minhas observações: Embora o nível de dificuldade tenha aumentado, meus estudos me trouxeram mais tranquilidade ao finalmente entender como manipular o ponteiro entre head e tail. Sinto-me orgulhoso de ter conseguido finalizar este exercício, ainda que tenha sido necessário várias pesquisas e tentativas. Reconheço a evolução, ainda que lenta e me sinto preparado (e ansioso) para o próximo desafio.

## Dia 4: Filas - Pedidos de um Restaurante
O desafio para o dia é implementar uma fila simples para gerenciar pedidos de um restaurante. Cada pedido pode ser representado por uma string com o nome do prato e a mesa em que foi feito. O sistema deve permitir adicionar novos pedidos na fila, remover pedidos que já foram entregues e listar todos os pedidos na ordem em que foram feitos.

• Solução do orientador: https://github.com/alura-cursos/7daysofcode-estruturas-de-dados/tree/dia-04

• Minhas observações: Exercício mais fácil, usando arrays. O conceito de filas foi facilmente entendido, bem mais simples de entender do que as listas encadeadas. O exemplo escolhido pelo orientador facilitou o entendimento, sendo a adição e remoção sempre de forma simples e intuitiva. Uma observação importante entre minha solução e a do orientador é a utilização da classe Pedido, que no meu caso, utilizei apenas ao final, na criação da instância, enquanto o orientador o fez dentro do método adicionar_pedido.

## Dia 5 - Pilhas - Pilha de Livros
O desafio do dia é implementar uma pilha simples para gerenciar os livros da saga “As Crônicas de Gelo e Fogo” (Game of Thrones). Cada livro deve ter um nome e o número de páginas. O sistema deve permitir adicionar novos livros na pilha, remover livros, mostrar o livro que está no topo e listar todos os livros da pilha.

• Solução do orientador: https://github.com/alura-cursos/7daysofcode-estruturas-de-dados/tree/dia-05

• Minhas observações: Assim como na fila, o exercício é simples e satisfatório. Sem dificuldades consegui finalizar o código, utilizando os conhecimentos adquiridos nos últimos desafios. Me sinto pronto para o próximo nível.

## Dia 6 - Hashmaps - Pontuação em jogos online
O desafio para o dia de hoje é implementar um sistema de pontuação para jogos online usando uma técnica de hashmap na sua linguagem preferida. Cada jogador terá um nome de usuário e um número de pontos associado, e o sistema deve permitir adicionar novos jogadores, atualizar a pontuação de jogadores existentes, remover jogadores e listar todos os jogadores em ordem decrescente de pontos, além de determinar qual jogador é o vencedor.

• Solução do orientador: https://github.com/alura-cursos/7daysofcode-estruturas-de-dados/blob/dia-06/hash-map.py

• Minhas observações: O exercício é simples, então busquei implementar a função lambda, que acabo de aprender em meus estudos para melhorar meu código. Não houve dificuldade no entendimento e implantação da maior parte das funções, exceto apenas pela listagem decrescente por pontuação, mas que foi resolvido com a aplicação do lambda. Minha solução ficou parcialmente semelhante à do orientador, mas um pouco mais verbosa, principalmente por eu ter adicionado métodos de verificações de inconsistências, como a existência (ou não) de um nome de jogador. Ainda assim, fico satisfeito com o resultado.

## Dia 7 - Árvores - Estoque online
Imagine que você está trabalhando em um sistema de gerenciamento de estoque de uma loja online. Você precisa implementar uma árvore binária que possa armazenar informações sobre os produtos em estoque. Cada nó na árvore deve representar um produto, e deve conter as seguintes informações:
ID do produto (um número inteiro único);
Nome do produto;
Quantidade em estoque,
Sua tarefa é implementar uma função que insere um novo produto na árvore com base no seu ID. A função deve receber como entrada o ID do novo produto, o nome e a quantidade em estoque. Se o ID já existir na árvore, a função deve atualizar as informações do produto.
EXERCÍCIO OPCIONAL
Como um desafio extra, você pode também implementar uma função que realiza a busca por um produto com base no seu ID e retorna suas informações.

• Solução do orientador: 

• Minhas observações: Uma estrutura nova para mim, então, comecei pelos estudos e... tive dificuldades. Assim como nas listas duplamente encadeadas, primeiro tive uma certa dificuldade em entender como o conceito se aplicaria ao código. Depois, entender como direcionar os novos inputs ao lado correto da árvore me deu outro nó na cabeça, mas com pesquisa eu consegui encontrar uma solução. Tive dificuldades, então refiz o exercício mais de uma vez para tentar assimilar tudo, mas creio ainda não ter compreendido com perfeição, então terei que aprofundar mais os estudos desse desafio. Por fim, inseri uma função extra, para listar todos os itens me informando em qual branch ele foi inserido, para fins de melhor entendimento.