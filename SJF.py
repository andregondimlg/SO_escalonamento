#SJF
# Classe para representar um processo
class Processo:
    def __init__(self, id, tempo_execucao):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.tempo_espera = 0  

def sjf(processos):
    processos.sort(key=lambda processo: processo.tempo_execucao)

    tempo_total = 0
    tempo_espera_total = 0

    print("Ordem de execução dos processos:")

    for index, processo in enumerate(processos):
        print(f"Processo {processo.id} | Tempo de Execução: {processo.tempo_execucao}")

        if index > 0:
            processo.tempo_espera = tempo_total

        tempo_total += processo.tempo_execucao
        tempo_espera_total += processo.tempo_espera

    tempo_medio_espera = tempo_espera_total / len(processos)
    print(f"\nTempo Médio de Espera: {tempo_medio_espera:.2f} unidades de tempo")

id = 1
processos = []
while True :
    valor = int(input('Adicione um tempo de execução para o processo: '))

    processos.append(Processo(id, valor))

    termina = input('Parar de adicionar? s ou n: ')
    id += 1

    if termina == 's':
        break


sjf(processos)
