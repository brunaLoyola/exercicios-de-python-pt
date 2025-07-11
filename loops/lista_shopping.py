"""
Exercício:

Cria um programa para gerenciar uma lista de compras, permitindo ao usuário
adicionar itens continuamente até digitar 'sair'.
Ao final, exibe todos os itens cadastrados e o total de elementos na lista.
"""


lista_compras = []

while True:
    item = input('Digite o item para adicionar a lista (ou "sair"): ')

    if item == 'sair':
        break
    else:
        lista_compras.append(item)

print(lista_compras)
