# CÁLCULO DA VELOCIDADE DO CENTRO DE MASSA ENTRE A MOLÉCULA DE H2 E O ELÉTRON

import velocidade_eletron as ve
import velocidade_molecula_cartesiano as vm
import massa_reduzida as mr

# Importando valores de massa da molécula e do elétron

mass_mol = mr.mass_mol
mass_eletron = mr.mass_eletron

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

# Cálculo da velocidade do centro de massa

Vcm_x = ((mass_mol/(mass_mol + mass_eletron))*(Vx_mol)) + ((mass_eletron/(mass_mol + mass_eletron))*(Vx_eletron))
print (Vcm_x)

Vcm_y = ((mass_mol/(mass_mol + mass_eletron))*(Vy_mol)) + ((mass_eletron/(mass_mol + mass_eletron))*(Vy_eletron))
print (Vcm_y)

Vcm_z = ((mass_mol/(mass_mol + mass_eletron))*(Vz_mol)) + ((mass_eletron/(mass_mol + mass_eletron))*(Vz_eletron))
print (Vcm_z)