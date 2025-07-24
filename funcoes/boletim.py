"""
Exercicio:

Função notas() que recebe várias notas de alunos
e retorna um dicionário com quantidade, maior, menor,
média da turma e situação (opcional).
Inclui docstrings para consulta.
"""


def notas(*nota, sit=False):
    """
    Calcula estatísticas de uma turma a partir das notas informadas.

    Parâmetros:
        *nota: notas dos alunos
        sit (bool): se True, inclui a situação da turma

    Retorna:
        dict: com total, maior, menor, média e, opcionalmente, situação
    """
    dicionario = dict()
    dicionario['total'] = len(nota)
    dicionario['maior'] = max(nota)
    dicionario['menor'] = min(nota)
    dicionario['media'] = sum(nota) / len(nota)

    if sit:
        if dicionario['media'] > 7:
            dicionario['situação'] = 'Boa'
        elif dicionario['media'] >= 5:
            dicionario['situação'] = 'Razoável'
        else:
            dicionario['situação'] = 'Ruim'
    return dicionario


resposta = notas(5.5, 10, 6.7, 9)
print(resposta)
