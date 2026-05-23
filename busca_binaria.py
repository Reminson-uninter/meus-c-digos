dados = [1, 3, 5, 7, 9, 11, 13]

def busca_binaria(inicio, fim, dados, busca):
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if (busca > dados[meio]):  # se o número procurado for maior que o valor da posição central
            inicio = meio + 1      # descarta a metade esquerda e continua à direita
        elif (busca < dados[meio]): # se o número procurado for menor que o valor da posição central
            fim = meio - 1          # descarta a metade direita e continua à esquerda
        else:
            return meio             # encontrou o elemento, retorna o índice
    return -1                       # se não encontrar, retorna -1

print(busca_binaria(0, len(dados)-1, dados, 7))
