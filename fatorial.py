def fatorial(numero: int) -> int:
    resultado = 1
    for i in range(2, (numero + 1)):
        resultado *= i
    return resultado