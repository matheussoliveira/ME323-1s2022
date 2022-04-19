import sys
from decimal import Decimal
import matplotlib.pyplot as plt
import random
import decimal

sys.setrecursionlimit(2000)

def prob(n, x, p):
    if (x == 0):
        return Decimal(1 - p)**n

    return prob(n - 1, x - 1, p) * Decimal(p) * Decimal(n) / Decimal(x)

p = 1/50063860

print(4160*p/100)


# n = 100
# xValues = []
# randomNumbers = []

# for index in range(1, n+1):
#     xValues.append(index)
#     random = decimal.Decimal(random.randrange(90, 110))/100
#     randomNumbers.append(random)

# p_argentina = 0.49
# p_peru = 0.70
# p_brasil = 0.36

# for i in range(n):
#   valores_x.append(i+1)
#   probabilidades_argentina.append(prob(n, i+1, p_argentina))

# for i in range(n):
#   probabilidades_peru.append(prob(n, i+1, p_peru))

# for i in range(n):
#   probabilidades_brasil.append(prob(n, i+1, p_brasil))

# plt.title("Argentina")
# plt.ylabel("P{X=x}")
# plt.xlabel("x")
# plt.plot(valores_x, probabilidades_argentina)
# plt.show()


# plt.title("Peru")
# plt.ylabel("P{X=x}")
# plt.xlabel("x")
# plt.plot(valores_x, probabilidades_peru)
# plt.show()

# plt.title("Brasil")
# plt.ylabel("P{X=x}")
# plt.xlabel("x")
# plt.plot(valores_x, probabilidades_brasil)
# plt.show()