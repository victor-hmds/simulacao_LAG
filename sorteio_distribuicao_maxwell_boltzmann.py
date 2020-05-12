# SORTEIO SEGUNDO DISTRIBUIÇÃO DE MAXWELL-BOLTZMANN

import scipy.stats as stats
import math as m
import random
import numpy as np
import matplotlib.pyplot as plt

# Condições iniciais

k = 1.38064852 * (10 ** (-23))                                                 # Constante de Boltzmann
#print('Constante de Boltzmann:', k)
M = 2 * 1.6735575 * (10 ** (-27))                                              # Massa da molécula de H2 em quilograma
#print('Massa da molécula de H2:', M)
T = 273.15 + 25                                                                # Temperatura em kelvin
#print('Temperatura:', T)
a = m.sqrt((k * T)/M)
#print('Fator de escala:', a)

# Sorteio de valores segundo a distribuição de Maxwell-Boltzmann e cálculo do valor médio

maxwell = stats.maxwell
r = maxwell.rvs(loc=0, scale=a, size=10000)                                    # Comando responsável pelo sorteio (loc define a origem e scale tem relação com a massa e temperatura) MÉTODO DE MONTE CARLO
#print (r)

def velocidade_mais_provavel():
    media = maxwell.mean(loc=0, scale=a)
    return media
print ('Velocidade mais provável:', velocidade_mais_provavel())

# Ajuste segundo a distribuição de Maxwell-Boltzmann dentro dos valores sorteados

params = maxwell.fit(r, floc=0)
#print (params)

# Sorteio de um valor do array r

def maxwell_escolhido():
    valor_escolhido = random.choice(r)
    return valor_escolhido
print ('O valor escolhido foi:', maxwell_escolhido())

# Configuração do histograma

count, bins, ignored = plt.hist(r, 40, density=True, histtype = 'stepfilled', facecolor = 'green')
x = np.linspace(0, 6000, 100)
plt.plot(x, maxwell.pdf(x, *params), linewidth=2, color='red')
plt.savefig('Distribuição Maxwell-Boltzmann.png')                              # Salvando imagem
plt.title('Distribuição de Maxwell-Boltzmann')                                 # Definindo título
plt.xlabel('Velocidade')                                                       # Definindo nome do eixo X
plt.ylabel('Densidade de Probabilidade')                                       # Definindo nome do eixo Y
plt.show()