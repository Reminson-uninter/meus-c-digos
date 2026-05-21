# O que é um numpy: é uma biblioteca de código aberto para a linguagem de programação Python, que é amplamente utilizada para computação científica e análise de dados. O NumPy fornece suporte para arrays multidimensionais e matrizes, além de uma coleção de funções matemáticas para operar com esses arrays.
# Ele é fundamental para muitas outras bibliotecas de ciência de dados e aprendizado de máquina, como pandas, SciPy e scikit-learn.
# O numpy  trabalha como a ideia de vetores (arrays) e matrizes, que são estruturas de dados que permitem armazenar e manipular grandes conjuntos de dados de forma eficiente.
# Ele oferece uma ampla gama de funções para realizar operações matemáticas, como álgebra linear, estatística, transformações de Fourier e muito mais.

import numpy
primeiro_array = numpy.zeros(1000000000, dtype=numpy.float32) 
print('1 - Conteúdo da Lista:{}, o tamanho da lista é: {}'.format(primeiro_array, len(primeiro_array) ))


primeiro_array = numpy.ones(100000)
print('2 - Conteúdo da Lista:{}, o tamanho da lista é: {}'.format(primeiro_array, len(primeiro_array) ))


#linspace(inicio,fim,quantidade de elementos)
#primeiro_array = numpy.linspace(10, 100, 10) 

#print('3 - Conteúdo da Lista:{}, o tamanho da lista é: {}'.format(primeiro_array, len(primeiro_array) ))

# 2 - Comparar desempenho
import time
start_time = time.time()
lista = [0] * 1000000000
end_time = time.time()
elapsed_time = end_time - start_time
print('Tempo gasto para criar uma lista de zeros: {} segundos'.format(elapsed_time))


start_time = time.time()
primeiro_array= numpy.zeros(1000000000, dtype='uint8')
end_time = time.time()
elapsed_time = end_time - start_time
print('A criação de um array de 1 bilhão de elementos: {} segundos'.format(elapsed_time))

