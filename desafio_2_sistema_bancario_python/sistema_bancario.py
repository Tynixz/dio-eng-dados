menu = """

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500 #limite do valor que pode ser sacado.
extrato = "" #variável para guardar cada ação concluída pelo cliente
numero_saques = 0 # variável para contar quantas vezes o cliente sacou.
LIMITE_SAQUES = 3 

while True:

    opcao = input(menu) #criar uma variável para mexer nos ifs.

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo :
            print ("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Saques excedidos.")

        elif valor > 0:
            saldo -= valor # saldo - valor = saldo
            extrato += f"Saque: R$ {valor:.2f}\n" # Adiciona o escrito "saque: R$ __"
            numero_saques += 1 # Como acontecerá o saque, soma +1 na contagem dos saques.
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizados movimentações." if not extrato else extrato) # IF Ternário 
#faz com que o código fique mais simples. Operador ternário substitui blocos IF/ELSE por expressao em uma linha.
#Esse If ternário usado significa: Verifico se o extrato está vazio (if not extrato - Como extrato é tipo String,
#ou seja, começa vazio.). Se não estiver vazio (else) exibe os dados dele.
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print ("Operação inválida, por favor selecione novamente a operação desejada.")
