import time
import sys

sys.setrecursionlimit(2000)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

valores = [10, 100, 500, 1000]

for n in valores:

    inicio = time.time()

    resultado = fatorial(n)

    fim = time.time()

    tempo = fim - inicio

    print(f"n = {n}")
    print(f"Tempo de execucao: {tempo:.6f} segundos")
    print("-----------------------------")