"""
Curso em Vídeo: Ordenando de forma crescente

Permite ao usuário digitar números únicos em uma lista e
exibe os valores em ordem crescente.
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
