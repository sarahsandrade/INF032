
valor_compra = float(input("Digite o valor de compra do produto: "))
valor_venda = float(input("Digite o valor de venda do produto: "))


lucro = ((valor_venda - valor_compra) / valor_compra) * 100

if lucro < 10:
    print(f"A margem de lucro foi de {lucro:.2f}%. Está na faixa: menor que 10%.")
elif 10 <= lucro <= 20:
    print(f"A margem de lucro foi de {lucro:.2f}%. Está na faixa: entre 10% e 20%.")
else:
    print(f"A margem de lucro foi de {lucro:.2f}%. Está na faixa: superior a 20%.")
