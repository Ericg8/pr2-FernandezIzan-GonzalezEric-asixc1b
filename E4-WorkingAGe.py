"""
Eric González, Izan Fernandez
18/10/2023
M03 UF1 A2
Descripció: Exercici 4

"""
#Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar, l'edat mínima per treballar legalment és 16 i suposarem l'edat màxima als 65.

edat = int(input("Quina edat tens? "))
if 16 <= edat <= 65:
    print("Si tens edat per treballar")
else:
    print("No tens edat per treballar")
