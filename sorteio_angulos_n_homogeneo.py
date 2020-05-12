# SORTEIO DOS ÂNGULOS EM COORDENADAS ESFÉRICAS DE FORMA NÃO HOMOGÊNEA

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import random

# Comandos para gerar imagem

fig = plt.figure()
ax = fig.add_subplot (111, projection= '3d')

r = 1.0
x = random.random()
CosTheta = 2 * x - 1
theta = math.acos(CosTheta)
phi = random.random() * 2.0 * math.pi

X = []
Y = []
Z = []

X = r*np.cos(phi)*np.sin(theta)
Y = r*np.sin(phi)*np.sin(theta)
Z = r*np.cos(theta)

ax.plot_wireframe(X, Y, Z)
plt.show()

# Sorteio do ângulo theta em radianos [0, pi]

#Theta = random.random() * math.pi
#print (Theta)

# Ângulo em graus
#theta = (180 * Theta)/math.pi
#print (theta)

# Sorteio do ângulo Phi em radianos [0, 2*pi]

#Phi = random.random() * 2.0 * math.pi
#print (Phi)

# Ângulo em graus
#phi = (180 * Phi)/math.pi
#print (phi)
    
