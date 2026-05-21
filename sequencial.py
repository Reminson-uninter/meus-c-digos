
def buscaSequencial(dados,busca):
    achou =0
    i =0
    while i < len(dados) and achou == 0:
        if dados[i] == busca:
            achou = 1
        else:
            i = i + 1
    if(achou == 0):
        return -1
    else:
        return i +1
    
    
dados = [0,1,2,3,4,5,6,7,8,9,10]
busca = 8  



print(buscaSequencial(dados,busca))    