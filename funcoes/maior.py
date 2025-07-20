"""
Curso em video: Maior valor

Função maior() que recebe vários valores inteiros
e informa qual deles é o maior.
"""

from time import sleep


def maior(* valores):
    cont = maior = 0
    print('*=' * 20)
    print('Analisando os valores passados ...')
    sleep(2)
    for num in valores:
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(1, 5, 6, 8, 10)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
