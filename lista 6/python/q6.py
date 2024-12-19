'''6.Entrar com vários números ate entrar com o numero 999. para cada numero imprimir seus divisores;'''
n = 0
while n != 999:
    n = int(input("Digite um numero: "))
    for i in range (1,n):
        if n%i == 0:
            print(f'{i}')
    print(f'{n}')