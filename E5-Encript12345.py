"""
Eric González, Izan Fernandez
11/10/2023
M03 UF1 A2
Descripció: Exercici 5

"""
#Demana una paraula per teclat i mostrar-la per pantalla, canviar les vocals per als numèrics 1, 2, 3, 4 o 5. Tenint en compte, que la lletra a i A és l'1, consecutivament fins a la lletra u i U que és el 5.
paraula = str(input ("Introduiex una paraula:"))

paraula1 = paraula.replace("A","1")
paraula2 = paraula1.replace("E","2")
paraula3 = paraula2.replace("I","3")
paraula4 = paraula3.replace("O","4")
paraula5 = paraula4.replace("U","5")

paraula6 = paraula5.replace("a","1")
paraula7 = paraula6.replace("e","2")
paraula8 = paraula7.replace("i","3")
paraula9 = paraula8.replace("o","4")
paraula10 = paraula9.replace("u","5")
print(paraula10)