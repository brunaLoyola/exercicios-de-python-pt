"""
Curso em video: Pedra, Papel, Tesoura

Simula um jogo de pedra, papel e tesoura entre o usuário e o computador.
"""

import random

lista = ['Pedra', 'Papel', 'Tesoura']
opcao = random.choice(lista)

print(' Digite a opção: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura')
opcao_usuario = int(input())

if opcao_usuario == 1:
    if opcao == 'Pedra':
        print('Empate !! Ambos fizeram Pedra.')
    elif opcao == 'Papel':
        print('Você perdeu !! O computador fez papel.')
    else:
        print('Você ganhou !! O computador escolheu tesoura.')
elif opcao_usuario == 2:
    if opcao == 'Papel':
        print('Empate !! Ambos fizeram Papel.')
    elif opcao == 'Tesoura':
        print('Você perdeu !! O computador fez tesoura.')
    else:
        print('Você ganhou !! O computador escolheu pedra.')
elif opcao_usuario == 3:
    if opcao == 'Tesoura':
        print('Empate !! Ambos fizeram Tesoura.')
    elif opcao == 'Pedra':
        print('Você perdeu !! O computador fez pedra.')
    else:
        print('Você ganhou !! O computador escolheu papel.')
else:
    print('Opção inválida.')
