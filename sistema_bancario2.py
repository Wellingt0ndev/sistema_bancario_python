import textwrap

def menu():
    menu = """
    ================ MENU ================
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nc]\tNova conta    
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\t\tSair do Sistema 
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"== Depósito realizado! Saldo: R$ {saldo:.2f} ==")
    else:
        print("## Operação inválida! O valor digitado não é válido ##")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor_valido = valor > saldo
    valor_max = valor > 500
    saque_permitido = numero_saques >= limite_saques

    if valor_valido:
        print("Operação inválida! Você não tem saldo suficiente")
    elif valor_max:
        print("Operação inválida! O valor passou do limite de saque")
    elif saque_permitido:
        print("Operação inválida! Limite de saque diário atingido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque realizado! Saldo: R$ {saldo:.2f}\n")
    else:
        print("Operação inválida! O valor digitado não é válido")
    return saldo, extrato

def exibir_extrato(saldo, /,*, extrato):
    print(f"\n =============================Extrato===============================\n")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print(f"\n ===================================================================")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF(somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n ## Já existe usuário com esse CPF! ##")
        return
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite o data de nascimento(dd-mm-aaaa): ")
    endereco = input("Digite o endereço(logradouro, nº - bairro - cidade/UF): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})
    print("== Usuário criado com sucesso! ==")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF(somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n == Conta criada com sucesso! ==")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    print("\n## Usuário não encontrado, criação de conta encerrada! ##")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta["usuario"]["nome"]}        
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1
    while True:
        operacao = menu()
        if operacao == "d":
            valor = float(input("Digite o valor de depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif operacao == "s":
            valor = float(input("Digite o valor que deseja sacar: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITES_SAQUES
            )
        elif operacao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif operacao == "nu":
            criar_usuario(usuarios)
        elif operacao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
        elif operacao == "lc":
            listar_contas(contas)
        elif operacao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()



    

    
