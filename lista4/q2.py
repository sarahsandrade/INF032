'''2. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana,
tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo
recebem listas vazias, ou você tem aula?).'''
semana = {}
semana['segunda'] = []
semana['terça'] = ['Redes de Computadores II']
semana['quarta'] = ['Engenharia de Software']
semana['quinta'] = ['Engenharia de Software','Redes de Computadores II']
semana['sexta'] = ['Tópicos Avançados II','Engenharia de Software']
semana['sábado'] = []  
semana['domingo'] = [] 
print(f'{semana}')