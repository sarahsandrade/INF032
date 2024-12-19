'''2.Entrar com números enquanto forem positivos, e imprimir quantos números foram digitados;'''

n = 0 
i = 0
while n % 2 == 0:
    n = int(input('Digite um numero:'))
    i+=1
    print (f" Qtd de numeros digitados: {i}")