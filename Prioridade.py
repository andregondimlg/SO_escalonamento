#PRIORIDADE

class Processo:
    def __init__(self, id, tempo_execucao, prioridade):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade


def escalonamento_prioridade(processos):
    
    
    processos.sort(key=lambda processo: processo.prioridade)

    tempo_total = 0
    tempo_espera_total = 0

    print("Ordem de execução dos processos (baseado na prioridade):")
    
    
    for processo in processos:
        print(f"Processo {processo.id} | Tempo de Execução: {processo.tempo_execucao} | Prioridade: {processo.prioridade}")
        
        tempo_espera = tempo_total
        tempo_total += processo.tempo_execucao
        tempo_espera_total += tempo_espera
        print(f"Tempo de espera do processo {processo.id}: {tempo_espera} unidades de tempo")

    
    tempo_medio_espera = tempo_espera_total / len(processos)
    print(f"\nTempo Médio de Espera: {tempo_medio_espera:.2f} unidades de tempo")


id = 1
processos = []
while True :
    valor = int(input('Adicione um tempo de execução para o processo: '))
    valor2 = int(input('Adicione uma prioridade para o processo: '))

    processos.append(Processo(id, valor, valor2))

    termina = input('Parar de adicionar? s ou n: ')
    id += 1

    if termina == 's':
        break


escalonamento_prioridade(processos)
