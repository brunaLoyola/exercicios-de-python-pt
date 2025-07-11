"""
Curso em Vídeo: Tabuada de vários números

Mostra a tabuada de vários números digitados pelo usuário.
O programa será interrompido quando for digitado um número negativo.
"""

numero = 0

while True:
    numero = int(input('Digite um número:'))
    if numero < 0:
        break

    for c in range(1, 11):
        print(f'{numero} X {c} = {c * numero}')
