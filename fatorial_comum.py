


def fatorial(ini,busca):
    busca = int(input('Digite um numero: '))

    while True:
        if busca <0:
           return 0
        elif busca ==0 or busca==1:
           print('numero invalido,não pode ser menor que 1')
           busca = int(input('Digite um numero: '))
           continue

        else:
           for i in range(ini,busca+1):
               ini*= i
        return ini


saida = fatorial(1,busca='')
print('{}\n Fim'.format(saida))

