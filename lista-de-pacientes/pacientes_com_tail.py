class Paciente:
    def __init__(self, nome, id, estado_saude):
        self.nome = nome
        self.id = id
        self.estado_saude = estado_saude  # Estado de saúde do paciente
        self.proximo = None  # Ponteiro para o próximo paciente


class ListaDePacientes:
    def __init__(self):
        self.head = None  # Inicia a lista vazia
        self.tail = None    # Ponteiro para o final da lista

    def adicionar_paciente(self, nome, id, estado_saude):
        novo_paciente = Paciente(nome, id, estado_saude)
        if self.head is None:
            # Se a lista estiver vazia, o novo paciente se torna a cabeça e o tail
            self.head = novo_paciente
            self.tail = novo_paciente
        else:
            # Adiciona o novo paciente ao final da lista
            self.tail.proximo = novo_paciente
            self.tail = novo_paciente  # Atualiza o tail

    def remover_paciente(self, id):
        atual = self.head
        anterior = None
        
        while atual is not None:
            if atual.id == id:
                if anterior is None:
                    # O paciente a ser removido é a cabeça
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo  # Remove o nó da lista
                
                # Se o paciente removido for o tail, atualiza o tail
                if atual == self.tail:
                    self.tail = anterior
                
                print(f"Paciente com ID {id} removido.")
                return  # Paciente encontrado e removido
            anterior = atual
            atual = atual.proximo
        
        print(f"Paciente com ID {id} não encontrado.")

    def listar_pacientes(self):
        atual = self.head
        if atual is None:
            print("A lista de pacientes está vazia.")
            return
        while atual:
            print(f"Nome: {atual.nome}, ID: {atual.id}, Estado de Saúde: {atual.estado_saude}")
            atual = atual.proximo


# Testando a implementação
lista = ListaDePacientes()

# Adicionando pacientes
print("Adicionando pacientes:")
lista.adicionar_paciente("João", 1, "Estável")
lista.adicionar_paciente("Maria", 2, "Tratamento Intensivo")
lista.adicionar_paciente("José", 3, "Crítico")

# Listando pacientes
print("\nLista de pacientes:")
lista.listar_pacientes()

# Removendo um paciente
print("\nRemovendo paciente com ID 2:")
lista.remover_paciente(2)

# Listando novamente
print("Lista de pacientes após remoção:")
lista.listar_pacientes()

# Tentando remover um paciente que não existe
print("\nTentando remover paciente com ID 4:")
lista.remover_paciente(4)

# Removendo o primeiro paciente
print("\nRemovendo paciente com ID 1:")
lista.remover_paciente(1)

# Listando pacientes novamente
print("Lista final de pacientes:")
lista.listar_pacientes()

# Removendo o último paciente
print("\nRemovendo paciente com ID 3:")
lista.remover_paciente(3)

# Listando pacientes novamente
print("Lista final de pacientes após remoção:")
lista.listar_pacientes()
