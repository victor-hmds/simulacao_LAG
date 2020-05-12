# CÁLCULO DA VELOCIDADE DA MOLÉCULA DE H2 NO REFERENCIAL DO CENTRO DE MASSA ANTES DA COLISÃO

import math as m
import massa_reduzida as mr
import velocidade_eletron as ve
import velocidade_molecula_cartesiano as vm
import velocidade_relativa_AC as vr

# Importando valores de massa da molécula, do elétron e a massa reduzida

mass_eletron = mr.mass_eletron
mass_mol = mr.mass_mol
mass_red = mr.mass_red

# Importando velocidades do elétron em coordenadas cartesianas

Vx_eletron = ve.calculo_Vx_eletron()
print (Vx_eletron)
Vy_eletron = ve.calculo_Vy_eletron()
print (Vy_eletron)
Vz_eletron = ve.calculo_Vz_eletron()
print (Vz_eletron)

# Importando velocidades da molécula em coordenadas cartesianas

Vx_mol = vm.calculo_Vx_mol()
print (Vx_mol)
Vy_mol = vm.calculo_Vy_mol()
print (Vy_mol)
Vz_mol = vm.calculo_Vz_mol()
print (Vz_mol)

# Importando velocidade relativa antes da colisão

Mod_g = vr.calculo_vel_rel()
print (Mod_g)

# Cálculo da velocidade da molécula de H2 no referencial do centro de massa

#def calculo_u_linha():
#    M = ((mass_eletron)/(mass_eletron + mass_mol)) * m.sqrt((2/mass_red)*(((mass_red * (Mod_g ** 2))/2) - delta_E))
# Falta o programa de delta E, 