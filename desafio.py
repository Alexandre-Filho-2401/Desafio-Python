saldo = 0
saques = 0
LIM_SAQUE = 500
extrato = []

while True:
    print("""
            =====================
            [1] Depositar
            [2] Saque
            [3] Extrato
            [0] Sair
            =====================
            """)
    opcao = input(">> ")

    if opcao == '1':
        deposito = float(input("Quanto deseja depositar?\n>> "))
        saldo += deposito
        extrato.append(f"R${deposito}")
    elif opcao == '2':
        if saques <= 2:
            saque = float(input("Quanto deseja sacar?\n>> "))
            if saque <= LIM_SAQUE:
                saldo -= saque
                extrato.append(f"-R${saque}")
                saques += 1
            else:
                print("Limite para saque excedido.")
        else:
            print("Limite de saques atingido.")
    elif opcao == '3':
        for extrato in extrato:
            print(extrato)
        print(f"Saldo total: R${saldo}")
    elif opcao == '0':
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
