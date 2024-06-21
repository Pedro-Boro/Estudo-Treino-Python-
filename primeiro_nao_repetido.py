#recebe um array com valores inteiros e retorna o primeiro que nao se repete.

teste1 = [1, 1, 2, 5, 2, 7, 9]
teste2 = [6, 7, 8, 7, 6, 8]
teste3 = [1, 2, 3, 4, 5, 6]

def primeiroValorNaoRepetido(numeros: list) -> int:
    '''
    Python3 doctest - Exemplos:
    >>> primeiroValorNaoRepetido(teste1)
    5
    >>> primeiroValorNaoRepetido(teste2)

    >>> primeiroValorNaoRepetido(teste3)
    1
    '''

    contagem = {}
    for numero in numeros:
        if numero in contagem:
            contagem[numero] += 1
        else: contagem[numero] = 1
    for numero in numeros:
        if contagem[numero] == 1:
            return numero