"""
Curso em Vídeo: Soma com flag

Lê vários números inteiros até o usuário digitar 999,
então exibe quantos números foram digitados e a soma deles,
desconsiderando o valor de parada.
"""

numero = 0
soma = 0
quantidade = 0

while numero != 999:
    numero = int(input('Digite um número (999 para finalizar): '))

    if numero != 999:
        soma += numero
        quantidade += 1

print(f'A soma dos números é {soma}\n'
      f'A quantidade de números digitados é {quantidade}')
