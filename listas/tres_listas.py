"""
Curso em video: Separando em três listas

Lê vários números em uma lista e separa os valores em listas
de pares e ímpares, exibindo o conteúdo das três listas.
"""

valores_totais = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    continuar = input('Deseja continuar [S/N]: ').upper()

    if continuar in 'N':
        valores_totais.append(valor)
        break
    else:
        valores_totais.append(valor)

for item in valores_totais:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(valores_totais)
print(pares)
print(impares)
