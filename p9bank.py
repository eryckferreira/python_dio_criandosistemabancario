saldo = 0
limite = 500
extrato = ""
numeroDeSaques = 0
limiteDeSaques = 3

while True:
    
    print("==============================")
    print("  Bem-vindo ao P9 Bank!  ")
    print("==============================")
    print("Por favor, selecione uma das opções abaixo:")
    print("[d] Depósito   - Adicione dinheiro à sua conta")
    print("[s] Saque      - Retire dinheiro da sua conta")
    print("[e] Extrato    - Veja o extrato de sua conta")
    print("[q] Sair       - Encerre a sessão")
    print("==============================")
    opcao = input("Selecione uma opção: ")

    if opcao == "d":
        valor = float(input("Informe o valor do Depósito: R$"))

        if valor >= 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("Operação falhou! o Valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numeroDeSaques >= limiteDeSaques

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numeroDeSaques += 1

        else:
            print("Operação falhou! o valor informado é inválido.")

    elif opcao == "e":
        print("======================== EXTRATO ========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("=========================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
