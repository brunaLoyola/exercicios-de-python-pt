"""
Curso em Vídeo: Adivinhação com laço

O computador gera um número aleatório entre 0 e 10
e continua pedindo palpites do usuário até ele acertar.
"""

from random import randint
from time import sleep

numero = randint(0, 10)
numero_usuario = 11
palpites = 0
while numero != numero_usuario:
    numero_usuario = int(input('Adivinhe um número entre 0 e 10: '))

    if numero == numero_usuario:
        palpites += 1
        print(f'O número {numero} é o correto. Parabéns!!')
        print(f'Você fez {palpites} palpites para acertar')
    else:
        print('O número está incorreto. Tente na próxima!!')
        sleep(1)
        palpites += 1
