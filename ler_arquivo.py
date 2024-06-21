#ler arquivo e retornar o numero de linhas que apresentam pelo menos uma das condiçoes:
#quantidade de 0 na linha é multiplo de 3
#quantidade de 1 na linha é multiplo de 2

def manipulacaoArquivo(arquivo: str) -> int:
    try:
        with open(arquivo, 'r') as arquivoAberto:
            linhas = 0
            for linha in arquivoAberto:
                if linha.count('0') % 3 == 0:
                    linhas +=1
                    continue
                elif linha.count('1') % 2 == 0:
                    linhas +=1
                    continue
                else: continue
        return linhas
    except FileNotFoundError:
        print('Arquivo não encontrado.')

dados = 'data.dat'
lerArquivo: int = manipulacaoArquivo(dados)
print(lerArquivo)