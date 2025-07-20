"""
Exercício:

Função que recebe um número como parâmetro e
verifica se ele é par ou ímpar, retornando o resultado.
"""


def par_impar(numero):
    if numero < 0:
        return print('O número é negativo')
    elif numero % 2 == 0:
        return print('O número é par')
    else:
        return print('O número é ímpar')


numero_usuario = int(input('Digite um número: '))
par_impar(numero_usuario)
