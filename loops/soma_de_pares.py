"""
Exercício:

Lê um número inteiro e exibe os 10 primeiros números pares maiores que ele.
"""

numero_usuario = int(input('Digite um número inteiro: '))
numeros_gerados = []

if numero_usuario % 2 != 0:
    numero_usuario += 3
else:
    numero_usuario += 2

for n in range(numero_usuario, numero_usuario+20, +2):
    print(n)
