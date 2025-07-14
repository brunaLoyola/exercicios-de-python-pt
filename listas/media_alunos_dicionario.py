"""Curso em video: Média aluno

Lê nome e média de um aluno e exibe situação
em um dicionário formatado.
"""

pessoa = {}

pessoa['Nome'] = input('Nome: ')
pessoa['Média'] = float(input(f'Digite a média de {pessoa["Nome"]}: '))

if pessoa['Média'] >= 7:
    pessoa['Situação'] = 'Aprovado'
elif 5 <= pessoa['Média'] < 7:
    pessoa['Situação'] = 'Recuperação'
else:
    pessoa['Situação'] = 'Reprovado'

for k, v in pessoa.items():
    print(f'{k} é igual a {v}')
