import random
import numpy as np

numeroTotalPartidas = 100 # mudar para 1 milhao
probAVencer = 0.50 # no exercicio 1-D, mudar para 0.49
numeroPartidasAtual = 0
numeroRodadasList = []

numeroVitoriasA = 0
numeroVitoriasB = 0

# numero de partidas
for partidaAtual in range(numeroTotalPartidas):
  fimRodada = False
  capitalA = 50
  capitalB = 20
  numeroRodada = 0

  # para cada partida, teremos varias rodadas ate achar um vencedor
  while fimRodada == False:
      numeroRodada += 1
      delta = -1
      valorAleatorio = random.uniform(0, 1)

      if valorAleatorio < probAVencer:
        delta=1

      capitalA = capitalA + delta
      capitalB = capitalB - delta

      if capitalA * capitalB > 0:
        continue

      if capitalA > 0:
        print('Partida ', partidaAtual, ' | ', 'A ganhou após ', numeroRodada, 'rodadas')
        numeroVitoriasA = numeroVitoriasA + 1
      else:
        print('Partida ', partidaAtual, ' | ', 'B ganhou após ', numeroRodada, 'rodadas')
        numeroVitoriasB = numeroVitoriasB + 1
      
      numeroRodadasList.append(numeroRodada)
      fimRodada = True

numeroRodadasList = np.array(numeroRodadasList)

print('----------------------------------------------')
print('Número total de partidas: ', numeroTotalPartidas)
print('Número vitorias A: ', numeroVitoriasA)
print('Número vitorias B: ', numeroVitoriasB)
print('Média numero rodadas: ', numeroRodadasList.mean())


probabilidades = []
dicionario = dict.fromkeys(numeroRodadasList) # Remove dados duplicados
rodadas = sorted(list(dicionario))

for value in rodadas:
    probability = np.count_nonzero(numeroRodadasList == value)/len(numeroRodadasList)
    probabilidades.append(probability)

esperanca = 0

for index in range(len(rodadas)):
    esperanca += rodadas[index] * probabilidades[index]

print("Esperança: ", esperanca)

variancia = 0

for index in range(len(rodadas)):
    variancia += (rodadas[index] - esperanca)**2 * probabilidades[index]


print("Variância: ", variancia)

