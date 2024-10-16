class Jogo:
    def __init__(self):
        self.pontuacoes = {} # dicionário para armazenar os jogadores (key) e pontuações (values)

    def adicionar_jogador(self, nome_jogador):
        if nome_jogador not in self.pontuacoes:
            self.pontuacoes[nome_jogador] = 0
            print('-'*50)
            print(f"Jogador '{nome_jogador}' adicionado com sucesso.")
        else:
            print('-'*50)
            print(f'Já existe um jogador com nome {nome_jogador}')


    def atualizar_pontuacao(self, nome_jogador, pontos):
        if nome_jogador in self.pontuacoes:
            self.pontuacoes[nome_jogador] += pontos
            print('-'*50)
            print(f'Pontuação de {nome_jogador} atualizada para {self.pontuacoes[nome_jogador]}.')
            print('-'*50)
        else:
            print('-'*50)
            print(f'Não existe um jogador com nome {nome_jogador}')

    def remover_jogador(self, nome_jogador):
        if nome_jogador in self.pontuacoes:
            del self.pontuacoes[nome_jogador]
            print('-'*50)
            print(f"Jogador '{nome_jogador}' removido com sucesso.")
        else:
            print('-'*50)
            print(f'Não existe um jogador com nome {nome_jogador}')

    def listar_jogadores_por_pontuacao(self):
        print('-'*50)
        print('Jogadores em ordem decrescente de pontos: ')
        for jogador, pontos in sorted(self.pontuacoes.items(), key=lambda item: item[1], reverse=True):
            print(f'{jogador}: {pontos} pontos')
        print('-'*50)

    def vencedor(self):
        if not self.pontuacoes:
            print('-'*50)
            print('Não existem jogadores cadastrados')
        
        vencedor = max(self.pontuacoes, key=self.pontuacoes.get)
        print('-'*50)
        print(f"O vencedor é '{vencedor}' com {self.pontuacoes[vencedor]} pontos.")
        print('-'*50)
        return vencedor

jogo = Jogo()
    
# Adicionando jogadores
jogo.adicionar_jogador("Alice")
jogo.adicionar_jogador("Bob")
jogo.adicionar_jogador("Charlie")

# Atualizando pontuações
jogo.atualizar_pontuacao("Alice", 10)
jogo.atualizar_pontuacao("Bob", 20)
jogo.atualizar_pontuacao("Charlie", 15)

# Listando jogadores
jogo.listar_jogadores_por_pontuacao()

# Verificando vencedor
jogo.vencedor()

# Removendo um jogador
jogo.remover_jogador("Bob")
jogo.listar_jogadores_por_pontuacao()