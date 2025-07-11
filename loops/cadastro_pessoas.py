"""
Curso em Vídeo: Cadastro de pessoas

Lê idade e sexo de várias pessoas, perguntando ao usuário
se deseja continuar a cada cadastro.

No final, exibe:
- Quantas pessoas têm mais de 18 anos
- Quantos homens foram cadastrados
- Quantas mulheres têm menos de 20 anos
"""

maior_idade = 0
homens = 0
mulheres_novas = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Sexo M ou F: ').upper()

    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_novas += 1

    continuar = input('Deseja continuar [S] ou [N] ?').upper()
    if continuar == 'N':
        break

print(f'Existem {maior_idade} pessoas maiores de 18 anos')
print(f'Existem {homens} homens')
print(f'Existem {mulheres_novas} mulheres com menos de 20 anos')
