#Recebe uma lista de valores inteiros e retorna-os em ordem crescente.

teste1 = []
teste2 = [9, 4, 5, 2]
teste3 = [4, 4, 7, 10, 3, 1, 1, 0]

def ordenarArray(numeros: list) -> list:
    '''
    Python3 doctest - Exemplos:
    >>> ordenarArray(teste1)
    []
    >>> ordenarArray(teste2)
    [2, 4, 5, 9]
    >>> ordenarArray(teste3)
    [0, 1, 1, 3, 4, 4, 7, 10]
    '''

    numeros.sort()
    return numeros