"""
Curso em Vídeo: 10 primeiros termos de uma PA

Lê o primeiro termo e a razão de uma progressão aritmética
e exibe os 10 primeiros termos.
"""

numero = int(input('Digite o primeiro termo de uma progressão aritmética: '))
razao = int(input('Informe a razão: '))

decimo = numero + (10 - 1) * razao
for c in range(numero, decimo + razao, razao):
    print(c)
