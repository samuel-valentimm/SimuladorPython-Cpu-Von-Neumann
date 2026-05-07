# Memória com 100 posições com início em 0
memoria = [0] * 100

# Função para escrever na memória
def escrever_memoria(endereco, valor):
    if 0 <= endereco < len(memoria):
        memoria[endereco] = valor
    else:
        print(f'Endereço {endereco} fora do alcance da memória.')

# Função para ler a memória
def ler_memoria(endereco):
    if 0 <= endereco < len(memoria):
        return memoria[endereco]
    else:
        print(f'Endereço {endereco} inválido!')

# Registradores (CPU)
ACC = 0 # Acumulador
PC = 0 # Program Counter

# CONJUNTO DE INSTRUÇÕES (ISA)
# 10: LOAD - Carrega um valor da memória para o ACC
# 20: ADD - Soma o valor da memória ao ACC atual
# 30: STORE - Armazena o valor do ACC em um endereço da memória
# 0: HALT - Para a execução do programa

# Entrada do opcode e dos dados 
proximo_end = 0
while proximo_end < 100:
    try: 
        op = input(f'Endereço [{proximo_end}] - Opcode: ')
        opcode = int(op)
        escrever_memoria(proximo_end, opcode)

        if opcode == 0: break # HALT
        
        proximo_end += 1 # Carrega o Dado na próxima posição
        dado = int(input(f'Endereço [{proximo_end}] - Dado: '))
        escrever_memoria(proximo_end, dado)
        proximo_end += 1 # Avança para o próximo par

    except ValueError:
        print('Entrada inválida! Digite apenas números.')

# Execução do Programa
while True:
    # FETCH - Busca a instrução no endereço que PC indicar
    instrucao = ler_memoria(PC)
    
    match instrucao:
        case 10: # LOAD - Pega o valor do proximo_end para o ACC
            ACC = ler_memoria(PC + 1) # Lê proximo_end e guarda em ACC
            print(f'Executando LOAD: ACC = {ACC}')
            PC += 2 # PC += 2 garante que o ciclo de instrução lera Opcode e Dado 

        case 20: # ADD - Soma o proximo_end com o ACC
            valor_soma = ler_memoria(PC + 1) # Lê o valor a ser somado
            ACC += valor_soma # Atualiza o ACC com a soma
            print(f'Executando ADD: Somando {valor_soma}, ACC = {ACC}')
            PC += 2

        case 30: # STORE - Salva o novo ACC no endereco do PC + 1
            endereco_destino = ler_memoria(PC + 1) # Vê em qual endereço o resultado será salvo
            escrever_memoria(endereco_destino, ACC) # Guarda ACC no endereço escolhido
            print(f'Executando STORE: Salvando {ACC} no endereço {endereco_destino}')
            PC += 2

        case 0: # HALT - Para a execução do programa
            print('Execução finalizada via Opcode 0 (HALT)')
            break
        
        case _: # Segurança caso Opcode nao seja definido
            print(f'Erro: Instrução inválida {instrucao} no PC {PC}')
            break
