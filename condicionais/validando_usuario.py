"""
Exercício:

Verifica se um número está entre 10 e 20 e
valida se o usuário é 'admin' ou 'root'.
"""

numero = int(input('Digite um número: '))

if numero >= 10 and numero <= 20:
    print(f'O número {numero} está entre 10 e 20.')
else:
    print(f'O número {numero} não está entre 10 e 20.')

usuario = 'admin'

if usuario == 'admin':
    print('O usuário é um administrador')
else:
    print('O usuário não é um administrador.')

usuario_02 = 'root'

if usuario_02 == 'admin':
    print('O usuário é um administrador.')
else:
    print('O usuário não é um administrador.')
