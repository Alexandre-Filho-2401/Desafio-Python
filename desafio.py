import sys
#Armazenamento dos dados de Usuario
users = {}

cpfEmUso = ""

#Funcoes de acesso
def criaUser():
    n = input("\nInsira Nome: ")
    i = int(input("Insira Idade: "))
    c = input("Insira CPF: ")
    s = input("Crie uma Senha: ")
    
    if c in users:
        print("Usurio j existe")
        menu1()
    x = users.update({c: {"nome":n,"idade":i,"senha":s, "contas":{}}})

    return x, menu1()

def acessaConta():
    global cpfEmUso
    cpfEmUso = input("\nInsira seu CPF: ")
    s = input("Insira sua senha: ")
    if cpfEmUso not in users or s not in users[cpfEmUso]["senha"]:
        print("CPF ou senha invalido, tente novamente")
        menu1()
    menu2()

#Funcoes menu
def criaConta():
    global conta
    v = input("\nInsira seu CPF: ")
    vS = input("Insira sua Senha: ")
    
    if v not in users or vS not in users[v]["senha"]:
        print("CPF ou senha invalido, tente novamente")
        criaConta()
    conta = input("De um nome a sua conta: ")
    return users[v]["contas"].update({conta: {"saldo":0,"saqD":0,"extrato":[]}}), menu2()

def deposito():
    global cpfEmUso
    c = input("\nEm que conta deseja depositar? ")
    if c not in users[cpfEmUso]["contas"]:
        print("Conta nao encontrada")
        deposito()
    d = float(input("Insira o valor do deposito: "))
    users[cpfEmUso]["contas"][c]["extrato"].append(f"+R${d:.2f}")
    users[cpfEmUso]["contas"][c]["saldo"] += d
    print(f"R${d:.2f} foi depositado")
    menu2()
    
def saque():
    global cpfEmUso
    c = input("\nDe qual conta deseja sacar? ")
    if c not in users[cpfEmUso]["contas"]:
        print("Conta nao encontrada")
        saque()
    e = float(input("Insira valor do saque: "))
    if e > users[cpfEmUso]["contas"][c]["saldo"]:
        print("Saldo insuficiente")
        menu2()
    if e > 1000:
        print("Limite de saque excedido")
        saque()
    elif users[cpfEmUso]["contas"][c]["saqD"] >= 3:
        print("Limite de saques diarios atingido")
        menu2()
    users[cpfEmUso]["contas"][c]["extrato"].append(f"-R${e:.2f}")
    users[cpfEmUso]["contas"][c]["saldo"] -= e
    users[cpfEmUso]["contas"][c]["saqD"] += 1
    print(f"R${e:.2f} foi retirado")
    menu2()
    
def extrato():
    c = input("Deseja ver o extrato de qual conta? ")
    if c not in users[cpfEmUso]["contas"]:
        print("Conta nao encontrada")
        extrato()
    print("======= Transacoes: =======")
    for t in users[cpfEmUso]["contas"][c]["extrato"]:
        print(t)
    print("Saldo: R$" + str(users[cpfEmUso]["contas"][c]["saldo"]))
    print("===========================")
    menu2()
 
#Menus
def menu1():
    
    print("\n=======================")
    print("\n[1]Entrar")
    print("[2]Cadastrar Usuario")
    print("[0]Sair")
    print("\n=======================")
    op = int(input(">> "))
    
    if op == 1:
        acessaConta()
    elif op == 2:
        criaUser()
    elif op == 0:
        sys.exit(0)
    else:
        print("Erro")
        menu1()
        
def menu2():
    print("\n======== MENU ==========")
    print("\n[1]Criar Conta")
    print("[2]Depositar")
    print("[3]Sacar")
    print("[4]Extrato")
    print("[0]Sair")
    print("\n========================")
    op = int(input(">> "))
    if op == 1:
        criaConta()
    elif op == 2:
        deposito()
    elif op == 3:
        saque()
    elif op == 4:
        extrato()
    elif op == 0:
        print("Deslogando")
        menu1()
    else:
        print("Erro")
        menu2()

#onde de fato comeca
menu1()
