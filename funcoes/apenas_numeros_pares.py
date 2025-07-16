"""
Exercício:

Função que recebe uma lista de números e retorna apenas os pares.
Inclui função auxiliar para coletar números do usuário até 'sair'.
"""


def numeros_pares(lista_numeros):
    lista_pares = []

    for i in lista_numeros:
        if i % 2 == 0:
            lista_pares.append(i)

    return lista_pares


def pedindo_numero():
    lista_usuario = []

    while True:
        numero = input('Digite um número: (ou digite "sair") ')

        if numero == 'sair':
            break
        else:
            lista_usuario.append(int(numero))
    return lista_usuario


lista_usuario = pedindo_numero()
lista_pares = numeros_pares(lista_usuario)

print('Lista de números pares: ', lista_pares)
