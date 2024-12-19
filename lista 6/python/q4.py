'''4.Entrar com vários números e informar quantos números entre 100 e 200 foram digitados. quando o valor 0 for digitado o programa deve encerrar;'''
n = 1 
i = 0
while n != 0:
    n = int(input('Digite um numero:'))
    if n < 200 and n > 100:
        i+=1
print (f" Qtd de numeros digitados entre 100 e 200: {i}")