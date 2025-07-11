"""
Curso em Vídeo: Menu de operações

Lê dois valores e apresenta um menu para o usuário escolher:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Realiza a operação escolhida em cada caso.
"""

opcao = 0

valor_01 = int(input('Digite o primeiro valor: '))
valor_02 = int(input('Digite o segundo valor: '))

while opcao != 5:
    print("""
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos numeros
        [5] Sair
    """)
    opcao = int(input())

    if opcao == 1:
        print(f'A soma dos números é {valor_01+valor_02}')
    elif opcao == 2:
        print(f'{valor_01} X {valor_02} = {valor_01*valor_02}')
    elif opcao == 3:
        if valor_01 > valor_02:
            print(f'O maior valor entre {valor_01} e {valor_02} = {valor_01}')
        elif valor_02 > valor_01:
            print(f'O maior valor entre {valor_01} e {valor_02} = {valor_02}')
        else:
            print('Ambos são números iguais')
    elif opcao == 4:
        valor_01 = int(input('Digite o primeiro valor: '))
        valor_02 = int(input('Digite o segundo valor: '))
