def calculadora(num1: float, num2: float, operacao: str):
    match operacao:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _ :return 'Insira uma operação válida! '

numero1 = float(input('Insira o primeiro valor: '))
sinal = input('Insira o sinal da operação que deseja realizar: ')
numero2 = float(input('Insira o segundo valor: '))

calcular = calculadora(numero1, numero2, sinal)
print(str(calcular))