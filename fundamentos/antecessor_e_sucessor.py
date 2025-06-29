"""
Curso em video: Exercício que imprime o antecessor e o sucessor
O programa irá ler um número e mostrar o seu antecessor e o seu sucessor
"""

numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1

print(
    f' O número digitado é {numero} \n '
    f' Seu antecessor é {antecessor} \n '
    f' Seu sucessor é {sucessor}'
)
