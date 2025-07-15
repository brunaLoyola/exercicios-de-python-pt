"""
Curso em video: Preenchendo uma Matriz 3X3

Declara uma matriz 3x3 preenchida pelo usuário
e exibe a matriz formatada na tela.
"""

matriz = []
temporaria = []
for i in range(3):
    for j in range(3):
        numero = int(input(f'Digite o valor [{i}, {j}]: '))
        temporaria.append(numero)
    matriz.append(temporaria[:])
    temporaria.clear()

for pos in range(3):
    print(matriz[pos])
