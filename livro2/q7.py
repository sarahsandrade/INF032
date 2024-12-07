n = int(input("Digite o número total de vendas: "))

pares = 0
impares = 0
i = 0
while i < n:
    if i % 2 == 0:
        pares+=i
    else:
        impares+=i
    i +=1

print(f'Soma dos pares ={pares}\nSoma dos impares= {impares}')