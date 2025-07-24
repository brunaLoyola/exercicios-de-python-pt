"""
Curso em vide: Leia números inteiros

Função leiaInt() que simula input() com validação,
aceitando apenas valores numéricos inteiros.
"""


def leiaInt(msg):
    ok = False
    valor = 0

    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número válido')
        if ok:
            break
    return valor


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
