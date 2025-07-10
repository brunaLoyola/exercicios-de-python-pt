"""
Exercício:

Analise uma frase e mostre quantas vezes a letra "a" aparece e suas posições.
"""

frase = input('Digite uma frase: ').lower().replace(' ', '')

quantidade = frase.count('a')

primeira_posicao = frase.find('a')

ultima_posicao = frase.rfind('a')

print(
    f'Essa é a quantidade de letras "A": {quantidade}\n'
    f'A primeira posição que o "A" aparece é a {primeira_posicao+1}°\n'
    f'A ultima posição é a {ultima_posicao+1}°.'
)
