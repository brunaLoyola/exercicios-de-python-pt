def aumentar(preco=0, taxa=0, formato=False):
    retorno = preco + (preco * taxa/100)
    return retorno if formato is False else moeda(retorno)


def diminuir(preco=0, taxa=0, formato=False):
    retorno = preco - (preco * taxa/100)
    return retorno if formato is False else moeda(retorno)


def metade(preco=0, formato=False):
    retorno = preco/2
    return retorno if formato is False else moeda(retorno)


def dobro(preco=0, formato=False):
    retorno = preco*2
    return retorno if formato is False else moeda(retorno)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxa_au=10, taxa_re=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_au}% de aumento: \t{aumentar(preco, taxa_au, True)}')
    print(f'{taxa_re}% de redução: \t{diminuir(preco, taxa_re, True)}')
    print('-' * 30)
