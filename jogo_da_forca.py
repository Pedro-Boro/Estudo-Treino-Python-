import random

#loop para manter o jogo aberto
jogo = True
while jogo:
    jogando = True
    vidas = 5

#lista de palavras possiveis
    palavras = ['abacaxi', 'borboleta', 'calculadora', 'deserto', 'elefante', 'ferramenta']

#o programa escolhe aleatoriamente uma palavra.
    palavra = random.choice(palavras)

#armazena a palavra certa
    palavraCerta: list = []
    for letra in palavra:
        palavraCerta.append(letra)

#printa a palavra toda com _
    underline = []
    for letra in palavraCerta:
        underline.append('_')
    print('\n'+ '     '+''.join(underline) + '     ' + str(vidas)+' Vidas\n')

#recebe input do jogador para uma letra ou palavra
    while jogando:
        jogada = input('Insira uma letra ou palavra: ')

#se estiver certo, substitui na palavra de _
        if jogada in palavraCerta:
            indices = [i for i, x in enumerate(palavraCerta) if x == jogada]
            for index in indices:
                underline[index] = jogada
            print('\n'+''.join(underline) + '     ' + str(vidas)+' Vidas\n')

#caso o jogador acerte a palavra, ele ganha.
        elif jogada == palavra:
            print('Venceu!\n')
            jogando = False

#se estiver errado, perde uma vida de 5.
        else:  
            vidas -= 1
            print('\n'+''.join(underline) + '     ' + str(vidas)+' Vidas\n')
        if vidas == 0:
            print('Perdeu!\n')
            jogando = False

#caso o jogador encontre todas as letras, ele ganha.
        if '_' not in underline:
            print('Venceu!\n')
            jogando = False

#pergunta se o jogador gostaria de jogar novamente
    jogarNovamente = input('Deseja jogar novamente? ')
    if jogarNovamente == 's' or jogarNovamente == 'S' or jogarNovamente == 'sim' or jogarNovamente == 'Sim':
        jogo = True
    else: jogo = False
