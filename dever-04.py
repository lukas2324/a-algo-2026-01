import math

def F(x):
    if x == 1:
        return 2
    else:
        return 2 * F(x - 1) + int(math.pow(x, 2))


x = int(input("Digite um valor para x: "))

if x < 1:
    print("Digite um número inteiro maior ou igual a 1.")
else:
    resultado = F(x)
    print(f"F({x}) = {resultado}")