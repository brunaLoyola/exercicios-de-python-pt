"""
Objetivo:
    Criar uma lista de compras permitindo adicionar itens até digitar 'sair'.

Etapas:
    1. Solicitar ao usuário que adicione itens à lista;
    2. Exibir a lista completa ao final e informar quantos itens ela contém.
"""

lista_compras = []

while True:
    item = input('Digite o item para adicionar a lista (ou "sair"): ')

    if item == 'sair':
        break
    else:
        lista_compras.append(item)

print(lista_compras)
