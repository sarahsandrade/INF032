import math
'''2. Assumir como constante no comando de linha do Python x = 3 e y = 6 e imprimir
usando PRINT( ) o resultado das equações seguintes:'''
x = 3
y = 6
'''(a) w = e'x − ln(y)'''
print(f'W = {math.exp(x) - math.log(y)}')
'''(b) z = x*y'2 + y*cos(x)'''
print(f'Z = {x * math.pow(y,2) + y * math.cos(x)}')
'''(c) s = √(x/y + ln(x+y)+tan(x))'''
print(f'S = {math.sqrt(x/y + math.log(x+y) + math.tan(x))}')