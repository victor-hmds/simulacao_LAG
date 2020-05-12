# CÁLCULO DA VELOCIDADE RELATIVA ANTES DA COLISÃO

import math
import velocidade_eletron as ve
import velocidade_molecula_cartesiano as vm

# Importando velocidades do elétron em coordenadas cartesianas

Vx_eletron = ve.calculo_Vx_eletron()
#print (Vx_eletron)
Vy_eletron = ve.calculo_Vy_eletron()
#print (Vy_eletron)
Vz_eletron = ve.calculo_Vz_eletron()
#print (Vz_eletron)

# Importando velocidades da molécula em coordenadas cartesianas

Vx_mol = vm.calculo_Vx_mol()
#print (Vx_mol)
Vy_mol = vm.calculo_Vy_mol()
#print (Vy_mol)
Vz_mol = vm.calculo_Vz_mol()
#print (Vz_mol)

# Cálculo da velocidade relativa antes da colisão
def calculo_vel_rel():
    Mod_g = math.sqrt(((Vx_mol - Vx_eletron) ** 2) + ((Vy_mol - Vy_eletron) ** 2) + ((Vz_mol - Vz_eletron) ** 2))
#   print (Mod_g)
    return Mod_g