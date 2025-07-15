"""
Curso em video: Matriz 3X3 com análise de informações

Trabalha com matriz 3x3, somando valores pares,
valores da terceira coluna e exibindo o maior
valor da segunda linha.
"""

matriz = []
temporaria = []
soma_par = 0
terceira_coluna = 0
for i in range(0, 3):
    for j in range(0, 3):
        numero = int(input(f'Digite o valor [{i}, {j}]'))
        temporaria.append(numero)
    matriz.append(temporaria[:])
    temporaria.clear()

for i in range(0, 3):
    print(matriz[i])

    terceira_coluna += matriz[i][2]

    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]

maior_segunda_linha = max(matriz[1])
print(f'A soma dos pares da matriz é {soma_par}')
print(f'A soma dos valores da terceira coluna {terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')
