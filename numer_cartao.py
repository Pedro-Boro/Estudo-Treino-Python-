#encontrar número do cartao sabendo que ele é multiplo de 123457, os primeiros 6 digitos são '543210', os 4 ultimos sao 1234 e o digito de Luhn é valido.


#declara listas
listaImpar = []
listaPar = []

#para cada numero de 6 digitos, testar um cartão
for i in range(100000, 999999): 
    numeroCartao = '543210' + str(i) + '123'

    #guardar os digitos em suas respectivas listas
    for indice, digito in enumerate(numeroCartao):
        if indice % 2 == 0:
            listaPar.append(int(digito))
        else:
            if (int(digito) * 2) > 9:
                listaImpar.append(((int(digito) * 2) // 10) + ((int(digito) * 2) % 10))
            else: 
                listaImpar.append((int(digito) * 2))

    #somar ambas as listas
    somaImpar = sum(listaImpar)
    somaPar = sum(listaPar)
    somaTotal = somaImpar + somaPar

    #limpa as listas para não estragar o loop
    listaImpar.clear()
    listaPar.clear()

    #testa os rtequisitos para ser um cartão válido
    ultimoDigito = 10 - (somaTotal % 10)
    if ultimoDigito == 4:
        if int(numeroCartao + '4') % 123457 == 0:
            print(numeroCartao + '4')
            break
        else: print('numero nao divisivel por 123457' + '        ' + numeroCartao + '4')
    else: print('numero final diferente de 4')
