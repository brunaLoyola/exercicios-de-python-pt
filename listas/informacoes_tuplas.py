"""
Curso em video: Informações de números em tupla

Lê quatro números, armazena em uma tupla e exibe:
- Quantas vezes o 9 apareceu;
- A posição do primeiro 3;
- Os números pares digitados.
"""

numero01 = int(input('Digite o primeiro número: '))
numero02 = int(input('Digite o segundo número: '))
numero03 = int(input('Digite o terceiro número: '))
numero04 = int(input('Digite o quarto número: '))
tupla = (numero01, numero02, numero03, numero04)

aparece = 0
pares = 0

for t in tupla:
    if t == 9:
        aparece += 1
    if t % 2 == 0:
        pares += 1

print(f'O número 9 aparece {aparece} vezes, existem {pares} números pares')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3)+1}° posição')
