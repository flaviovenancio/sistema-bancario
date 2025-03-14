# Sistema Bancário Simples

Este é um programa em Python que simula um sistema bancário simples com as seguintes funcionalidades:

## Depósito

* Saque

* Exibição de Extrato

* Saída do sistema

## Como Usar

1. Execute o script Python.

2. Escolha uma das opções do menu:

    * [d] Depositar

    * [s] Sacar

    * [e] Extrato

    * [q] Sair

3. Siga as instruções apresentadas na tela.

## Regras do Sistema

* O saldo inicial é R$ 0,00.

* O limite máximo por saque é de R$ 500,00.

* O usuário pode realizar até 3 saques por dia.

* Depósitos devem ser valores positivos.

* O extrato exibe todas as transações realizadas e o saldo atual.

## Exemplo de Uso

```bash
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> d

Digite o valor do depósito:
=> 100

Depósito realizado com sucesso!

Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> e

========== Extrato ==========
Depósito realizado no valor de R$ 100.00

Seu saldo é de R$ 100.00
============================
```
## Requisitos

* Python 3.x instalado

## Como Executar

Salve o código em um arquivo banco.py e execute:
```bash
python banco.py
```


