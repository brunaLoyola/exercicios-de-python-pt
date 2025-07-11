"""
Curso em Vídeo: Cadastro de grupo

Lê o nome, idade e sexo de 4 pessoas e exibe:
- A média de idade do grupo
- O nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
"""

soma = 0
menos_de_vinte = 0
idade_mais_velho = 0
nome_mais_velho = ''

for c in range(1, 5):
    nome = input('Digite seu nome: ')
    idade = int(input('Qual sua idade: '))
    sexo = int(
        input(
            'Informa seu sexo: \n'
            '1 - Feminino \n'
            '2 - Masculino \n'
        ))

    soma += idade

    if sexo == 1 and idade < 20:
        menos_de_vinte += 1
    elif sexo == 2 and c == 1:
        idade_mais_velho = idade
        nome_mais_velho = nome
    elif sexo == 2 and c != 1 and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome

print(f'A média das idades é {soma/4}')
print(
    f'O homem mais velho tem {idade_mais_velho} anos\n'
    f'E se chama {nome_mais_velho}'
)
print(f'A quantidade de mulheres com menos de 20 anos é de {menos_de_vinte}')
