#ROBIN

class Processo:
    def __init__(self, id, tempo_execucao):
        self.id = id
        self.tempo_execucao = tempo_execucao

def round_robin(processos, quantum):
    fila = processos.copy()
    tempo_total = 0 

    print("Ordem de execução dos processos:")
    while fila:
        processo_atual = fila.pop(0)  

        
        if processo_atual.tempo_execucao > quantum:
            
            print(f"Processo {processo_atual.id} executado por {quantum} unidades de tempo.")
            processo_atual.tempo_execucao -= quantum  
            fila.append(processo_atual)  
            tempo_total += quantum
        else:
            
            print(f"Processo {processo_atual.id} executado por {processo_atual.tempo_execucao} unidades de tempo (completo).")
            tempo_total += processo_atual.tempo_execucao

    print(f"\nTempo total de execução: {tempo_total} unidades de tempo")


id = 1
processos = []
while True :
    valor = int(input('Adicione um tempo de execução para o processo: '))

    processos.append(Processo(id, valor))

    termina = input('Parar de adicionar? s ou n: ')
    id += 1

    if termina == 's':
        break


quantum = 3

round_robin(processos, quantum)
