'''3.Entrar com vários números positivos e imprimir a media dos números digitados. o programa acaba quando se informar que não deseja mais continuar.'''
n = 0 
i = 0
while n % 2 == 0:
    aux = int(input('Digite um numero positivo:'))
    if aux > 0:
        n += aux
        i +=1
    aux = input('Deseja continuar ?\nS - Sim\nN - Não\n')
    aux = aux.upper()
    if aux == 'N':
        break
print(f'A media dos numeros digitados é igual a: {n/i}')
