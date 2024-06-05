"""
Sistema Bancário com Funcionalidades Adicionadas

Este programa implementa um sistema bancário modularizado com as operações
de depósito, saque, extrato, criação de usuário, criação de conta corrente
e listagem de contas.

Autor: Izairton Oliveira de Vasconcelos, adaptado do curso da DIO "Formação Python Developer" do desafio ' Otimizando o Sistema Bancário com Funções Python'
Data: 05/06/2024
"""

import textwrap  # Importa a biblioteca textwrap para facilitar a formatação de texto

def menu():
    """
    Exibe o menu de opções do sistema bancário.
    """
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [lu]\tListar usuários
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))  # Exibe o menu e retorna a opção escolhida pelo usuário

def depositar(usuarios, contas, /):
    """
    Realiza o depósito na conta do usuário identificado pelo CPF.
    """
    cpf = input("Informe o CPF do usuário: ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário existe

    if not usuario:  # Se o usuário não for encontrado
        print("\n@@@ Usuário não encontrado! @@@")
        return

    conta = filtrar_conta(cpf, contas)  # Verifica se a conta do usuário existe
    if not conta:  # Se a conta não for encontrada
        print("\n@@@ Conta não encontrada para este usuário! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito
    if valor > 0:  # Se o valor for positivo
        conta['saldo'] += valor  # Adiciona o valor ao saldo da conta
        conta['extrato'] += f"Depósito:\tR$ {valor:.2f}\n"  # Registra o depósito no extrato
        print("\n=== Depósito realizado com sucesso! ===")
    else:  # Se o valor for negativo ou zero
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

def sacar(usuarios, contas, /):
    """
    Realiza o saque da conta do usuário identificado pelo CPF.
    """
    cpf = input("Informe o CPF do usuário: ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário existe

    if not usuario:  # Se o usuário não for encontrado
        print("\n@@@ Usuário não encontrado! @@@")
        return

    conta = filtrar_conta(cpf, contas)  # Verifica se a conta do usuário existe
    if not conta:  # Se a conta não for encontrada
        print("\n@@@ Conta não encontrada para este usuário! @@@")
        return

    valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque
    excedeu_saldo = valor > conta['saldo']  # Verifica se o valor do saque excede o saldo
    excedeu_limite = valor > conta['limite']  # Verifica se o valor do saque excede o limite
    excedeu_saques = conta['numero_saques'] >= conta['limite_saques']  # Verifica se o número de saques excedeu o limite

    if excedeu_saldo:  # Se o valor do saque exceder o saldo
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:  # Se o valor do saque exceder o limite
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:  # Se o número de saques exceder o limite
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:  # Se o valor for positivo
        conta['saldo'] -= valor  # Subtrai o valor do saldo da conta
        conta['extrato'] += f"Saque:\t\tR$ {valor:.2f}\n"  # Registra o saque no extrato
        conta['numero_saques'] += 1  # Incrementa o número de saques
        print("\n=== Saque realizado com sucesso! ===")
    else:  # Se o valor for negativo ou zero
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

def exibir_extrato(usuarios, contas, /):
    """
    Exibe o extrato da conta do usuário identificado pelo CPF.
    """
    cpf = input("Informe o CPF do usuário: ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário existe

    if not usuario:  # Se o usuário não for encontrado
        print("\n@@@ Usuário não encontrado! @@@")
        return

    conta = filtrar_conta(cpf, contas)  # Verifica se a conta do usuário existe
    if not conta:  # Se a conta não for encontrada
        print("\n@@@ Conta não encontrada para este usuário! @@@")
        return

    print("\n================ EXTRATO ================")
    print(f"Titular: {usuario['nome']}")  # Exibe o nome do titular da conta
    print(f"CPF: {usuario['cpf']}")  # Exibe o CPF do titular da conta
    print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])  # Exibe o extrato ou uma mensagem caso não haja movimentações
    print(f"\nSaldo:\t\tR$ {conta['saldo']:.2f}")  # Exibe o saldo da conta
    print("==========================================")

def criar_usuario(usuarios):
    """
    Cria um novo usuário (cliente do banco).
    """
    cpf = input("Informe o CPF (somente número): ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário já existe

    if usuario:  # Se o usuário já existir
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")  # Solicita o nome completo do usuário
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")  # Solicita a data de nascimento do usuário
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")  # Solicita o endereço do usuário

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})  # Adiciona o usuário à lista de usuários
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    """
    Filtra um usuário pelo CPF.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]  # Filtra a lista de usuários pelo CPF
    return usuarios_filtrados[0] if usuarios_filtrados else None  # Retorna o usuário encontrado ou None

def criar_conta(agencia, numero_conta, usuarios, contas):
    """
    Cria uma nova conta corrente vinculada a um usuário.
    """
    cpf = input("Informe o CPF do usuário: ")  # Solicita o CPF do usuário
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário existe

    if usuario:  # Se o usuário for encontrado
        contas.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "limite": 500,
            "extrato": "",
            "numero_saques": 0,
            "limite_saques": 3
        })  # Adiciona a nova conta à lista de contas
        print("\n=== Conta criada com sucesso! ===")
    else:  # Se o usuário não for encontrado
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas_por_cliente(contas, usuarios):
    """
    Lista todas as contas de um cliente específico, identificado pelo CPF.
    """
    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário existe

    if not usuario:  # Se o usuário não for encontrado
        print("\n@@@ Usuário não encontrado! @@@")
        return

    contas_cliente = [conta for conta in contas if conta["usuario"]["cpf"] == cpf]  # Filtra a lista de contas pelo CPF do cliente

    if not contas_cliente:  # Se não houver contas para o cliente
        print("\n@@@ Nenhuma conta encontrada para este usuário. @@@")
        return

    for conta in contas_cliente:  # Para cada conta do cliente
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))  # Exibe as informações da conta

def listar_usuarios(usuarios):
    """
    Lista todos os usuários cadastrados.
    """
    if not usuarios:  # Se não houver usuários cadastrados
        print("\n@@@ Nenhum usuário cadastrado! @@@")
        return

    for usuario in usuarios:  # Para cada usuário cadastrado
        linha = f"""\
            Nome:\t\t{usuario['nome']}
            CPF:\t\t{usuario['cpf']}
            Data Nasc.:\t{usuario['data_nascimento']}
            Endereço:\t{usuario['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))  # Exibe as informações do usuário

def filtrar_conta(cpf, contas):
    """
    Filtra uma conta pelo CPF do usuário.
    """
    contas_filtradas = [conta for conta in contas if conta["usuario"]["cpf"] == cpf]  # Filtra a lista de contas pelo CPF do usuário
    return contas_filtradas[0] if contas_filtradas else None  # Retorna a conta encontrada ou None

def main():
    """
    Função principal que gerencia a execução do sistema bancário.
    """
    AGENCIA = "0001"  # Número da agência
    usuarios = []  # Lista de usuários
    contas = []  # Lista de contas

    while True:
        opcao = menu()  # Exibe o menu e obtém a opção do usuário

        if opcao == "d":
            depositar(usuarios, contas)  # Chama a função de depósito

        elif opcao == "s":
            sacar(usuarios, contas)  # Chama a função de saque

        elif opcao == "e":
            exibir_extrato(usuarios, contas)  # Chama a função de exibição de extrato

        elif opcao == "nu":
            criar_usuario(usuarios)  # Chama a função de criação de usuário

        elif opcao == "nc":
            numero_conta = len(contas) + 1  # Determina o número da nova conta
            criar_conta(AGENCIA, numero_conta, usuarios, contas)  # Chama a função de criação de conta

        elif opcao == "lc":
            listar_contas_por_cliente(contas, usuarios)  # Chama a função de listagem de contas por cliente

        elif opcao == "lu":
            listar_usuarios(usuarios)  # Chama a função de listagem de usuários

        elif opcao == "q":
            break  # Encerra o loop e finaliza o programa

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")  # Exibe mensagem de erro para opção inválida

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
