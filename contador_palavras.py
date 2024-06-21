#recebe uma frase digitada pelo usuário e retorna o número de palavras presentes na frase

frase = input('digite uma frase:')
palavras: list = frase.split(' ')
contador = 0
for i in palavras:
    contador += 1
print(str(contador))
