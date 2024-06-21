frase = input('digite uma frase:')
palavras: list = frase.split(' ')
contador = 0
for i in palavras:
    contador += 1
print(str(contador))