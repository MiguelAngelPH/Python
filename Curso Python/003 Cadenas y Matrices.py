import os
os.system("clear")

# En Python una cadena es una MATRIZ y se puede acceder a su lectura asi
a = "Bananas"
print("esta es la cadena: ", a[1])

print("-------------")

print("utilizando un FOR:")
for x in a:
    print(x)

print("-------------")
print("Utilizo LEN() para saber la longitud")

print(len(a))
print("-------------")

#para saber si un texto esta dentro de una cadena uso IN
y = " The best things in life are free!"
print("life esta en la frase?", "life" in y)
print("-------------")

if "free" in y:
    print("'free' esta presente en la frase" )
print("-------------")

# Usando un NOT
if "expensive" not in y:
    print("'expensive', no esta en la frase")
print("-------------")
#imprimiendo solo una parte de la cadena, con un rango determinado
print(y[2:14])
print(y[:9])
print(y[9:])
print("-------------")

#para iniciar de adelante, hacia atras
print(y[-14:-1])
print("-------------")

#Convertir una cadena en Mayusculas o minusculas
print(y.upper())
z = "DOGS"
print(z.lower())
print("-------------")

#Quitar espacios en blanco al inicio
print(y)
print(y. strip())
print("-------------")

#Divide la cadena segun lo especifiquemos entre comillas, como concatenar
print(y)
print(y.split("s"))
print("-------------")

#Concatenando usando "espacios"
c = a + y
print(c)
c= a + "       " + y[-6:]
print(c)
print("-------------")

#Para poder imprimir una cadena combinando STRING & INT, usamos "format()"
age = 32
txt = "My name is Miguel, and I am {}"
print(txt.format(age))
print("-------------")

#Podemos tener varias variables numericas e insertarlas en una variable texto, sin importar el lugar

Cantidad = 5
Precio = 30.8
producto_Num = 103


myorder = " llevo {} piezas del producto : {}, por un precio de $ {} "
print(myorder.format(Cantidad,Precio,producto_Num))
print("--")

#podemos usar indices
stock = "En bodega quedan {0}, del producto {2}"
print(stock.format(Cantidad,Precio,producto_Num))
print("-------------")

#Para poder poner COMILLAS en una cadena se utiliza "\"

txt2 = "Los ravioles de \"Maga\" estaban \"crudones\""
print(txt2)


print("-----\"FIN\"--------")



