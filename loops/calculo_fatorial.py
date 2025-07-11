"""
Curso em Vídeo: Cálculo fatorial

Lê um número inteiro e exibe seu fatorial
mostrando o cálculo completo no formato tradicional.
"""

from math import factorial
numero = int(input('Digite um número, para mostrar o fatorial: '))
contador = numero

while contador > 0:
    print(f'{contador} ', end='')
    print(' X ' if contador > 1 else '=', end=' ')
    contador -= 1

print(factorial(numero))
