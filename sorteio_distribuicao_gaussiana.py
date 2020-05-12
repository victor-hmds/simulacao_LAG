# SORTEIO SEGUNDO DISTRIBUIÇÃO GAUSSIANA

import scipy.stats as stats
import random
import numpy as np
import matplotlib.pyplot as plt

# Sorteio segundo a distribuição gaussiana e cálculo do valor médio

mu = 0.7416                                                                    # Média
sigma = 0.05                                                                   # Desvio Padrão
s = np.random.normal (mu, sigma, 10000)

def calculo_dist_internuclear():
    media = stats.gmean(s, axis=0)
    return media
print ('Raio internuclear mais provável:', calculo_dist_internuclear())

# Função de erro

abs (mu - np.mean(s)) < 0.01 
abs (sigma - np.std(s, ddof=1)) < 0.01

# Sorteio um valor do array criado pela função s

def gauss_escolhido():
    valor_escolhido = random.choice(s)                     
    return valor_escolhido
print ('O valor sorteado foi:', gauss_escolhido())

# Configuração do histograma segundo a distribuição gaussiana

count, bins, ignored = plt.hist(s, 40, density=True, histtype = 'stepfilled', facecolor = 'green')
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='red')
plt.savefig('Distribuição Gaussiana.png')                                      # Salvando imagem
plt.title('Distribuição Gaussiana')                                            # Definindo título
plt.xlabel('Raio Internuclear')                                                # Definindo nome do eixo X
plt.ylabel('Densidade de Probabilidade')                                       # Definindo nome do eixo Y
plt.show()
