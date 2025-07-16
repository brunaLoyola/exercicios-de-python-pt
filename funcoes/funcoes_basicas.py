"""
Exercício:

Funções básicas com parâmetros e retorno.
Inclui saudação personalizada e impressão de itens de uma lista.
"""

lista_global = ['Abacaxi', 'Banana', 'Uva', 'Rocambole']


def imprime_frase(nome, idade):
    return print(f'Olá {nome}, você não parece ter {idade}')


def exibir_lista(lista):
    for item in lista:
        print(item)


nome_usuario = input('Digite seu nome: ')
idade_usuario = int(input('Digite sua idade: '))

imprime_frase(nome_usuario, idade_usuario)
exibir_lista(lista_global)
