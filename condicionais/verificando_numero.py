"""
Exercício:

Verifica se um número é positivo, negativo ou igual a zero.
"""

numero = int(input('Digite um numero: '))

if numero == 0:
    print('Seu número é 0.')
elif numero < 0:
    print('Seu número é negativo.')
else:
    print('Seu número é positivo.')
