menu = """

[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair

 => """

saldo = 0
limite = 500 
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, extrato):

    menu_deposito = "Digite o valor do deposito ou Digite 'q' para voltar ao menu anterio \n\n"

    while True:

        valor = input(menu_deposito)
        
        if valor == "q":
            print("Operação cancelada")
            return saldo, extrato

        try:
            valor_deposito = float(valor)
            
            if valor_deposito <= 0:
                print("Valor invalido, digite o valor novamente")

            else:
                float(valor_deposito)
                saldo += valor_deposito
                extrato += f"Depósito realizado no valor de R$ {valor_deposito:.2f}\n"
                print("\nDeposito realizado, confira seu novo saldo na opção de extrato\n")
                return saldo, extrato

        except ValueError:
            print("Valor invalido, digite um valor ou digite 'q' para sair.")

def sacar(saldo, extrato, numero_de_saques):

    menu_saque = "Digite o valor que deseja retirar ou Digite 'q' para voltar ao menu anterior \n\n"

    while True:
        if saldo <= 0:
            print("Você não possui saldo para sacar")
            break

        valor = input(menu_saque)
        
        if valor == "q":
            print("Operação cancelada")
            return saldo, extrato, numero_de_saques

        try:
            valor_saque = float(valor)

            if valor_saque <= 0:
                print("Valor invalido, digite o valor novamente")
                
            elif valor_saque > 500:
                print("Valor excede o permitido para um unico saque, seu limite por saque é de R$ 500, tente novamente")

            else:
                saldo -= valor_saque
                numero_de_saques += 1 
                extrato += f"Saque realizado no valor de R$ {valor_saque:.2f}\n"
                print("\nSaque realizado, confira seu novo saldo na opção de extrato\n")
                return saldo, extrato, numero_de_saques

        except ValueError:
            print("Valor invalido, digite um valor ou digite 'q' para sair.")

def exibir_extrato(saldo, extrato):
    
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\n==========Extrato==========\n")
        print(extrato, f"\n\nSeu saldo é de R$ {saldo:.2f}")
        print("\n===========================")
        return saldo
    
while True:
    opcao = input(f"Escola uma opcão {menu}")
     
    if opcao == "d":
        print("Depósito\n")
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        if numero_de_saques < LIMITE_SAQUES:
            print("Saque\n")
            saldo, extrato, numero_de_saques = sacar(saldo, extrato, numero_de_saques)
        else:
            print("Numero de saques diarios atingidos")

    elif opcao == "e":
        print("Extrato\n")
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("Saindo")
        break
        
    else :
        print("Opção invalida, por favor escolher novamente a operação desejada")
        