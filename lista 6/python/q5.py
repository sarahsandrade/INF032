'''5.Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caracter de cada nome;'''
name = ''
while name != 'FIM':
    name = input("Digite um nome:")
    name = name.upper()
    print(name)