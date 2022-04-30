from tabulate import tabulate
import matplotlib.pyplot as plt

values = []
xAsis = [x for x in range(1, 126)]
yAsis = []

for x1 in range(1, 6):
    for x2 in range(1, 6):
        for x3 in range(1, 6):
            y = x1+x2+x3
            yAsis.append(y)
            values.append([x1, x2, x3, y])

table = [["x1", "x2", "x3", "y"]] + values

# print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

plt.title("Função de distribuição de Y")
plt.xlabel("Eventos")
plt.ylabel("Valores de Y")
plt.plot(xAsis, yAsis)
plt.show()

