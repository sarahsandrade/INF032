'''4. Criar a lista com nomes das bolsas de valores do mundo: Bolsas = ['dow', 'ibov', 'ftse',
'dax', 'nasdaq', 'cac']. Fatiá-la conforme os itens a seguir.'''
Bolsas = ['dow', 'ibov', 'ftse','dax', 'nasdaq', 'cac']
'''(a) Selecionar as três primeiras.'''
print(f'{Bolsas[:3]}')
'''(b) Incluir a sublista Bs = ['hong kong', 'merval'] na lista anterior.'''
Bs = ['hong kong', 'merval']
Bolsas.extend(Bs)
print(f'{Bolsas}')
'''(c) Descobrir qual o índice da 'nasdaq'.'''
print(f'{Bolsas.index('nasdaq')}')
'''(d) Remover 'cac' da lista.'''
Bolsas.remove('cac')
print(f'{Bolsas}')
'''(e) Inserir “sp&500” como índice 2 na lista de bolsas, mas sem excluir nenhum
elemento já inscrito.'''
Bolsas.insert(2,'sp&500')
print(f'{Bolsas}')