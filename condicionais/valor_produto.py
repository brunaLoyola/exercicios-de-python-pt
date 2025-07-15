"""
Curso em video: Desconto em compra

Calcula o valor final de um produto com base nas condições escolhidas.
- à vista dinheiro / cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

valor_produto = float(input('Digite o valor do produto: '))

opcao = int(
            input(
                '1 - à vista dinheiro/cheque\n'
                '2 - à vista no cartão\n'
                '3 - 2x no cartão\n'
                '4 - 3x ou mais no cartão \n'
            )
        )

if opcao == 1:
    valor = valor_produto - (valor_produto * 0.10)
    print(
        'Opção á vista no dinheiro/cheque\n'
        f'Essa opção tem um desconto de 10% ficando no valor de R${valor:.2f}'
    )

elif opcao == 2:
    valor = valor_produto - (valor_produto * 0.05)
    print(
        'Opção á vista no cartão, essa opção tem um desconto de 5%\n'
        f'Ficando no valor de R${valor:.2f}'
    )

elif opcao == 3:
    print(
        f'Opção 2x no cartão, essa opção tem o valor de R${valor_produto}\n'
        f'Ficando em 2x {valor_produto / 2}')

elif opcao == 4:
    quantidade = int(input('Qual a quantidade de vezes irá pagar: '))
    valor = valor_produto + (valor_produto * 0.20)
    print(
        f'Opção de {quantidade}x no cartão, essa opção tem um juros de 20%\n'
        f'Ficando no valor total de R${valor:.2f}\n'
        f'Em parcelas de R${valor_produto/quantidade:.2f}'
    )

else:
    print('Opção inválida !!')
