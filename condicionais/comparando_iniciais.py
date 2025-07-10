"""
Exercício

Compara as iniciais de dois nomes ignorando maiúsculas, minúsculas e espaços.
"""

primeiro_nome = input('Digite o primeiro nome: ').lower()
segundo_nome = input('Digite o segundo nome: ').lower()

if primeiro_nome[0] == segundo_nome[0]:
    print(f'As duas letras são iguais, sendo {primeiro_nome[0]}!')
else:
    print(
        f'As letras são diferentes, a do primeiro nome "{primeiro_nome[0]}"\n'
        f'Do segundo nome "{segundo_nome[0]}"'
    )
