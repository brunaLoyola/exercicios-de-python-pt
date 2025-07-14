"""
Curso em video: Aposentadoria

Lê nome, ano de nascimento e CTPS, armazena em dicionário,
incluindo idade e cálculo da aposentadoria.
"""

from datetime import datetime

pessoa = {}
ano_atual = datetime.now().year

pessoa['Nome'] = input('Nome: ')
pessoa['Idade'] = ano_atual - int(input('Ano de nascimento: '))
pessoa['Ctps'] = int(input('Carteira de trabalho (0 se não tem): '))

if pessoa['Ctps'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))

    aposenta = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - ano_atual)
    pessoa['Aposentadoria'] = aposenta

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
