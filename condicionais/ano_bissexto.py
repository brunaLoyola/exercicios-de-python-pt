"""
Curso em vídeo: Verificação de ano bissexto

Lê um ano informado e verifica se ele é bissexto.
"""


ano = int(input('Digite o ano a ser verificado: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')
