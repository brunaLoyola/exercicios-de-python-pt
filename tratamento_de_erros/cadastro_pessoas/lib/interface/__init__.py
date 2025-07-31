def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('Erro!! Por favor, digite um número inteiro')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return valor


def linha(tamanho=42):
    return '-'*tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    for c, item in enumerate(lista, start=1):
        print(f'{c} - {item}')
    print(linha())
    opc = leia_int('Sua opção: ')
    return opc
