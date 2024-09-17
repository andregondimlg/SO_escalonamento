# O algoritmo FIFO (First In, First Out), ou "primeiro a entrar, primeiro a sair"
class Fila:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    
    def remover(self):
        if self.is_empty():
            return "A fila está vazia"
        return self.itens.pop(0)  

    def primeiro(self):
        if self.is_empty():
            return "A fila está vazia"
        return self.itens[0]

    def is_empty(self):
        return len(self.itens) == 0

    def print_fila(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", " -> ".join(str(item) for item in self.itens))

fila = Fila()

while True :
    valor = input('Adicione um valor na fila')
    fila.adicionar(valor)

    termina = input('Parar de adicionar? s ou n')

    if termina == 's':
        break

fila.print_fila()

print(f"Desenfileirado: {fila.remover()}")

fila.print_fila()

print(f"Primeiro da fila: {fila.primeiro()}")
