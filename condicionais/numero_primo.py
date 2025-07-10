""""
Curso em video: Número primo

Verifica se um número informado é primo.
"""

numero = int(input('Digite um número válido: '))

if numero >= 2:
    confirma = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            confirma = False
            break
    if confirma:
        print('É primo.')
    else:
        print('Não é primo.')
else:
    print('Número inválido.')
