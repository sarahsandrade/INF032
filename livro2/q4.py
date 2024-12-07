
baixa_historica = float(input("Digite o valor da baixa histórica da ação: "))
alta_historica = float(input("Digite o valor da alta histórica da ação: "))
preco_atual = float(input("Digite o valor atual da ação: "))

intervalo = alta_historica - baixa_historica

suporte = baixa_historica + intervalo * 0.3
resistencia = baixa_historica + intervalo * 0.6

if suporte <= preco_atual <= resistencia:
    print(f"O suporte é {suporte}, a resistência é {resistencia}")
    print("O preço da ação está dentro da faixa de suporte-resistência")
else:
    print(f"O suporte é {suporte}, a resistência é {resistencia}")
    print("O preço da ação está fora da faixa de suporte-resistência")
