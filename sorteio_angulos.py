# SORTEIO DOS ÂNGULOS EM COORDENADAS ESFÉRICAS

import math as m
import random

# Sorteio do ângulo theta em radianos [0, pi]

def sorteio_theta():
    x = random.random()
    CosTheta = 2 * x - 1                                                       # O sorteio deve ser feito para o cosseno de theta para garantir a homogeneidade dos pontos sorteados
    Theta = m.acos(CosTheta)
    #print (Theta)
    return Theta

# Ângulo em graus
#theta = (180 * Theta)/m.pi
#print (theta)

# Sorteio do ângulo Phi em radianos [0, 2*pi]

def sorteio_phi():
    Phi = random.random() * 2.0 * m.pi
    #print (Phi)
    return Phi

# Ângulo em graus
#phi = (180 * Phi)/m.pi
#print (phi)