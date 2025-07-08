"""
Curso em Vídeo

O usuário irá digitar vários valores numéricos, adicionando-os em uma lista.
Caso o número já exista nela, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

valores.sort()
print(f'Esta é sua lista ordenada: {valores}')
