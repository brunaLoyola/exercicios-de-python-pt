"""
Curso em video

Gera cinco números aleatórios em uma tupla e exibe os valores,
indicando o maior e o menor entre eles.
"""

from random import randint

numeros = (
            randint(1, 10), randint(1, 10),
            randint(1, 10), randint(1, 10), randint(1, 10))

for numero in numeros:
    print(f'{numero} ', end='')

print(f'\nO maior número da tupla é {max(numeros)}\n'
      f'O menor número da tupla é {min(numeros)}')
