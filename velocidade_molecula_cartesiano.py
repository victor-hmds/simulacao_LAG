# SORTEIO DA VELOCIDADE DA MOLÉCULA EM COORDENADAS CARTESIANAS em m/s

import math
import sorteio_distribuicao_maxwell_boltzmann as smb
import sorteio_angulos as sa

# Importando m�dulo da velocidade sorteada segundo a distribui��o de Maxwell-Boltzmann e �ngulos sorteados

vel_mb = smb.maxwell_escolhido()
#print (vel_mb)
theta = sa.sorteio_theta()
#print (theta)
phi = sa.sorteio_phi()
#print (phi)

# C�lculos das componentes cartesianas da velocidade da mol�cula

def calculo_Vx_mol():
    Vx_mol = vel_mb * math.sin(theta) * math.cos(phi)
#   print (Vx_mol)
    return Vx_mol

def calculo_Vy_mol():
    Vy_mol = vel_mb * math.sin(theta) * math.sin(phi)
#   print (Vy_mol)
    return Vy_mol

def calculo_Vz_mol():
    Vz_mol = vel_mb * math.cos(theta)
#   print (Vz_mol)
    return Vz_mol