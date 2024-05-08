menu = """

[d] = Depósito
[s] = Saque
[e] = Extrato
[q] = Sair

=>"""

saldo = 0
extrato = ""
total_saque = 0
SAQUE_MAX = 3

while True:
    operacao = input(menu)

    if operacao == "d":
        valor =float(input("Digite o valor de depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado! Saldo: R$ {saldo:.2f}")        
        else:
            print("Operação inválida! O valor digitada não é válido")
        

    elif operacao == "s":
        valor = float(input("Digite o valor que deseja sacar: R$ "))

        valor_valido = valor > saldo
        valor_max = valor > 500
        saque_permitido = total_saque >= SAQUE_MAX

        if valor_valido:
            print("Operação inválida! Você não tem saldo suficiente")
        elif valor_max:
            print("Operação inválida! O valor passou do limite de saque")
        elif saque_permitido:
            print("Operação inválida! Limite de saque diário atingido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            total_saque += 1
            print(f"Saque realizado! Saldo: R$ {saldo:.2f}\n")
        else:
            print("Operação inválida! O valor digitada não é válido")

    elif operacao == "e":
        print(f"\n =============================Extrato===============================\n")
        print("Não houve movimentação" if not extrato else extrato)
        print()
        print(f"Saldo: R$ {saldo:.2f}\n")
        print(f"\n ===================================================================")

    elif operacao == "q":
        print("Obrigado por utilizar nosso sistema")
        break
    else:
        print("Operação inválida! Por favor digite uma operação válida!")

    

    