# DISTRIBUIÇÃO DA ENERGIA CINÉTICA APÓS EXCITAÇÃO DA MOLÉCULA

#_____________________________________________________________________________________________________________________________

# Bibliotecas

import scipy.stats as stats
import math
import random
import numpy as np
import matplotlib.pyplot as plt

#_____________________________________________________________________________________________________________________________

# SORTEIO SEGUNDO DISTRIBUIÇÃO GAUSSIANA

# Esse sorteio é utilizado na simulação para sorteio da distância internuclear para o cálculo de Delta E (vide tese de doutorado da Aline Medina), que servirá também para o código para exemplificar o método de reflexão para obtenção da energia cinética dos fragmentos.

# SORTEIO SEGUNDO A DISTRIBUIÇÃO GAUSSIANA E CÁLCULO DO VALOR MÉDIO
    
mu = 0.7416                                                                    # Média
sigma = 0.0876                                                                 # Desvio Padrão
g = np.random.normal (mu, sigma, 10000)

# Comando responsável pelo sorteio segundo a distribuição gaussiana, que é obtida por meio da biblioteca numpy do python, o método utilizado é por meio de Monte Carlo

def calculo_dist_internuclear():
    media = stats.gmean(g, axis=0)
    return media
#print ('Distância internuclear mais provável:', calculo_dist_internuclear())

# FUNÇÃO ERRO

abs (mu - np.mean(g)) < 0.01 
abs (sigma - np.std(g, ddof=1)) < 0.01

# SORTEIO DE UM VALOR DO ARRAY CRIADO PELA FUNÇÃO g
# Deve haver uma comparação do valor da distância internuclear sorteada com os valores permitidos segundo o Princípio de Franck-Condom

# Definindo o valor máximo da função gaussiana para comparação temos,

valor_max_gauss = 4.55283                                                      # Valor máximo que a gaussiana pode tomar

prob_sorteada = random.uniform(0, 1)*valor_max_gauss                           # Probabilidade sorteada comparada ao valor máximo da gaussiana
print ('Probabilidade sorteada =', prob_sorteada)

r = random.choice(g)                                                           # Sorteio de distância internuclear
print ('Distância internuclear sorteada = ', r)

prob_gauss = valor_max_gauss*np.exp( - (r - mu)**2 / (2 * sigma**2))           # Probabilidade calculada no ponto r sorteado
print ('Probabilidade calculada de r =', prob_gauss)

while (prob_sorteada > prob_gauss):
    valor_max_gauss = 4.55283
    prob_sorteada = random.uniform(0, 1)*valor_max_gauss
    print ('Nova probabilidade sorteada = ', prob_sorteada)
    r = random.choice(g)
    print ('Nova distância internuclear sorteada = ', r)
    prob_gauss = valor_max_gauss*np.exp( - (r - mu)**2 / (2 * sigma**2))
    print ('Nova probabilidade calculada de r = ', prob_gauss)
    
# CURVAS DE POTENCIAL DE ESTADOS EXCITADOS

# 1 Piu peso 0,419
    
y1 = 2.5751 * np.exp(-r/0.3375) + 0.9879

# 2 Piu peso 0,379

y2 = 2.5479 * np.exp(-r/0.3476) + 1.0526

# 1 Sigma peso 0,203

y3 = 2.517 * np.exp(-r/0.335) + 0.957

# FALTA COLOCAR TODO O PROGRAMA EM UM LOOP DE 1000000 DE VEZES E TIRAR UM HISTOGRAMA DE CADA CURVA DE POTENCIAL

# CONFIGURAÇÃO DO HISTOGRAMA SEGUNDO A DISTRIBUIÇÃO GAUSSIANA (somente utilizado para compreensão do programa, na simulação não é necessária)

#count, bins, ignored = plt.hist(g, 40, density=True, histtype = 'stepfilled', facecolor = 'green')
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='red')
#plt.savefig('Distribuição Gaussiana.png')                                      # Salvando imagem
#plt.title('Distribuição Gaussiana')                                            # Definindo título
#plt.xlabel('Raio Internuclear')                                                # Definindo nome do eixo X
#plt.ylabel('Densidade de Probabilidade')                                       # Definindo nome do eixo Y
#plt.show()