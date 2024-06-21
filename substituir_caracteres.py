#Recebe uma string e substitui todas as vogais por '?'.

def substituirCaracteres(string: str) -> str:
    '''
    Python3 doctest - Exemplos:
    >>> substituirCaracteres('Pedro Henrique')
    'P?dr? H?nr?q??'
    >>> substituirCaracteres('GOIABA')
    'G???B?'
    '''

    vogais = 'AEIOUaeiou'
    stringf = []
    for caractere in string:
        if caractere in vogais:
            stringf.append('?')
        else: stringf.append(caractere)
    return ''.join(stringf)