"""
Exercicio:

Trabalha com listas, compreensões e realiza filtragem de pares e soma.
"""


numeros = [1, 2, 3, 4, 5]

quadrado = [num * num for num in numeros]
print(quadrado)

pares = [num for num in numeros if num % 2 == 0]
print(pares)

print(sum(pares))
