# SORTEIOS DA SIMULAÇÃO

#_____________________________________________________________________________________________________________________________

# Bibliotecas

import scipy.stats as stats
import math
import random
import numpy as np
import matplotlib.pyplot as plt

#_____________________________________________________________________________________________________________________________

# SORTEIO DOS ÂNGULOS EM COORDENADAS ESFÉRICAS

# O sorteio dos ângulos em coordenadas esféricas é utilizada em diversos momentos no código principal:
# 1 - Sortear os ângulos iniciais da molécula de hidrogênio para definir a velocidade da molécula.
# 2 - Sortear os ângulos de cada fragmento após a dissociação ocasionada pela interação elétron - molécula.
# 3 - E também no detector...

# SORTEIO DO ÂNGULO THETA EM RADIANOS [0, pi]

class Sorteio_angulo():
    def sorteio_theta():
        x = random.random()
        CosTheta = 2 * x - 1
        
# O sorteio deve ser feito para o cosseno de theta para garantir a homogeneidade dos pontos sorteados quando disposto espacialmente, para maiores informações acesse o arquivo angulos.py
        
        Theta = math.acos(CosTheta)
        return Theta
    #print (sorteio_theta())

# ÂNGULOS THETA EM GRAUS

    theta = (180 * sorteio_theta())/math.pi
    #print (theta)

# SORTEIO DO ÂNGULO PHI EM RADIANOS [0, 2*pi]

    def sorteio_phi():
        Phi = random.random() * 2.0 * math.pi
        return Phi
    #print (sorteio_phi())

# ÂNGULO PHI EM GRAUS

    phi = (180 * sorteio_phi())/math.pi
    #print (phi)
    

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
# Compara os valores determinados da média e desvio padrão com os valores calculados da distribuição gerada

abs (mu - np.mean(g)) < 0.01 
abs (sigma - np.std(g, ddof=1)) < 0.01

# SORTEIO DE UM VALOR DO ARRAY CRIADO PELA FUNÇÃO g
# Deve haver uma comparação do valor da distância internuclear sorteada com os valores permitidos segundo o Princípio de Franck-Condom

valor_escolhido = random.choice(g)
print ('O valor sorteado foi:', valor_escolhido)

if (0.5916 < valor_escolhido < 0.8916):
    valor_escolhido_FC1 = valor_escolhido
    print ("Sorteio de primeira:", valor_escolhido_FC1)
    
else:
    valor_escolhido_FC2 = random.choice(g)
    print ("Sorteio realizado novamente:", valor_escolhido_FC2)

# CONFIGURAÇÃO DO HISTOGRAMA SEGUNDO A DISTRIBUIÇÃO GAUSSIANA (somente utilizado para compreensão do programa, na simulação não é necessária)

count, bins, ignored = plt.hist(g, 40, density=True, histtype = 'stepfilled', facecolor = 'green')
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='red')
plt.title('Distribuição Gaussiana')                                            # Definindo título
plt.xlabel('Distância Internuclear (Angstron)')                                           # Definindo nome do eixo X
plt.ylabel('Densidade de Probabilidade')                                       # Definindo nome do eixo Y
plt.savefig('Distribuição Gaussiana.png')                                      # Salvando imagem
plt.show()


#_____________________________________________________________________________________________________________________________


# SORTEIO SEGUNDO DISTRIBUIÇÃO DE MAXWELL-BOLTZMANN

# Esse sorteio é utilizado para definir o módulo velocidade da molécula de H2 antes da interação com o feixe de elétrons.

# CONDIÇÕES RELEVANTES DA MOLÉCULA

k = 1.38064852 * (10 ** (-23))                                                 # Constante de Boltzmann
#print('Constante de Boltzmann:', k)
M = 2 * 1.6735575 * (10 ** (-27))                                              # Massa da molécula de H2 em quilograma
#print('Massa da molécula de H2:', M)
T = 273.15 + 25                                                                # Temperatura em kelvin
#print('Temperatura:', T)
a = math.sqrt((k * T)/M)                                                       # Fator de escala (scale) responsável pela largura da distribuição
#print('Fator de escala:', a)

# SORTEIO DE VALORES SEGUNDO A DISTRIBUIÇÃO DE MAXWELL-BOLTZMANN E CÁLCULO DO VALOR MÉDIO

maxwell = stats.maxwell
m = maxwell.rvs(loc=0, scale=a, size=10000)
#print (m)

# Comando responsável pelo sorteio (loc define a origem, scale tem relação com a massa e temperatura e size a dimensão do array), utiliza também o método de Monte Carlo

def velocidade_mais_provavel():
    media = maxwell.mean(loc=0, scale=a)
    return media
#print ('O módulo da velocidade mais provável:', velocidade_mais_provavel())

# AJUSTE SEGUNDO A DISTRIBUIÇÃO DE MAXWELL-BOLTZMANN DENTRO DOS VALORES SORTEADOS (relevante somente ao histograma para compreensão do programa)

params = maxwell.fit(m, floc=0)
#print (params)

# SORTEIO DE UM VALOR DO ARRAY CRIADO PELA FUNÇÃO m

def maxwell_escolhido():
    valor_escolhido = random.choice(m)
    return valor_escolhido
#print ('O valor sorteado foi:', maxwell_escolhido())

# CONFIGURAÇÃO DO HISTOGRAMA SEGUNDO A DISTRIBUIÇÃO DE MAXWELL-BOLTZMANN (somente utilizado para compreensão do programa, na simulação não é necessária)

count, bins, ignored = plt.hist(m, 40, density=True, histtype = 'stepfilled', facecolor = 'green')
x = np.linspace(0, 5500, 100)
plt.plot(x, maxwell.pdf(x, *params), linewidth=2, color='red')
plt.title('Distribuição de Maxwell-Boltzmann')                                 # Definindo título
plt.xlabel('Velocidade (m/s)')                                                       # Definindo nome do eixo X
plt.ylabel('Densidade de Probabilidade')                                       # Definindo nome do eixo Y
plt.savefig('Distribuição Maxwell-Boltzmann.png')                              # Salvando imagem
plt.show()