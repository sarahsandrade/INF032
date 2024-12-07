n = int(input("Digite a quantidade de meses:"))
i = 1
s = 0
while i <=n:
    s+= (70 - (i - 1)) / (7 * i)
    i+=1
print(f'{s}')