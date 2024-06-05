# Sistema Bancário Versão 2

Este projeto implementa um sistema bancário simples utilizando a linguagem Python. O sistema permite a criação de usuários, a criação de contas correntes vinculadas a esses usuários e a realização de operações bancárias básicas como depósito, saque e visualização de extrato.

É uma adaptação do código disponibilizado pela empresa educadora DIO, do curso "Formação Python Developer ", do desafio " Otimizando o Sistema Bancário com Funções Python "

## Funcionalidades

- **Depositar**: Permite depositar um valor em uma conta corrente identificada pelo CPF do usuário.
- **Sacar**: Permite sacar um valor de uma conta corrente identificada pelo CPF do usuário, respeitando limites de saldo, valor e número de saques diários.
- **Extrato**: Exibe o extrato de uma conta corrente identificada pelo CPF do usuário, mostrando o histórico de movimentações e o saldo atual.
- **Nova Conta**: Cria uma nova conta corrente para um usuário existente, identificado pelo CPF.
- **Listar Contas**: Lista todas as contas de um cliente específico, identificado pelo CPF.
- **Listar Usuários**: Lista todos os usuários cadastrados no sistema.
- **Novo Usuário**: Cria um novo usuário (cliente do banco) com informações como nome, CPF, data de nascimento e endereço.
- **Sair**: Sair

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

Sistema_Bancario/
│
├── codigo-fonte/
│ ├── sistema_bancario_v2.py
│
├── apoio/
│ └── README.md
│
├── doc/
│
├── tests/
│
└── README.md


## Como Executar

1. **Clone o repositório**:
   git clone https://github.com/IOVASCON/Sistema_Bancario_V2.git

2. Navegue até o diretório do projeto:
cd Sistema_Bancario_V2/codigo-fonte

3. Execute o script Python:
python sistema_bancario_v2.py

## Uso

1. Ao executar o script, o menu principal será exibido com as seguintes opções:

================ MENU ================
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[lu] Listar usuários
[nu] Novo usuário
[q]  Sair
=> 

2. Selecione uma das opções digitando a letra correspondente e pressionando Enter.

3. Siga as instruções exibidas para cada operação.

## Exemplo de Uso

Criação de Usuário

1. Selecione a opção [nu] para criar um novo usuário.
2. Informe os dados solicitados: CPF, nome, data de nascimento e endereço.

Criação de Conta

1. Selecione a opção [nc] para criar uma nova conta.
2. Informe o CPF do usuário para associar a conta ao usuário existente.

Depósito

1. Selecione a opção [d] para realizar um depósito.
2. Informe o CPF do usuário e o valor a ser depositado.

Saque

1. Selecione a opção [s] para realizar um saque.
2. Informe o CPF do usuário e o valor a ser sacado.

Exibir Extrato

1. Selecione a opção [e] para exibir o extrato.
2. Informe o CPF do usuário para visualizar o extrato da conta.

Listar Contas

1. Selecione a opção [lc] para listar as contas de um cliente.
2. Informe o CPF do cliente para listar suas contas.

Listar Usuários

1. Selecione a opção [lu] para listar todos os usuários cadastrados.

Sair

1. Selecione a opção [q] para sair do sistema.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a ......