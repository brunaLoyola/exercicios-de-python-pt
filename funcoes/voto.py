"""
Curso em video: Voto

Função voto() que recebe o ano de nascimento
e retorna se o voto é NEGADO, OPCIONAL ou OBRIGATÓRIO.
"""

from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: OPCIONAL.'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO.'


nascimento = int(input('Digite a data de nascimento: '))
print(voto(nascimento))
