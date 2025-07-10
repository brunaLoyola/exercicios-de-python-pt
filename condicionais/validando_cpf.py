"""
Exercício:

Valida um CPF removendo a pontuação e
verificando se possui 11 dígitos numéricos.
"""

cpf = (
    input('Digite seu CPF (com traços e pontos): ')
    .replace('.', '')
    .replace('-', '')
)

if cpf.isdigit() and len(cpf) == 11:
    print(f'Seu cpf é {cpf} e contém os 11 dígitos')
else:
    print('Cpf incorreto, não contém os 11 dígitos numéricos')
