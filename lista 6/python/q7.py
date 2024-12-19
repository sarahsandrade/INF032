'''7.Dado um pais A, com 5.000.0000 de habitantes e uma taxa de natalidade de 3% ao ano, e um pais B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano. calcular e imprimir o tempo necessário para que a população do pais A ultrapasse a população do pais B;
'''
A = 5000000
B = 7000000
anos = 0
tA =0.03
tB = 0.02
print(f'País A = {A}\nPaís B ={B}\nContagem de anos = {anos}')
while A <= B:
    nA = tA* A
    nB = tB* B
    anos +=1
    A += nA
    B += nB
print(f'País A = {A}\nPaís B ={B}\nContagem de anos = {anos}')