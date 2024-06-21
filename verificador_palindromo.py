ligado = True
while ligado:
    palavra = input('Insira a palavra que deseja testar: ')
    if ' ' in palavra:
        print('Somente uma palavra!')
    else:
        if palavra == palavra[::-1]:
            print(f'A palavra {palavra} é um Palíndromo!')
        else: print(f'A palavra {palavra} não é um Palíndromo!')
    continuar = input('deseja tentar novamente? ')
    if continuar == 'S' or continuar == 's' or continuar == 'Sim' or continuar == 'sim':
        ligado = True
    else: ligado = False 