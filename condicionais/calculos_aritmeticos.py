"""
Exercício:

Realiza cálculos com base na operação escolhida pelo usuário.
"""

numero_01 = int(input('Digite o primeiro número: '))
numero_02 = int(input('Digite o segundo número: '))

operacao = input('Digite a operação (+, -, *, /): ')

if operacao in '+':
    print(f'Resultado: {numero_01 + numero_02}')
elif operacao in '-':
    print(f'Resultado: {numero_01 - numero_02}')
elif operacao in '*':
    print(f'Resultado: {numero_01 * numero_02}')
elif operacao in '/':
    print(f'Resultado: {numero_01 / numero_02}')
else:
    print('Operação inválida!')
