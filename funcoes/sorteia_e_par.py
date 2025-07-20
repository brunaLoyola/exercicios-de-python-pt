"""
Curso em video: Sorteia e soma valores pares

Programa com lista números e duas funções:
sorteia() para gerar 5 valores aleatórios
e somaPar() para somar os valores pares da lista.
"""

from time import sleep
from random import randint


def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {numeros}, temos {soma}')


def sorteia():
    lista = []
    print('Sorteando os 5 valores da lista: ', end='')
    for i in range(5):
        numero = randint(1, 10)
        lista.append(numero)
        print(f'{numero} ', end='', flush=True)
        sleep(0.5)
    print('Pronto!')
    somaPar(lista)


sorteia()
