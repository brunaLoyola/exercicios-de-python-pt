"""
Curso em Vídeo: Soma de números pares

Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Valores ímpares devem ser desconsiderados.
"""


soma = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}° número: '))

    if numero % 2 == 0:
        soma += numero

print(f'A soma dos números pares deu {soma}')
