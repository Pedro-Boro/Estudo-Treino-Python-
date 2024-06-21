#Receber uma string e retorná-la invertida (bar -> rab).

def inverterString(string: str) -> str:
    '''
    Python3 doctest - Exemplos:
    >>> inverterString('teste')
    'etset'
    >>> inverterString('Goiaba')
    'abaioG'
    '''

    return string[::-1]