"""
Exercício:

- Imprime números de 1 a 10
- Imprime números pares de 0 a 20
- Calcula e exibe a soma de 1 a 100
"""

for x in range(1, 11):
    print(x)

for par in range(0, 21, 2):
    print(par)

resultado = 0
for num in range(0, 100+1):
    resultado += num
    print(resultado)
