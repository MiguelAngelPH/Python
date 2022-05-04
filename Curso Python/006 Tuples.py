import os
os.system("clear")

#Una Tupla es una coleccion de Datos, ordenada e inmutable
#Los Datos estan ordenados y no se pueden modificar, pueden estar ducplicados
#Se escriben entre PARENTESIS
#Son: <class 'Tuple'>
#Pueden combinar el tipo de datos

firstTuple = ("jose", True, "lalo", "lulu", "dana", 4, 9.67)
print(firstTuple)
print("--------------")

#Para crear una Tupla de un solo elemento se pone "","" al final
secTuple = ("perros",)
print(secTuple)
print(type(firstTuple))
print("--------------")

#Para Cambiar un elemento de una TUPLA, se tiene que convertir a LISTA y despues regresar a TUPLA
print(firstTuple)
modLista = list(firstTuple)
modLista [3]= "Gatos"
newTuple = tuple(modLista)
print(newTuple)
print("--------------")

#Desempaquetar el TUPLE en variables
desempaquetado = (9, 0, 1)
(x, y , z ) = desempaquetado
print(x + y + z)
print("--------------")

#Cuando hay mas elementos en el TUPLE que de Variables
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
print("--------------")









