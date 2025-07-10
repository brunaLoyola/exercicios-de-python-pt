"""
Curso em video: Conversor de base

Converte um número inteiro para binário, octal ou hexadecimal
conforme a escolha do usuário.
"""

numero = int(input('Digite um número inteiro para conversão: '))

opcao = int(
        input(
            'Informa a opção desejada para conversão \n'
            '1 - Para Binário\n'
            '2 - Para octal \n'
            '3 - Para Hexadecimal \n'
        )
    )

if opcao == 1:
    numero_bin = bin(numero)
    print(f'Número convertido: {numero_bin[2:]}.')
elif opcao == 2:
    numero_octal = oct(numero)
    print(f'Número convertido: {numero_octal[2:]}.')
elif opcao == 3:
    numero_hexa = hex(numero)
    print(f'Número convertido: {numero_hexa[2:]}.')
else:
    print('Opção inválida.')
