"""
Eric González, Izan Fernandez
11/10/2023
M03 UF1 A2
Descripció: Exercici 3

"""
#Escriu un programa que llegeixi 5 enters. El primer i el segon creen un rang, el tercer i el quart creen un altre rang. Mostra True si el cinquè valor, està comprès dins els dos rangs, si no False

numero1 = int(input("Escriu un numero: "))
numero2 = int(input("Escriu un numero: "))
numero3 = int(input("Escriu un numero: "))
numero4 = int(input("Escriu un numero: "))
numero5 = int(input("Escriu un numero: "))

rang1 = range(numero1, numero2)
rang2 = range(numero3, numero4)
if numero5 in rang1 and numero5 in rang2:
    print("true")
else:
    print("false")
