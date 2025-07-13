"""
Exercicio:

Simula um programa de compras que armazena produtos com preços,
exibe a lista cadastrada, calcula o total e mostra o mais caro.
"""

produtos = int(input('Quantos produtos você deseja comprar: '))
lista_informacao = []

for produto in range(1, produtos+1):
    nome = input(f'Digite o nome do {produto}° produto: ')
    valor = float(input(f'Digite o valor do {produto}° produto: '))
    lista_informacao.append([nome, valor])

print(lista_informacao)
