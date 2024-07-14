# Sistema Bancário Simulado em Python

## Descrição Geral

Este projeto simula um sistema bancário básico, permitindo a criação de contas para clientes, realização de transações como depósitos e saques, e manutenção de um histórico de transações. Foi desenvolvido como uma ferramenta educacional para demonstrar conceitos de Programação Orientada a Objetos (POO), como classes, herança, métodos abstratos e interfaces. Este projeto foi uma oportunidade valiosa para praticar e aprofundar meus conhecimentos em POO.

## Motivação e Objetivos

### Treinamento em POO

A principal motivação para desenvolver este sistema bancário foi treinar em Programação Orientada a Objetos. A POO é uma abordagem de programação que utiliza "objetos" – instâncias de classes – para diseñar aplicativos e programas de software. Ao trabalhar neste projeto, tive a chance de:

- Entender melhor os conceitos fundamentais de POO, como encapsulamento, herança e polimorfismo.
- Praticar a criação de classes e objetos, bem como a implementação de métodos e propriedades.
- Desenvolver habilidades em design de classes e relações entre elas, como associação e composição.
- Implementar padrões de projeto e princípios SOLID, embora de forma simplificada, para melhorar a qualidade do código.

### Aprendizagem Prática

Além de treinar em POO, este projeto também serviu como uma excelente oportunidade para aprender sobre:

- Manipulação de dados e estruturas de dados.
- Tratamento de erros e exceções.
- Desenvolvimento de interfaces de usuário interativas.
- Teste e depuração de código.

## Classes Principais

### Cliente
Representa um cliente genérico no banco, com um endereço e uma lista de contas associadas.

### PessoaFisica
Herda de `Cliente`, adicionando atributos específicos para pessoas físicas, como CPF, nome e data de nascimento.

### Conta
Base para contas bancárias, armazenando saldo, número da conta, agência, cliente titular e histórico de transações.

### ContaCorrente
Herda de `Conta`, adicionando limites específicos para contas correntes.

### Historico
Gerencia o histórico de transações de uma conta.

### Transacao, Saque, Deposito
`Transacao` é uma classe abstrata para transações, enquanto `Saque` e `Deposito` representam tipos específicos de transações.

## Funcionalidades Principais

### Menu Interativo
Permite ao usuário escolher entre várias operações, como realizar um saque, depósito, visualizar o extrato ou criar novos clientes e contas.

### Transações
Inclui suporte para saques e depósitos, com validações de saldo e limites específicos para contas correntes.

### Histórico de Transações
Cada transação é registrada em um histórico, permitindo o acompanhamento das atividades financeiras de um cliente.

## Execução Principal

O programa inicializa listas para clientes e contas, e entra em um loop que interage com o usuário através de um menu, chamando funções apropriadas para executar as operações escolhidas.
