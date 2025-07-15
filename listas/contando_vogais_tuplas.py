"""
Curso em video

Mostra as vogais presentes em cada palavra de uma tupla.
"""

palavras = ('amor', 'felicidade', 'bondade', 'generosidade')

for palavra in palavras:
    print(f'\n Na palavra {palavra.upper()} temos:', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
