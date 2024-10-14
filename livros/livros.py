class Livro:
    def __init__(self, titulo, ano, num_paginas):
        self.titulo = titulo
        self.ano = ano
        self.num_paginas = num_paginas

    def __str__(self):
        return f"{self.titulo} | Ano: {self.ano} | {self.num_paginas} páginas"    

class PilhaDeLivros:
    def __init__(self):
        self.pilha_de_livros = []

    def adicionar_livro(self, titulo, ano, num_paginas): #push
        novo_livro = Livro(titulo, ano, num_paginas)
        self.pilha_de_livros.append(novo_livro)
        print(f'Livro "{novo_livro}" adicionado!')

    def remover_livro(self): #pop
        if self.pilha_de_livros:
            livro = self.pilha_de_livros.pop() #remove o ultimo a entrar LIFO
            print(f'Livro removido: {livro}')
        else:
            print('A pilha de livros está vazia.')

    def exibir_peek(self): #peek
        if self.pilha_de_livros:
            print(f'{self.pilha_de_livros[-1]}') # imprime o último da pilha
        else:
            print('A pilha de livros está vazia.')

    def listar_livros(self):
        if not self.pilha_de_livros:
            print('A pilha de livros está vazia.')
        else:
            for livro in self.pilha_de_livros:
                print(livro)

pilha = PilhaDeLivros()

# Adicionando alguns livros
pilha.adicionar_livro("A Guerra dos Tronos (A Game of Thrones)", 1996, 694)
pilha.adicionar_livro("A Fúria dos Reis (A Clash of Kings)", 1998, 768)
pilha.adicionar_livro("A Tormenta de Espadas (A Storm of Swords)", 2000, 1171)
pilha.adicionar_livro("O Festim dos Corvos (A Feast for Crows)", 2005, 753)
pilha.adicionar_livro("A Dança dos Dragões (A Dance with Dragons", 2011, 1016)


# Listando livros
pilha.listar_livros()

# Verificando o livro do topo
pilha.exibir_peek() #deve mostrar o livro "A dança dos dragões"

# Removendo um livro
pilha.remover_livro() #remove o livro "A dança dos dragões"

# Listando livros novamente
pilha.listar_livros() #mostra a pilha sem o livro "A dança dos dragões"

# Removendo todos os livros
pilha.remover_livro()
pilha.remover_livro()
pilha.remover_livro()
pilha.remover_livro()
pilha.remover_livro()  # Deve informar que não há livros

# Listando livros
pilha.listar_livros() # Deve informar que a pilha está vazia