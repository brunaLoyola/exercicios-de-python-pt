"""
Exercício: Cálculo de notas para saque

Lê um valor inteiro e determina quantas notas de 100, 50, 20, 10, 5 e 1
são necessárias para o saque.
"""

valor = int(input('Digite o valor inteiro que será retirado: '))
notas = [100, 50, 20, 10, 5, 1]

print('Notas que serão entregues: ')

for nota in notas:
    quantidade = valor // nota
    valor %= nota

    if quantidade > 0:
        print(f'{quantidade} nota(s) de R${nota}')
