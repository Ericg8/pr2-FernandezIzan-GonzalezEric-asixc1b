"""
Eric González, Izan Fernandez
11/10/2023
M03 UF1 A1
Descripció: Exercici 2

"""
#Per poder fer un estudi de la ventilació d'una aula necessitem poder calcular la quantitat d'aire que hi cap en una habitació. Llegeix les 3 dimensions de l'aula i mostra per pantalla quin volum té.

longitud = float(input("Ingresa la longitud en metres: "))
ample = float(input("Ingresa la amplitud en metres: "))
Altura = float(input("Ingresa l'altura en metres: "))

calcul = longitud * ample * Altura

print("El volum de l'aula és:",calcul, "m3")
