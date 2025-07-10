"""
Curso em video: Alistamento Militar

Lê o ano de nascimento e
informa a situação do alistamento militar com base na idade.
"""

from datetime import datetime

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade_atual = datetime.now().year - ano_nascimento

if idade_atual <= 17:
    print(f'Você tem {idade_atual} anos, a idade para alistamento é 18 anos')
    print(f'Faltam {18 - idade_atual} ano(s)')
elif idade_atual == 18:
    print('Parabéns você já tem 18 anos. Está na hora de se alistar')
else:
    print(
        f'Sua idade é de {idade_atual} anos,'
        f'O prazo para alistamento está atrasado em {idade_atual - 18} anos'
    )
