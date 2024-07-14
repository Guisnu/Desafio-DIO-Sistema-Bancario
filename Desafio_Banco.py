saldo = 0

LIMITE_DE_SAQUES = 3
contador_saque_diario = 0

extrato = []

titulo = "Menu" 
titulo_centralizado= titulo.center(30,"=")

menu = f"""{titulo_centralizado}
    
    [d] - Deposito
    [s] - Sacar
    [e] - Extrato
    [q] - Sair
    
{30*"="}
Digite a opção desejada..:"""

while True:

    opcao = input(menu)
    contador_extrato = 0

    
    if opcao == "d":
        valor_deposito = float(input("Digite a quantidade que deseja depositar..: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Deposito REALIZADO!\nO saldo atual da conta é..: {saldo:.2f}R$\n")
            extrato.append(f"Deposito {valor_deposito:.2f}")
        else:
            print(f"O valor do deposito deve ser maior que 0")

    elif (opcao == "s") or (opcao == "S"):

        print(f"Saldo atual {saldo:.2f}R$\n")

        if (contador_saque_diario == LIMITE_DE_SAQUES):
            print("Limite de saque diario excedido")
        else:
            saque = float(input("Digite o valor que deseja sacar..: "))

            if (saldo < saque):
                print(f"\nSaldo insuficiente!!")

            elif (saque > 500):
                print("\nO limite por saque é de 500.00R$")
            else:
                saldo -= saque
                contador_saque_diario += 1
                extrato.append(f"Saque {saque:.2f}")
                print(f"\nSaque REALIZADO!\nSeu saldo atual é {saldo}R$")

    elif (opcao == "e") or (opcao == "E"):
        if extrato == []:
            print("\nNão houve movimentação recente na sua conta")
        else:
            for n in extrato:
                contador_extrato += 1
                print(f"{contador_extrato} - {n}\n")
        print(f"{30*"="}")
        print(f"Seu saldo atual é {saldo:.2f}")

    elif (opcao == "q") or (opcao == "Q"):
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção invalida\n")