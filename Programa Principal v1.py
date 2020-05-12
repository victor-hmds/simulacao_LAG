# PROGRAMA PRINCIPAL

# IMPORTAÇÃO DOS PROGRAMAS DE SORTEIO

import sorteio_angulos as sa
import sorteio_distribuicao_maxwell_boltzmann as smb
import sorteio_distribuicao_gaussiana as sg



theta = sa.sorteio_theta()
print (theta)

phi = sa.sorteio_phi()
print (phi)

raio_intern = sg.gauss_escolhido()
print (raio_intern)

veloc_mol = smb.maxwell_escolhido()
print (veloc_mol)