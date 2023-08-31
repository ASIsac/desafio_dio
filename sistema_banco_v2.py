import textwrap

def menu():
    menu = '''
\t========== MENU ==========
\t---> [1] DEPÓSITO  <------
\t---> [2] SAQUE     <------
\t---> [3] EXTRATO   <------
\t---> [4] NOVA CONTA    <--
\t---> [5] LISTAR CONTAS <--
\t---> [6] NOVO USUÁRIO  <--
\t---> [0] SAIR       <-----
\t==========================
    --> '''
    
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, quantidade_deposito, /):
    
    if valor > 0:
        saldo += valor
        quantidade_deposito += 1
        extrato += f'Deposito {quantidade_deposito}: R$ {valor:.2f}\n'
        print(f'\nSaldo: ---> R$ {saldo:.2f} <---\n')
    else:
        print('Valor inválido !')

    return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, limite_de_saque, quantidade_saques_diarios):
    
    if valor_saque > saldo:
        print('\nErro na operação de saque')
    
    elif valor_saque > limite_de_saque:
        print('\nErro na operação de saque. Valor excede o limite')
    
    elif quantidade_saques_diarios  == 0:
        print('\nLimite de saques diários atingidos')
    
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque {quantidade_saques_diarios}: R$ {valor_saque:.2f}\n"
        quantidade_saques_diarios -= 1
    else:
        print('Erro na operação')

    return saldo, extrato


def mostar_extrato(saldo, /, *, extrato):
    print('============ EXTRATO ==============')

    if saldo > 0:
        print(extrato)
        print(f'\nSaldo Atual: R$ {saldo:.2f}')
        
    else:
        print('\nNão foram realizadas movimentações!')
    print('===================================\n')

    return saldo, extrato


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ---> Já existe usuário com esse CPF! <---")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, Nr - bairro - cidade/ sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t\t{conta['numero_conta']}
            Titular da Conta:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def saindo_do_sistema():
    print('\n= = = = = = = = = = = = = = = = = = = ')
    print('| Obrigado por usar o nosso sistema |')
    print('|           Até a próxima!          |')
    print('= = = = = = = = = = = = = = = = = = = \n')
    
    return


def main():

    SAQUE_DIARIO        = 3
    LIMITE_SAQUE        = 500
    AGENCIA             = '0001'

    extrato             = ''
    saldo               = 0
    quantidade_deposito = 1
    usuarios = []
    contas = []
    


    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input('\nValor a depositar: R$ '))
            saldo, extrato = depositar(saldo, valor, extrato, quantidade_deposito)
        
        elif opcao == '2':
            print(f'Saldo disponível: R$ {saldo:.2f}')
            valor_saque = float(input('Digite o valor que você deseja sacar: R$ '))
            saldo, extrato = sacar(
                saldo= saldo,
                valor_saque= valor_saque,
                extrato= extrato,
                limite_de_saque= LIMITE_SAQUE,
                quantidade_saques_diarios= SAQUE_DIARIO,
            )
            print(f'\nSaldo Atual: R$ {saldo:.2f}')
        
        elif opcao == '3':
            mostar_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)
        
        elif opcao == '0':
            saindo_do_sistema()
            break

        else:
            print('\n Operação inválida!')
            print ('Digite novamente a operação desejada.\n')

main()


