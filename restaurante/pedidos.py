class Pedido:
    def __init__(self, numero, nome_cliente, prato, mesa, valor_total):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.prato = prato
        self.mesa = mesa
        self.valor_total = valor_total

    def __str__(self):
        return f'Pedido #{self.numero} | Cliente: {self.nome_cliente} | Mesa: {self.mesa} | Prato: {self.prato} | Valor: R${self.valor_total}'

class FilaDePedidos:
    def __init__(self):
        self.pedidos = []

    def adicionar(self, pedido): #enqueue
        self.pedidos.append(pedido)
        print(f'Pedido adicionado: {pedido}') #adiciona ao fim da lista

    def remover(self): #dequeue
        if self.pedidos:
            pedido = self.pedidos.pop(0) #remove o primeiro item da lista
            print(f'Pedido entregue: {pedido}')
        else:
            print('Nenhum pedido pendente')

    def mostrar_pedidos(self):
        if not self.pedidos:
            print('Não existem pedidos na fila')
        else:
            for pedido in self.pedidos:
                print(pedido)

fila = FilaDePedidos()

# Adicionando alguns pedidos

fila.adicionar(Pedido(1, 'Victor', 'Pastel', 2, 12.50))
fila.adicionar(Pedido(2, 'Gabi', 'Sushi', 5, 65.56))
fila.adicionar(Pedido(3, 'Guilherme', 'Sanduíche', 8, 35.50))

# Listando pedidos
fila.mostrar_pedidos()

# Removendo um pedido
fila.remover()

# Listando pedidos novamente
fila.mostrar_pedidos()

# Removendo todos os pedidos
fila.remover()
fila.remover()
fila.remover() #deve mostrar que não há pedidos

# Listando pedidos
fila.mostrar_pedidos()