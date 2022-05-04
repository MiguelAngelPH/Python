import os
os.system("clear")


x = 5
y = "hello, world"

#this is a comment.

"""multiples
lineas de comentario
"""

print(y, ". Esta es x: ", x)


if 5 > 2:
    print("five is greater than two!")

print("----------")
#tipos de Variables.

print("VARIABLES")
#Especificando un tipo de variable

x = str(3)      # x sera un 3 en letra
y = int(3)      # y sera una numero 3 entero
z = float(3.1)  # z sera un float

print(y + z, ", x")  # aca imprime a "x" como un string y le puedo anadir una coma

# asi podemos obtener el tipo de una variable

print("Z es del tipo", type(z))
print("X es del tipo", type(x))
print("Y es del tipo", type(y))

print("----------")
#las variables se distinguen entre minusculas y MAYUSCULAS
print("las variables se distinguen entre minusculas y MAYUSCULAS: ")
a = "lalo"
A = 3
print("a = ",a,".  A = ",A)


print("----------")
# SE PUEDEN ASIGNAR VARIABLES EN UNA SOLA LINEA

b, c, d = 10, 30, "Si"

print("asignando variables en una sola linea: ", b,c,d)

print("----------")
# UnPack una "lista" en distintas variables
print("UnPack una lista en distintas variables")

myFruits = ("orange", "banana", "apple")
a, b , c = myFruits
print(a, b , c)

print("----------")
#sumando cadenas o Variables cons signo +
print("sumando cadenas o Variables")
z = a + b
print(z)
print( a + b + c + ", sumando todo solo usanso signo + ")
# no se pueden sumar strings + int
# en int el + se convierte en operador aritmetico
x = 25
y = 1.8
w = x + y
print("la suma de x + y es: ", w, type(w))


print("----------")
#FUNCIONES: variables globales fuera de las funciones

x = "awesome"

def myfunc():
    print("python is " + x)
myfunc()


def myfunc():
  x = "fantastic"
  print("Python is " + x)
  print("se cambio la variable x solo a la de la funcion, despues retoma el valor de x global")

myfunc()

print("Python is " + x)


def myfunc():
    global x
    x = "fantastic"
myfunc()

print( " aca estamos fuera de la funcion y x cambio a fantastic, porque se declaro global dentro de la funcion")
print("python is: ", x)











