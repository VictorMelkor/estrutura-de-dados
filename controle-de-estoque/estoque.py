class Produto:
    def __init__(self, nome, codigo_barras, preco, quantidade):
        self.nome = nome
        self.codigo_barras = codigo_barras
        self.preco = preco
        self.quantidade = quantidade
        self.proximo = None #ponteiro para o próximo nó
        self.anterior = None #Ponteiro para o nó anterior

class ListaDeProdutos:
    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar_produto(self, nome, codigo_barras, preco, quantidade):
        novo_produto = Produto(nome, codigo_barras, preco, quantidade)
        if self.head is None: # se a lista está vazia, novo_produto se torna head e tail
            self.head = novo_produto
            self.tail = novo_produto
        else:                       # se a lista já tiver itens:
            self.tail.proximo = novo_produto #  percorre a lista buscando um tail None e aloca o novo produto no fim da lista
            novo_produto.anterior = self.tail # indica ao penultimo item da lista que o novo produto é o ultimo (encadeamento)
            self.tail = novo_produto # referencia o produto ao fim da lista

    def remover_produto(self, nome):
        atual = self.head #ponteiro que vai percorrer a lista, mostrando o item atual que está sendo verificado
        
        while atual: #enquanto a lista tiver itens
            if atual.nome == nome: # se o nome informado constar na lista
                if atual.anterior: #se tem anterior, não é o head
                    atual.anterior.proximo = atual.proximo
                if atual.proximo: #se tem próximo, não é o tail
                    atual.proximo.anterio = atual.anterior
                if atual == self.head: #se for o head
                    self.head = atual.proximo
                if atual == self.tail: #se for o tail
                    self.tail = atual.anterior
                return True
            atual = atual.proximo        
        print(f'O produto {nome} não está na lista') # se a lista estiver vazia ou não houver o produto na lista
        return False

    def atualizar_produto(self, nome, novo_preco, nova_quantidade):
        if nova_quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        atual = self.head
        while atual:
            if atual.nome == nome:
                atual.quantidade = nova_quantidade
                atual.preco = novo_preco
                return True
            atual = atual.proximo
        return False

    def listar_produtos(self):
        atual = self.head
        print(f'{"PRODUTO":<20}{"CÓDIGO DE BARRAS":<20}{"PREÇO":<15}{"QUANTIDADE":<10}')
        print('-'*70)
        if atual is None:
            print("A lista de pacientes está vazia.")
            return
        while atual:
            print(f"{atual.nome:<20}{atual.codigo_barras:<20}R${atual.preco:<15}{atual.quantidade:<10}")
            atual = atual.proximo

lista = ListaDeProdutos()

print('Adicionando produtos')
lista.adicionar_produto('Arroz', 123456, 17.50, 2)
lista.adicionar_produto('Feijão', 654321, 5.75, 1)
print()

print('Listando produtos:')
lista.listar_produtos()
print()

print('Removendo produtos')
lista.remover_produto('Arroz')
print()

print('Listando produtos:')
lista.listar_produtos()
print()

print('Adicionando produtos')
lista.adicionar_produto('Arroz', 123456, 17.50, 2)

print('Listando produtos:')
lista.listar_produtos()
print()

print('Alterando preço e quantidade')
lista.atualizar_produto('Feijão', 21.50, 6)
print()

print('Listando produtos:')
lista.listar_produtos()
print()

print('Removendo produtos que não estão na lista')
lista.remover_produto('Cenoura')
print()