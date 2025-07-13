"""
Exercício:

Calcula a média dos valores de uma lista de números.
"""

lista_numeros = []

while True:
    numero = int(input('Digite um número para soma ("0" para finalizar): '))

    if numero == 0:
        break

    lista_numeros.append(numero)

soma_lista = sum(lista_numeros)
media = soma_lista / len(lista_numeros)

print(f'Essa é a soma da lista: {soma_lista}')
print(f'Essa é a média da lista: {media}')
