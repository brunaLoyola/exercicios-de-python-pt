"""
Curso em video: Valor da passagem

Calcula o preço de uma passagem com base na distância da viagem em km.
"""

distancia = int(input('Digite a distância da viagem km: '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'A distância é {distancia}km, o valor da passagem é R${valor:.2f}.')
else:
    valor = distancia * 0.45
    print(f'A distância é {distancia}km, o valor da passagem é R${valor:.2f}.')
