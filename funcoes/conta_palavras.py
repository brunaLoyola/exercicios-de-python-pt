"""
Exercício:

Função que conta o número de palavras em uma frase recebida
como parâmetro e retorna a quantidade.
"""


def conta_palavras(frase):
    lista_palavras = frase.split()
    return len(lista_palavras)


frase_usuario = input('Digite uma frase: ')
print(conta_palavras(frase_usuario))
