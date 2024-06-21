#recebe mes como um inteiro entre 1 e 12, caso o numero informado nao esteja nesse parâmetro, responder: 'mes desconhecido'.

def mesCorrespondente(mes: int) -> str:
    '''
    Python3 doctest - Exemplo:
    >>> mesCorrespondente(1)
    'Janeiro'
    >>> mesCorrespondente(2)
    'Fevereiro'
    >>> mesCorrespondente(3)
    'Março'
    >>> mesCorrespondente(4)
    'Abril'
    >>> mesCorrespondente(5)
    'Maio'
    >>> mesCorrespondente(6)
    'Junho'
    >>> mesCorrespondente(7)
    'Julho'
    >>> mesCorrespondente(8)
    'Agosto'
    >>> mesCorrespondente(9)
    'Setembro'
    >>> mesCorrespondente(10)
    'Outubro'
    >>> mesCorrespondente(11)
    'Novembro'
    >>> mesCorrespondente(12)
    'Dezembro'
    >>> mesCorrespondente(13)
    'Mês Desconhecido'
    '''

    if mes == 1:
        strMes = 'Janeiro'
    elif mes == 2:
        strMes = 'Fevereiro'
    elif mes == 3:
        strMes = 'Março'
    elif mes == 4:
        strMes = 'Abril'
    elif mes == 5:
        strMes = 'Maio'
    elif mes == 6:
        strMes = 'Junho'
    elif mes == 7:
        strMes = 'Julho'
    elif mes == 8:
        strMes = 'Agosto'
    elif mes == 9:
        strMes = 'Setembro'
    elif mes == 10:
        strMes = 'Outubro'
    elif mes == 11:
        strMes = 'Novembro'
    elif mes == 12:
        strMes = 'Dezembro'
    else: strMes = 'Mês Desconhecido'

    return strMes
