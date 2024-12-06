'''3. Criar a lista de números num=[3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2] e fatiá-la con-
forme os itens a seguir:'''

num=[3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2]

'''(a) Fatiar do elemento de índice 2 ao de índice 3.'''
print(f'{num[2:4]}')
'''(b) Fatiar do quinto elemento ao nono elemento.'''
print(f'{num[5:10]}')
'''(c) Fatiar do elemento de índice 1 ao último.'''
print(f'{num[1:]}')
'''(d) Fatiar do primeiro elemento ao último.'''
print(f'{num[:]}')
'''(e) Fatiar do primeiro elemento ao último saltando de três em três elementos.'''
print(f'{num[::3]}')
'''(f) Selecionar o último elemento da lista.'''
print(f'{num[-1]}')
'''(g) Selecionar os três últimos elementos da lista.'''
print(f'{num[-3:]}')
'''(h) Selecionar os quatro primeiros elementos da lista.'''
print(f'{num[:4]}')
'''(i) Contar o número de elementos da lista.'''
print(f'Total de elemntos:{len(num)}')
'''(j) Contar quantas vezes aparece o número 1 na lista.'''
print(f'Num de ocorrencias de 1: {num.count(1)}')