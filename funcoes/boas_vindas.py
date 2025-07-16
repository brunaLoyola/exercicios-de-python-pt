"""
Exercício:

Função que exibe uma saudação personalizada,
recebendo o nome como parâmetro.
"""


def boas_vindas(nome):
    print(f'Seja bem-vindo(a), {nome}')


nome_usuario = input('Digite seu nome: ')
boas_vindas(nome_usuario)
