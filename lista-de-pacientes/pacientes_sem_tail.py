class Paciente:
    def __init__(self, nome, id, estado_saude):
        self.nome = nome
        self.id = id
        self.estado_saude = estado_saude # Condição de saúde do paciente
        self.proximo = None # Ponteiro para o próximo paciente

class ListaDePacientes:
    def __init__(self):
        self.head = None # Inicia a lista vazia

    def adicionar_paciente(self, nome, id, estado_saude):
        novo_paciente = Paciente(nome, id, estado_saude)
        if self.head is None: #Se a lista estiver vazia...
            self.head = novo_paciente # O novo paciente inicia a lista
        else: #Se a lista não estiver vazia...
            atual = self.head 
            while atual.proximo: # Percorre a lista até o final...
                atual = atual.proximo
            atual.proximo = novo_paciente # Adiciona o novo paciente ao fim da lista

    def remover_paciente(self, estado_saude):
        atual = self.head
        anterior = None

        while atual is not None:
            if atual.estado_saude == estado_saude:
                if anterior is None:
                    self.head = atual.proximo # O paciente pra ser removido é o head
                else:
                    anterior.proximo = atual.proximo # remove o nó da lista
                print(f"Paciente com estado '{estado_saude}' removido.")
                return #paciente encontrado e removido
            anterior = atual
            atual = atual.proximo
        
        print(f"Paciente com estado '{estado_saude}' não encontrado.")

    def listar_pacientes(self):
        atual = self.head
        if atual is None:
            print('A lista de pacientes está vazia.')
            return
        while atual:
            print(f"Nome: {atual.nome} | id: {atual.id} | Estado de Saúde: {atual.estado_saude}")
            atual = atual.proximo

#Testando a implementação
lista = ListaDePacientes()

# Adicionando pacientes
print("Adicionando pacientes:")
lista.adicionar_paciente("João", 30, "Estável")
lista.adicionar_paciente("Maria", 25, "Crítico")
lista.adicionar_paciente("José", 40, "Tratamento Intensivo")

# Listando pacientes
print("\nLista de pacientes:")
lista.listar_pacientes()

# Removendo um paciente
print("\nRemovendo paciente com estado 'Crítico':")
lista.remover_paciente("Crítico")

# Listando novamente
print("Lista de pacientes após remoção:")
lista.listar_pacientes()

# Tentando remover um paciente que não existe
print("\nTentando remover paciente com estado 'Desconhecido':")
lista.remover_paciente("Desconhecido")

# Removendo o primeiro paciente
print("\nRemovendo paciente com estado 'Estável':")
lista.remover_paciente("Estável")

# Listando pacientes novamente
print("Lista final de pacientes:")
lista.listar_pacientes()

# Removendo o último paciente
print("\nRemovendo paciente com estado 'Tratamento Intensivo':")
lista.remover_paciente("Estável")

# Listando pacientes novamente
print("Lista final de pacientes após remoção:")
lista.listar_pacientes()