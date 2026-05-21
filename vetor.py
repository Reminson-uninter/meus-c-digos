#criando um vertor usando numpy
import numpy

rng = numpy.random.default_rng() # numpy tem seus métodos random inclusos
vetor = rng.random(10) # criando um vetor de 10 elementos
print(f'Array de 1 Dimensão (VETOR) randômico: {vetor}\n')

matriz = rng.random((4, 4)) 
m_coluna = numpy.sort(matriz, axis=0) # ordenando a matriz por coluna
m_linha = numpy.sort(matriz, axis=1) # ordenando a matriz por linha
m_col_lin = numpy.sort(matriz, axis=0) # ordenando a matriz por coluna e linha
print(f'Ordenando a matriz por coluna: {m_coluna}\n')


tensor = rng.random((4, 4, 4))
print(f'Array de 3 Dimensões (TENSOR) randômico: {tensor}\n')


# Ordenando o vetor
vetor_ordenado = numpy.sort(vetor)
print(f'Vetor ordenado: {vetor_ordenado}\n')