"""
Curso em video: Fatorial

Função fatorial() que recebe um número e parâmetro opcional show
para exibir ou não o processo de cálculo.
"""

from math import factorial


def fatorial(num, show=0):
    fat = factorial(num)
    if show == 1:
        contador = num
        while contador > 0:
            print(f'{contador} ', end='')
            print(' X ' if contador > 1 else '=', end=' ')
            contador -= 1
    return f'{fat}'


numero_usuario = int(input('Digite um número: '))
mostrar = int(input('Deseja mostrar o fatorial ?: (1-Sim / 0-Não)'))
print(fatorial(numero_usuario, mostrar))
