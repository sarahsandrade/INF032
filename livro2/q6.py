
compra = float(input("Digite o valor da compra: "))


if 0 <= compra <= 20:
    des = 5/100
elif 21 <= compra <= 50:
    des = 10/100
elif 51 <= compra <= 100:
    des = 15/100
elif 101 <= compra <= 1000:
    des = 20/100
elif compra > 1000:
    des = 30/100


valor_desconto = compra * des
valor_final = compra - valor_desconto
print(f"Valor a ser pago: {valor_final}")
