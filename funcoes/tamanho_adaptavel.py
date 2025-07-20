"""
Curso em video: Moldura adaptável

Função escreva() que recebe um texto como parâmetro
e exibe a mensagem formatada com moldura adaptável.
"""


def escreva(texto):
    tamanho = len(texto)

    print('-' * tamanho)
    print(f'{texto}')
    print('-' * tamanho)


texto_usuario = input('Digite uma mensagem: ')
escreva(texto_usuario)
