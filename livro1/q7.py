import statistics as st
'''7. Observar a seguinte lista de dados, lista= [2, 2, 3, 3, 3, −1, −1, −2, 0, 0, 0, 2, 4, 5, 1,
2, 2, 0, 0, 0,2 ,1, 5, 5, 7, 6, 5, 0, 0]. Programar o Console para encontrar as seguintes
medidas estatísticas:'''
lista= [2, 2, 3, 3, 3, -1,-1,-2, 0, 0, 0, 2, 4, 5, 1, 2, 2, 0, 0, 0,2 ,1, 5, 5, 7, 6, 5, 0, 0]
'''(a) Soma de todos os elementos.'''
print(f'{sum(lista)}')
'''(b) Máximo elemento da lista.'''
print(f'{max(lista)}')
'''(c) Mínimo elemento da lista.'''
print(f'{min(lista)}')
'''(d) Média dos elementos da lista.'''
print(f'{st.median(lista)}')
'''(e) Mediana dos elementos da lista.'''
print(f'{st.mean(lista)}')
'''(f) Moda dos elementos da lista.'''
print(f'{st.mode(lista)}')
'''(g) Desvio-padrão amostral.'''
print(f'{st.stdev(lista)}')
'''(h) Desvio-padrão populacional.'''
print(f'{st.pstdev(lista)}')
'''(i) Contar o número de vezes que aparece o número 0.'''
print(f'N de vezes q o 0 aparece: {lista.count(0)}')
'''(j) Contar o número de vezes que aparece o número 5.'''
print(f'N de vezes q o 5 aparece: {lista.count(5)}')
'''(k) Ordenar a lista em ordem crescente.'''
lista.sort()
print(f'{lista}')
'''(l) Ordenar a lista em ordem decrescente.'''
lista.reverse()
print(f'{lista}')