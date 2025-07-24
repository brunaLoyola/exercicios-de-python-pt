"""
Curso em video: Interactive Helping System

Crie um sistema interativo que mostre a ajuda dos comandos em Python
usando a função help().
O programa deve continuar até o usuário digitar 'FIM'.
"""


def ajuda(com):
    help(com)


comando = ''

while True:
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
