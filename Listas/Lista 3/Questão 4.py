from tabulate import tabulate
import matplotlib.pyplot as plt


#------------------------------------------ item a -----------------------------------------------------------


values = []
yValues = []

for x1 in range(1, 6):
    for x2 in range(1, 6):
        for x3 in range(1, 6):
            y = x1+x2+x3
            yValues.append(y)
            values.append([x1, x2, x3, y])

table = [["x1", "x2", "x3", "y"]] + values
minY = min(yValues)
maxY = max(yValues)

xAsis = range(minY, maxY+1)
yProbabilities = []
yDictionary = dict.fromkeys(yValues)
possibleYValues = sorted(list(yDictionary))

for value in possibleYValues:
    probability = yValues.count(value)/len(yValues)
    yProbabilities.append(probability)

expectation = 0

for index in range(len(possibleYValues)):
    expectation += possibleYValues[index] * yProbabilities[index]

variance = 0

for index in range(len(possibleYValues)):
    variance += (possibleYValues[index] - expectation)**2 *yProbabilities[index]

print("Expectation:", expectation)
print("Variance:", variance)


# Uncomment to print table with x1, x2, x3 and y values.
# print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

plt.title("Função de distribuição de Y")
plt.xlabel("Valores de Y")
plt.ylabel("Probabilidade de Y")
plt.bar(xAsis, yProbabilities)
plt.show()


#------------------------------------------ item b -----------------------------------------------------------


values = []
yValues = []

for x1 in range(1, 6):
    for x2 in range(1, 6):
        for x3 in range(1, 6):
            if x1 + x2 < 6:
                y = x1+x2+x3
                yValues.append(y)
                values.append([x1, x2, x3, y])

table = [["x1", "x2", "x3", "y"]] + values
minY = min(yValues)
maxY = max(yValues)

xAsis = range(minY, maxY+1)
yProbabilities = []
yDictionary = dict.fromkeys(yValues)
possibleYValues = sorted(list(yDictionary))

for value in possibleYValues:
    probability = yValues.count(value)/len(yValues)
    yProbabilities.append(probability)

expectation = 0

for index in range(len(possibleYValues)):
    expectation += possibleYValues[index] * yProbabilities[index]

variance = 0

for index in range(len(possibleYValues)):
    variance += (possibleYValues[index] - expectation)**2 *yProbabilities[index]

print("Expectation:", expectation)
print("Variance:", variance)


# Uncomment to print table with x1, x2, x3 and y values.
# print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

plt.title("Função de distribuição condicional de Y")
plt.xlabel("Valores de Y")
plt.ylabel("Probabilidade de Y")
plt.bar(xAsis, yProbabilities)
plt.show()


#------------------------------------------ item c -----------------------------------------------------------


values = []
yValues = []

for x1 in range(1, 6):
    for x2 in range(1, 6):
        for x3 in range(1, 6):
            y = x1+x2+x3

            if y > 11:
                yValues.append(y)
                values.append([x1, x2, x3, y])

table = [["x1", "x2", "x3", "y"]] + values
minY = min(yValues)
maxY = max(yValues)

xAsis = range(minY, maxY+1)
yProbabilities = []
yDictionary = dict.fromkeys(yValues)
possibleYValues = sorted(list(yDictionary))

for value in possibleYValues:
    probability = yValues.count(value)/len(yValues)
    yProbabilities.append(probability)

expectation = 0

for index in range(len(possibleYValues)):
    expectation += possibleYValues[index] * yProbabilities[index]

variance = 0

for index in range(len(possibleYValues)):
    variance += (possibleYValues[index] - expectation)**2 *yProbabilities[index]

print("Expectation:", expectation)
print("Variance:", variance)


# Uncomment to print table with x1, x2, x3 and y values.
# print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

plt.title("Função de distribuição condicional de x1")
plt.xlabel("Valores de Y")
plt.ylabel("Probabilidade de Y")
plt.bar(xAsis, yProbabilities)
plt.show()