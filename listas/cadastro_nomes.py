"""
Exericio:

Cria um menu interativo para cadastrar e listar nomes usando
laço while e armazenando dados em uma lista.
"""

lista_nomes = []

while True:
    opcao = int(
                input(
                    'Digite uma das opções:\n'
                    '01 - Cadastrar nome \n'
                    '02 - Listar nomes cadastrados\n'
                    '03 - Sair\n'
                )
            )

    if opcao == 1:
        nome = input('Digite um nome: ')
        lista_nomes.append(nome)
        continue

    elif opcao == 2:
        for item in lista_nomes:
            print(item)
        continue
    elif opcao == 3:
        break
    else:
        print('Opção incorreta')
        continue
