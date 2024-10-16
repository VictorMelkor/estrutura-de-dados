class Produto:
    def __init__(self, id, nome, quantidade):
        self.id = id              # ID do produto
        self.nome = nome          # Nome do produto
        self.quantidade = quantidade  # Quantidade em estoque


class Node:
    def __init__(self, produto):
        self.produto = produto    # Produto armazenado no nó
        self.esquerda = None      # Filho à esquerda
        self.direita = None       # Filho à direita


class ArvoreProduto:
    def __init__(self):
        self.raiz = None          # Raiz da árvore

    def inserir(self, id, nome, quantidade):
        novo_produto = Produto(id, nome, quantidade)  # Cria um novo produto
        if self.raiz is None:
            self.raiz = Node(novo_produto)            # Define o produto como raiz se a árvore estiver vazia
            return "Produto inserido como raiz."
        else:
            return self._inserir(novo_produto, self.raiz)  # Chama o método privado para inserir

    def _inserir(self, produto, no):
        if produto.id < no.produto.id:  # Se o ID do produto for menor que o ID do nó atual
            if no.esquerda is None:      # Se não houver filho à esquerda
                no.esquerda = Node(produto)  # Adiciona o produto à esquerda
                return "Produto inserido à esquerda do ID {}".format(no.produto.id)
            else:
                return self._inserir(produto, no.esquerda)  # Recursivamente insere na subárvore esquerda
        elif produto.id > no.produto.id:  # Se o ID do produto for maior que o ID do nó atual
            if no.direita is None:         # Se não houver filho à direita
                no.direita = Node(produto)  # Adiciona o produto à direita
                return "Produto inserido à direita do ID {}".format(no.produto.id)
            else:
                return self._inserir(produto, no.direita)  # Recursivamente insere na subárvore direita
        else:
            # ID já existe, atualiza as informações
            no.produto.nome = produto.nome
            no.produto.quantidade = produto.quantidade
            return "Produto atualizado."

    def buscar(self, id):
        return self._buscar(id, self.raiz)  # Chama o método privado para buscar

    def _buscar(self, id, no):
        if no is None:
            return None  # Retorna None se o nó atual é vazio
        if id == no.produto.id:
            return no.produto  # Retorna o produto se o ID for encontrado
        elif id < no.produto.id:
            return self._buscar(id, no.esquerda)  # Busca na subárvore esquerda
        else:
            return self._buscar(id, no.direita)  # Busca na subárvore direita

    def listar(self):
        produtos = []  # Lista para armazenar produtos
        self._listar(self.raiz, produtos, "Raiz")  # Inicia a listagem a partir da raiz
        return produtos  # Retorna a lista de produtos

    def _listar(self, no, produtos, branch):
        if no is not None:
            # Visita a subárvore esquerda
            self._listar(no.esquerda, produtos, "Esquerda")
            # Adiciona o produto na lista com a informação da branch
            produtos.append((no.produto, branch))
            # Visita a subárvore direita
            self._listar(no.direita, produtos, "Direita")


# Exemplo de uso:
arvore = ArvoreProduto()
print(arvore.inserir(5000, "Produto A", 10))  # Insere Produto A
print(arvore.inserir(1001, "Produto B", 5))   # Insere Produto B
print(arvore.inserir(1553, "Produto C", 20))  # Insere Produto C
print(arvore.inserir(5115, "Produto D", 15))  # Insere Produto D

# Atualizando um produto existente
print(arvore.inserir(2, "Produto B Atualizado", 15))  # Atualiza nome e quantidade do  Produto B

# Listando todos os produtos com suas branches
produtos_listados = arvore.listar()
for produto, branch in produtos_listados:
    print(f'ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}, Branch: {branch}')
