
import math  

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

delta = B**2 - 4*A*C

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    x1 = -B / (2 * A)
    print(f"Existe uma única raiz real: x1 = {x1}")
else:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f"Existem duas raízes reais:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
