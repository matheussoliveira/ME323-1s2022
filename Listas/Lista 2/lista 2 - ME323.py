import sys
import math
from decimal import Decimal
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import scipy.integrate as integrate
import math

sys.setrecursionlimit(5000)

def prob(n, x, p):
    if (x == 0):
        return float(1 - p)**n

    return prob(n - 1, x - 1, p) * float(p) * float(n) / float(x)

class PDF():
    def __init__(self,mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):
        self.mean = sum(self.data) // len(self.data)
        return self.mean

    def calculate_stdev(self,sample=True):
        if sample:
            n = len(self.data)-1
        else:
            n = len(self.data)
        mean = self.mean
        sigma = 0
        for el in self.data:
            sigma += (el - mean)**2
        sigma = math.sqrt(sigma / n)
        self.stdev = sigma
        return self.stdev

    def pdf(self, x):
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)

probabilidades = []
valores_x = []

n = 1500+100*8
p = 0.5+(6/50)

for i in range(n):
  valores_x.append(i+1)
  probabilidades.append(prob(n, i+1, p))

fig, ax = plt.subplots(1, 1)

fdp = []

for prop in probabilidades:
    fdp.append(norm.pdf(prop))

esperanca = 0

for index in range(0, n):
    esperanca += float(probabilidades[index]) * float(fdp[index])

variancia = 0

for index in range(0, n):
    variancia += (probabilidades[index] - esperanca) ** 2

desvioPadrao =  math.sqrt(variancia)

print("Esperança = ", esperanca)
print("Variancia = ", variancia)
print("Desvio padrão = ",desvioPadrao)

y = [esperanca-desvioPadrao, esperanca+desvioPadrao]
x = [0, 2300]

plt.plot(valores_x, fdp)
# plt.text(0,esperanca,'E(x)')
plt.annotate("E(x)", (1150, esperanca))
plt.fill_between(x, y, color="none", hatch="|", edgeColor="g")
plt.show()