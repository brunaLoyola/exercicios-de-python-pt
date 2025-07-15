"""
Curso em video: Pares e ímpares lista

Lê sete valores numéricos e armazena em lista única,
mantendo pares e ímpares separados em ordem crescente."""

lista = [[], []]

for pos in range(0, 7):
    valor = int(input(f'Digite o {pos+1}° valor: '))

    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
print(f"Lista de números pares: {lista[0]}")
lista[1].sort()
print(f"Lista de números ímpares: {lista[1]}")
