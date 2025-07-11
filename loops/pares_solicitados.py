"""
Objetivo:
    Coletar números do usuário, filtrar os pares e exibir estatísticas.

Etapas:
    1. Solicitar 10 números e armazená-los em uma lista;
    2. Criar uma nova lista apenas com os números pares;
    3. Exibir a lista completa, os números pares e a soma dos pares.
"""

lista_numeros = []
lista_par = []

for numero in range(1, 11):
    num = int(input(f'Digite o {numero}° número: '))
    lista_numeros.append(num)

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_par.append(numero)

print(f'Lista completa: {lista_numeros} ')

print(f'Lista de números pares: {lista_par}')

print(f'Soma dos números par: {sum(lista_par)}')
