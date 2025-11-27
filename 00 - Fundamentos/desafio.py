menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


#Primeira parte do problema: Criar as funções para as operações existentes:Sacar, Depositar e Visualizar extrato
def sacar(valor):
    global saldo
    global extrato
    global numero_saques 


    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")



def depositar(valor):
    if valor > 0:
        global saldo
        global extrato 
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return

def visualizar_historico(saldo, extrato):     
    pass



#Segnda parte do problema: Criar as funções para criar usuário e criar conta bancária corrente
def cadatrar_usuario():
    pass

def cadastrar_conta():
    pass    












while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

        

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
