"""
Curso em Vídeo: Média, maior e menor

Lê vários números inteiros e ao final mostra:
- A média entre todos os valores
- O maior e o menor valor lido

O programa pergunta ao usuário se ele deseja continuar digitando valores.
"""

soma = 0
quantidade = 0
maior = 0
menor = 0
while True:
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    continuar = input('Deseja continuar ? [S] / [N]: ').upper()

    if continuar == 'N':
        break

print(f'A média dos valores é {soma/quantidade}')
print(f'O maior número é {maior} e o menor número é {menor}')
