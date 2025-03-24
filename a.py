
print('qnt vc recebe por mes?')
salario=int(input('responda aqui '))

numeros = 0
despesa = []  # Lista vazia para armazenar despesas
numero_final = 0  # Será atualizado com a quantidade de despesas


def despesas():
    global numeros, numero_final  # Permite modificar as variáveis globais
    print('O que você gastou hoje?')    
    resposta = input('Responda aqui: ')
    despesa.append(float(resposta))  # Adiciona um novo item na lista

    print('Terminou?')
    print('SIM (y)')
    print('NÃO (n)')
    fim = input('Responda aqui: ')

    if fim == 'y':
        numero_final = numeros + 1  # Salva quantos itens foram adicionados
        final()
    else:
        numeros += 1  # Incrementa para o próximo índice
        despesas()  # Chama novamente para continuar adicionando


def final():
    total = 0  # Inicializa a variável total antes do loop
    print("\nResumo das despesas:")
    
    for i in range(numero_final):
        total += despesa[i]  # Soma cada despesa ao total
        print(f"Despesa {i + 1}: R$ {despesa[i]:.2f}")  # Formata para 2 casas decimais
    
    print(f"\nTotal gasto: R$ {total:.2f}")  # Exibe o total
    porcentagem_perdida= (total / salario) * 100
    print(f'vc perdeu {porcentagem_perdida:.2f}%')
    seu_din=total-salario
    if total>salario:
        print(f'vc deve {seu_din*1} reais')
    else:
        print(f'vc tem {seu_din*-1} reais')


despesas()  # Inicia o programa

