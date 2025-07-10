"""
Exercício:

Compara dois números informados e exibe informações sobre sua relação.
"""

numero_01 = int(input('Digite o primeiro número: '))
numero_02 = int(input('Digite o segundo número: '))

if numero_01 == numero_02:
    print("Os dois números são iguais !")
elif numero_01 > numero_02:
    print(f'O maior número é: {numero_01}.')
else:
    print(f'O maior número é: {numero_02}.')
