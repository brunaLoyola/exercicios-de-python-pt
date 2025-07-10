"""
Curso em video: Aprovação de empréstimo

Simula a análise de um empréstimo para compra de casa
com base no salário e prazo de pagamento.
"""

valor_casa = float(input('Informe o valor do imóvel R$'))
salario = float(input('Informe o seu salário R$'))
anos_pagar = int(input('Informe em quantos anos irá pagar: '))
valor_prestacao = valor_casa / (anos_pagar * 12)
porcentagem_salario = salario * 0.30

if valor_prestacao <= porcentagem_salario:
    print(
        f'Seu emprestimo foi aprovado !! \n'
        f'Valor da parcela: R${valor_prestacao:.2f} \n'
        f'Quantidade de anos: {anos_pagar}'
    )
else:
    print(
        f'Emprestimo negado !! \n'
        f'O valor os 30% do seu salário ficando em R${valor_prestacao:.2f}.'
    )
