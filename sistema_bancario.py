def depositar(saldo, extrato):
    valor = float(input('Informe o valor do depósito: '))

    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
    else:
        print('Operação não realizada, o valor inserido é inválido')

    return saldo, extrato


def sacar(saldo, limite, extrato, numero_saques):
    valor = float(input('Informe o valor do saque: '))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('Operação não realizada! Você não possui saldo suficiente.')
    elif excedeu_limite:
        print('Operação não realizada! Você não possui limite suficiente.')
    elif excedeu_saques:
        print('Operação não realizada! Número máximo de saques atingido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('Operação não realizada! O valor informado é inválido.')

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print('\n================= Extrato =================')
    print('Não foram feitas movimentações.' if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print('=============================================')


menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == '2':
        saldo, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques)

    elif opcao == '3':
        exibir_extrato(saldo, extrato)

    elif opcao == '4':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
