"""
Curso em video: Categoria de natação

Lê o ano de nascimento de um atleta e mostra sua categoria conforme a idade
"""
from datetime import datetime

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade_atual = datetime.now().year - ano_nascimento

if idade_atual <= 9:
    print(f'A idade é {idade_atual} anos, sendo da categoria MIRIM')
elif idade_atual > 9 and idade_atual <= 14:
    print(f'A idade é {idade_atual} anos, sendo da categoria INFANTIL')
elif idade_atual > 14 and idade_atual <= 19:
    print(f'A idade é {idade_atual} anos, sendo da categoria JUNIOR')
elif idade_atual == 20:
    print(f'A idade é {idade_atual} anos, sendo da categoria SÊNIOR')
else:
    print(f'A idade é {idade_atual} anos, sendo da categoria MASTER')
