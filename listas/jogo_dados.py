"""
Curso em video: Jogando os dados

Simula 4 jogadores jogando dado, armazena resultados em
dicionário e exibe ranking por ordem de resultado.
"""

from random import randint
from time import sleep
from operator import itemgetter

ranking = []
jogo = {
    'Jogador01': randint(1, 6),
    'Jogador02': randint(1, 6),
    'Jogador03': randint(1, 6),
    'Jogador04': randint(1, 6)
}

print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
