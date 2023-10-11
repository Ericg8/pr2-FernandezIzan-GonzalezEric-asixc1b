"""
Eric González, Izan Fernandez
11/10/2023
M03 UF1 A2
Descripció: Exercici 1

"""
#Demanar el diàmetre d'una pizza rodona i imprimeix la seva superfície. Pots usar Math.PI per escriure el valor de Pi.

import math

diametre = int(input("Escriu el diametre de la pizza: "))
radi = diametre / 2
Area = math.pi * (radi**2)
print("La superficie de la pizza es de",Area)