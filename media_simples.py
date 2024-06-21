#Recebe uma lista de valores numéricos e, se forem menos que 3 valores retorna False, se forem 3 valores ou mais retorna a média simples.

from typing import Union

teste1 = [10, 8, 5, 9]
teste2 = [5, 3, 4]
teste3 = [1, 2, 3, 4]
teste4 = [1, 2]

def mediaSimples(notas: list) -> Union[ float, bool]:
    #Retorno float pois existe a possibilidade da média das notas resultar em um numero não inteiro
    #Por exemplo: [1, 2, 3, 4] teria o retorno 2.5
    '''
    Python3 doctest - Exemplos:
    >>> mediaSimples(teste1)
    8.0
    >>> mediaSimples(teste2)
    4.0
    >>> mediaSimples(teste3)
    2.5
    >>> mediaSimples(teste4)
    False
    '''

    soma = sum(notas)
    quantidade = len(notas)
    if quantidade < 3:
        return False
    else: return soma / quantidade
    