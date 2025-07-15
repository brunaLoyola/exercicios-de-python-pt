"""
Exercício:

Valida o acesso de um usuário com base na idade e exibe os dados do cadastro.
"""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
email = input('Digite seu email: ')

if idade < 18 and idade >= 0:
    print('Acesso negado')
elif idade >= 18:
    print(f' Nome:{nome}\n Idade:{idade}\n Email:{email}.')
else:
    print('Idade inválida')
