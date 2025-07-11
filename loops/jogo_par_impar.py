"""
Curso em Vídeo: Par ou ímpar

Joga par ou ímpar com o computador até o jogador perder,
exibindo no final o total de vitórias consecutivas.
"""

from random import randint
from time import sleep

vitorias = 0
while True:
    computador = randint(0, 10)
    opcao = input('Você quer impar ou par ? ').upper()
    jogador = int(input('Dígite um número: '))
    print('ímpar ou par ...')
    sleep(1)

    print(f' Computador: {computador} \n Jogador: {jogador} ')
    resultado = computador + jogador
    if opcao == 'PAR':
        if resultado % 2 == 0:
            print('Parábens você venceu!!')
            vitorias += 1
        else:
            print(f'Que pena você perdeu !! Você venceu {vitorias} vezes')
            break
    elif opcao == 'IMPAR':
        if resultado % 2 != 0:
            print('Parábens você venceu!!')
            vitorias += 1
        else:
            print(f'Que pena você perdeu !! Você venceu {vitorias} vezes')
            break
    else:
        print('Opção inválida.')
