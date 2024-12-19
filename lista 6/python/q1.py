'''1. Entrar como n's números e imprimir o triplo de cada. o programa encerra quando entrar com o numero 999;'''

n = 0
while n != 999:
    n = int(input("Digite um numero: "))
    print(f'O triplo de {n} = {n*3}')