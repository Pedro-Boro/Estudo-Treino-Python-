#Recebe uma lista de números inteiros e retorna a quantidade de números pares da lista.

teste1 = [1, 5, 6, 8, 3]
teste2 = [2, 9, 5, 8, 4]
teste3 = [1, 3, 5]
teste4 = [2]

def parOuImpar(numeros: list) -> int:
    '''
    Python3 doctest - Exemplos:
    >>> parOuImpar(teste1)
    2
    >>> parOuImpar(teste2)
    3
    >>> parOuImpar(teste3)
    0
    >>> parOuImpar(teste4)
    1
    '''

    qntPares = 0
    for numero in numeros:
        if numero % 2 == 0:
            qntPares += 1
        else: continue
    return qntPares