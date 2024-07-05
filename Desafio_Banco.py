

def menu():
    titulo = "Menu" 
    titulo_centralizado= titulo.center(30,"=")
    menu = f"""{titulo_centralizado}
    
    [d] - Deposito
    [s] - Sacar
    [e] - Extrato
    [nu] - Novo usuario
    [nc] - Nova contas
    [lc] - Listar contas
    [q] - Sair
    
{30*"="}
Digite a opção desejada..: """
    return (input(menu))

def depositar(saldo,valor_deposito,extrato):
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f"Deposito REALIZADO!\nO saldo atual da conta é..: {saldo:.2f}R$\n")
        extrato.append(f"Deposito {valor_deposito:.2f}R$")
    else:
        print(f"O valor do deposito deve ser maior que 0")
    return saldo

def sacar(*, saldo, contador_saque_diario, limite_de_saques, extrato):
    if (contador_saque_diario == limite_de_saques):
        print("Limite de saque diario excedido")
    else:
        saque = float(input("Digite o valor que deseja sacar..: "))
        if (saque > saldo):
            print(f"\nSaldo insuficiente!!")
        elif (saque > 500):
            print("\nO limite por saque é de 500.00R$")
        else:
            saldo -= saque
            contador_saque_diario += 1
            extrato.append(f"Saque {saque:.2f}R$")
            print(f"\nSaque REALIZADO!\nSeu saldo atual é {saldo}R$")
    return saldo, contador_saque_diario

def mostrar_extrato(extrato, saldo):
    if extrato == []:
        print("\nNão houve movimentação recente na sua conta")
    else:
        for indice,tranzacao in enumerate(extrato):
            print(f"{indice + 1} - {tranzacao}\n")
    print(f"{30*"="}")
    print(f"Seu saldo atual é {saldo:.2f}R$")

def filtrar_usuario(cpf,usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] ==  cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (comente numeros)..: ")
    usario = filtrar_usuario(cpf,usuarios)

    if usario:
        print(f"já existe um usuário com esse CPF!!")
        return
    
    nome = input("Informe seu nome completo..: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa)..: ")
    endereco = input("Informe o endereço (logradoro, nro - bairro - cidade/sigla estado)")

    usuarios.append({"nome" : nome, "data_nascimento" : data_nascimento, "endereco" : endereco})

    print("Usuário criado com sucesso!!")

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário..: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criado com sucesso!!")
        contas.append({"agencia" : agencia, "numero_conta" : numero_conta, "usuario" : usuario})

    print("!!! Usuário não encontrado, fluxo de criação de conta encerrado !!!")

def listar_contas(contas):
    if contas == []:
        print("!! Não há nenhuma conta criada !!")
    for conta in contas:
        linha = f"""
                Agência : {conta['agencia']}
                C/C:      {conta['numero_conta']}
                Titular:  {conta['usuario']['nome']}
            """
        print(100*"=")
        print(linha)

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    contador_saque_diario = 0
    extrato = []
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor_deposito = float(input("Digite a quantidade que deseja depositar..: "))
            saldo = depositar(saldo,valor_deposito,extrato)

        elif (opcao == "s") or (opcao == "S"):
            print(f"Saldo atual {saldo:.2f}R$\n")
            saldo, contador_saque_diario = sacar(
                saldo = saldo,
                contador_saque_diario = contador_saque_diario,
                limite_de_saques = LIMITE_DE_SAQUES,
                extrato = extrato,
            )

        elif (opcao == "e") or (opcao == "E"):
            mostrar_extrato(extrato,saldo)

        elif (opcao == "nu"):
            criar_usuario(usuarios)

        elif (opcao == "nc"):
            numero_conta = len(contas + 1)
            criar_conta(AGENCIA,numero_conta, usuarios, contas)

        elif (opcao == "lc"):
            listar_contas(contas)

        elif (opcao == "q") or (opcao == "Q"):
            print("Obrigado por utilizar nosso sistema!")
            break

        else:
            print("Opção invalida\n")

main()