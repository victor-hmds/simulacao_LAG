# SORTEIO DA VELOCIDADE DA MOLÃ‰CULA EM COORDENADAS CARTESIANAS em m/s

import math
import sorteio_distribuicao_maxwell_boltzmann as smb
import sorteio_angulos as sa

# Importando módulo da velocidade sorteada segundo a distribuição de Maxwell-Boltzmann e ângulos sorteados

vel_mb = smb.maxwell_escolhido()
#print (vel_mb)
theta = sa.sorteio_theta()
#print (theta)
phi = sa.sorteio_phi()
#print (phi)

# Cálculos das componentes cartesianas da velocidade da molécula

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