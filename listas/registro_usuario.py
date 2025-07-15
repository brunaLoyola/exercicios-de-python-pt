"""
Exercício:

Cadastra informações de três usuários e determina quem é
maior de idade.
"""

informacoes_usuario = []

for quantidade in range(3):
    print(f'Usuário {quantidade+1}')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    informacoes_usuario.append([nome, idade])

for pessoa in informacoes_usuario:
    print(f'Nome:{pessoa[0]}')
    print(f'Idade:{pessoa[1]}')

for pessoa in informacoes_usuario:
    if int(pessoa[1]) >= 18:
        print(f'{pessoa[0]} é maior de idade')
    else:
        print(f'{pessoa[0]} é menor de idade')
