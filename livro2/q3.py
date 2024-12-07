
compra = float(input("Digite o valor de compra do produto: "))
venda = float(input("Digite o valor de venda do produto: "))


lucro = ((venda - compra) / compra) * 100

if lucro < 10:
    print(f"A margem de lucro foi menor que 10%.")
elif 10 <= lucro <= 20:
    print(f"A margem de lucro foi entre 10% e 20%.")
else:
    print(f"A margem de lucro foi superior a 20%.")
