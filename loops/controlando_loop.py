"""
Exercício:

- Imprime números de 1 a 5 usando um loop
- Permite ao usuário digitar a senha até que informe a correta
"""

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

while True:
    senha = int(input('Digite uma senha: '))

    if senha == 1234:
        print('Senha correta.')
        break
    else:
        print('Senha incorreta.')
