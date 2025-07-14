"""
Curso em video: Mega Sena

Gera palpites aleatórios para jogos da Mega Sena
"""

import random

lista = []

jogos = int(input('Quantos jogos você irá querer fazer: '))

for pos in range(0, jogos):
    lista.append(random.sample(range(1, 61), 6))

for pos in range(0, jogos):
    print(f'O seu {pos+1}° jogo é: {lista[pos]} ')
