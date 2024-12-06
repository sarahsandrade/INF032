'''5. Abrir um arquivo chamado bov.txt e salvar os dados das siglas das ações e seus
valores na seguinte ordem: 'petr4', 'vale3', 'ggbr4', 28.4, 31.3, 15.76.'''
dados = ['petr4', 'vale3', 'ggbr4', 28.4, 31.3, 15.76]
file = open('bov.txt','w')
linha = ' '.join(dados[:3] + [str(dados[3]), str(dados[4]), str(dados[5])])
file.write(linha)
file.close()
