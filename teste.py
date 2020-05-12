from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
import random
 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def sphere(r):
    n = 0
    while (n<=100):
        n += 1
        x = random.random()
        CosTheta = 2 * x - 1
        theta = math.acos(CosTheta)
        phi = random.random() * 2.0 * math.pi
        #theta = np.linspace(0, np.pi, 100)
        #phi = np.linspace(0, 2 * np.pi, 100)        
        x = r * np.outer(np.cos(phi), np.sin(theta))
        y = r * np.outer(np.sin(phi), np.sin(theta))
        z = r * np.outer(np.ones(np.size(phi)), np.cos(theta))
    return x,y,z
 
x,y,z = sphere(2)
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b')
 
plt.show()