'''6. Abrir o arquivo bov.txt do exercício anterior no Console e imprimir o resultado
dos elementos existentes nele.'''
file = open('bov.txt','r')
print(f'{file.read()}')