"""
Curso em Vídeo: Cadastro de produtos

Lê o nome e o preço de vários produtos, perguntando
ao usuário se deseja continuar. Ao final exibe:
- O total gasto na compra
- Quantos produtos custam mais de R$1000
- O nome do produto mais barato
"""

total = 0
mais_de_mil = 0
nome_barato = ''
cont = 0
menor = 0
while True:
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    total += valor
    cont += 1

    if cont == 1:
        nome_barato = nome
        menor = valor
    else:
        if valor < menor:
            nome_barato = nome
            menor = valor

    if valor > 1000:
        mais_de_mil += 1

    continuar = input('Deseja continuar ? [S] / [N]: ').upper()

    if continuar == 'N':
        break

print(f' O total da compra deu R${total:.2f} \n'
      f'A quantidade de produtos a cima de R$1.000,00 é de {mais_de_mil}')
print(f'O produto de menor valor é o {nome_barato} custando R${menor:.2f}')
