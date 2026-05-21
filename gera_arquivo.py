
import numpy
import plotly.express


vetor_a = numpy.linspace(0,1000,100) # criando um vetor de 100 elementos entre 0 e 1000
vetor_b = numpy.linspace(10,3000,100) # criando um vetor de 100 elementos entre 10 e 3000
vetor_c = numpy.linspace(10, 8000, 100) # criando um vetor de 00 elementos entre 10 e 8000

print(f'Vetor A: {vetor_a}\n')
print(f'Vetor B: {vetor_b}\n')
print(f'Vetor C: {vetor_c}\n')


# Numpy já tem métodos bem diretos de como salvar um arquivo no formato .txt
numpy.savetxt('vetor_a.txt', vetor_a, fmt='%.2f', delimiter=' ') # o fmt é para formatar a saída do arquivo, nesse caso, com 2 casas decimais
numpy.savetxt('vetor_b.txt', vetor_b, fmt='%.2f', delimiter=' ')
numpy.savetxt('vetor_c.txt', vetor_c, fmt='%.2f', delimiter=' ')

# Agora podemos utilizar uma das várias bibliotecas para plotar gréficos

array_a = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=' ')
array_b = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=' ')
array_c = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=' ')

print(f'Array A: {array_a}\n')
print(f'Array B: {array_b}\n')
print(f'Array C: {array_c}\n') 

array_abc = numpy.array([array_a, array_b, array_c])
print(f'Array ABC: {array_abc}\n')

array_abc = array_abc.transpose() # transpondo o array para ficar no formato correto para o plotly
print(f'Array ABC transposto: {array_abc}\n')

fig = plotly.express.line(array_abc)
fig.show() 