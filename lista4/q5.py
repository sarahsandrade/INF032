'''5. Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome,
idade, telefone. O programa deve ler um 5 dados completos, e imprimir todos os itens do
dicionário no formato chave: nome-idade-fone.'''
agenda = {}

agenda['12345678901'] = {'nome': 'João', 'idade': 25, 'telefone': '1234-5678'}
agenda['98765432100'] = {'nome': 'Ana', 'idade': 30, 'telefone': '9876-5432'}
agenda['45612378912'] = {'nome': 'Carlos', 'idade': 40, 'telefone': '4567-8910'}
agenda['78945612300'] = {'nome': 'Maria', 'idade': 35, 'telefone': '7894-5612'}
agenda['32165498700'] = {'nome': 'Fernanda', 'idade': 28, 'telefone': '3216-5498'}

print('12345678901:', f"{agenda['12345678901']['nome']}-{agenda['12345678901']['idade']}-{agenda['12345678901']['telefone']}")
print('98765432100:', f"{agenda['98765432100']['nome']}-{agenda['98765432100']['idade']}-{agenda['98765432100']['telefone']}")
print('45612378912:', f"{agenda['45612378912']['nome']}-{agenda['45612378912']['idade']}-{agenda['45612378912']['telefone']}")
print('78945612300:', f"{agenda['78945612300']['nome']}-{agenda['78945612300']['idade']}-{agenda['78945612300']['telefone']}")
print('32165498700:', f"{agenda['32165498700']['nome']}-{agenda['32165498700']['idade']}-{agenda['32165498700']['telefone']}")
