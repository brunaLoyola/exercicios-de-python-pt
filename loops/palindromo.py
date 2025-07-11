"""
Curso em Vídeo: Verificação de palíndromo

Lê uma frase qualquer e informa se ela é um palíndromo,
desconsiderando os espaços.
"""

frase = input('Digite uma frase: ').upper().replace(' ', '')
inverso = frase[::-1]

if frase == inverso:
    print('Parabéns você tem um palindromo')
else:
    print('Que pena não é um palindromo')
