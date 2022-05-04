import os
os.system("clear")

#Uso de FOR.


otraVariable = "hola"
nuevaCadena = ""



acumulador = ""

for letra in otraVariable:
    if letra == "o":
        letra = "oo"
    if letra == "l":
        letra = "lll"
    if letra == "a":
        letra = "aaaa"
    acumulador += letra

print (acumulador)