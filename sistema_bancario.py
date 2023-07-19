menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

# Variáveis iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    # Exibir o menu e receber a opção do usuário
    opcao = input(menu)

    # Opção 1 - Depositar
    if opcao == "1":
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Desculpe, não é possível depositar um valor negativo ou zero.')

    # Opção 2 - Sacar
    elif opcao == '2':
        valor = float(input('Informe o valor do saque: '))
        if valor > 0:
            if valor > saldo:
                print('Desculpe, você não tem saldo suficiente para fazer o saque.')
            elif valor > limite:
                print('Desculpe, você não pode sacar um valor maior que o limite.')
            elif numero_saques > LIMITE_SAQUES:
                print('Desculpe, você atingiu o limite máximo de saques por dia.')
            else:
                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                numero_saques += 1
        else:
            print('Desculpe, você só pode sacar valores maiores que zero.')

    # Opção 3 - Extrato
    elif opcao == '3':
        print('\n================= Extrato =================')
        if not extrato:
            print('Desculpe, não há movimentações no extrato ainda.')
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print('=============================================')

    # Opção 4 - Sair
    elif opcao == '4':
        break

    
    else:
        print('Desculpe, a opção escolhida é inválida. Por favor, selecione novamente.')
