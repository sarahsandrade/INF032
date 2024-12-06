import xlrd
import matplotlib.pyplot as plt
import numpy as num
'''8. Os dados a seguir representam os preços diários de fechamentos no pregão da
Bovespa entre os meses de setembro e outubro de 2019. A coluna A do Excel se
refere a VALE3 (Vale do Rio Doce) e a coluna B indica GGBR4 (Gerdau). Os dados
estão em um arquivo Excel na planilha denominada Plan1.
Deseja-se, então, que esses dados sejam importados para o Python com a biblioteca
xlrd e que se responda aos itens a seguir.'''
file = xlrd.open_workbook("plan1.xls")
plan = file.sheet_by_name('pl1')
'''(a) Importar os dados do Excel e transformar a coluna A em uma variável que
represente a Vale e a coluna B em outra variável que represente a coluna B.'''
VALE3 = plan.col_values(0)
GGBR4 = plan.col_values(1)
'''(b) Transformar as variáveis em vetores usando a biblioteca numpy.'''
VALE3 = num.array(VALE3, dtype=str)
VALE3 = num.char.replace(VALE3, ',', '.')
VALE3 = VALE3.astype(float)
print(f'VALE3 = {VALE3}')
GGBR4 = num.array(GGBR4,dtype=str)
GGBR4 = num.char.replace(GGBR4, ',', '.')
GGBR4 =GGBR4.astype(float)
print(f' GGBR4 = {GGBR4}')

'''(c) Fazer os dois gráficos dos preços da Vale e da Gerdau usando subplot. Colocar
a Vale na parte superior da figura e a Gerdau na parte inferior.'''
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(VALE3, label="VALE3", color='blue')
plt.title("Preços da Vale (VALE3)")
plt.xlabel("Dias")
plt.ylabel("Preço")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(GGBR4, label="GGBR4", color='green')
plt.title("Preços da Gerdau (GGBR4)")
plt.xlabel("Dias")
plt.ylabel("Preço")
plt.grid(True)

plt.tight_layout()
plt.show()
'''(d) Calcular os retornos das duas empresas e plotar os quatro gráficos (preço da
Vale e seu retorno; preço da Gerdau e seu retorno) no formato de uma matriz
com 2×2 elementos.'''
VALE3_returns = num.diff(VALE3) / VALE3[:-1]
GGBR4_returns = num.diff(GGBR4) / GGBR4[:-1]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(VALE3, color='blue')
plt.title("Preços da Vale (VALE3)")
plt.xlabel("Dias")
plt.ylabel("Preço")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(VALE3_returns, color='orange')
plt.title("Retornos da Vale (VALE3)")
plt.xlabel("Dias")
plt.ylabel("Retorno")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(GGBR4, color='green')
plt.title("Preços da Gerdau (GGBR4)")
plt.xlabel("Dias")
plt.ylabel("Preço")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(GGBR4_returns, color='red')
plt.title("Retornos da Gerdau (GGBR4)")
plt.xlabel("Dias")
plt.ylabel("Retorno")
plt.grid(True)

plt.tight_layout()
plt.show()