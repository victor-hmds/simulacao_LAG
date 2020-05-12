# CÁLCULO DA VELOCIDADE DO ELÉTRON EM m/s

# Por ser um feixe as velocidade nas outras direções (Vx e Vz) sem ser a direção de propagação (Vy) são nulas

import math as m

energia_eletron_ev = float(input ('Digite o valor da energia do feixe de elétron em eV: '))

energia_eletron = energia_eletron_ev * 1.602 * (10 ** (-19))                   # Energia do feixe de elétrons em Joule
#print (energia_eletron)

mass_eletron = 9.109 * (10 ** (-31))
#print (mass_eletron)

def calculo_Vy_eletron():
    Vy_eletron = m.sqrt((2 * energia_eletron)/mass_eletron)
#   print (Vy_eletron)
    return Vy_eletron

def calculo_Vx_eletron():
    Vx_eletron = float(0)
#   print (Vx_eletron)
    return Vx_eletron

def calculo_Vz_eletron():
    Vz_eletron = float(0)
#   print (Vz_eletron)
    return Vz_eletron