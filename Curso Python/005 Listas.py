import os
os.system("clear")

#Las listas se crean usando corchetes
#Si se agregan nuevos valores a la lista, estos quedan al final de la lista
#Los elementos pueden tener el mismo valor
#Elementos pueden ser cualquier tipo de datos y combinados
myList = ["apple","banana", "orange", "apple", True, 0, 3.1]
print("valores de la lista:", len(myList))
print("esta es la lista: ", myList)
print(type(myList[4]))
print("-----------")

#Accesar a los elementos por indices
print("solo el 3:", myList[3])
print("del 3 al 6:", myList[3:6])
print("hasta el 5to:", myList[:5])
print("del atras hacia adelante", myList[-7:-5])
print("-----------")

#Con "in" sabemos si un articulo existe en la Lista
if "orange" in myList:
    print("\"Orange\" esta en la lista")
print("-----------")

#Asi cambiamos el valor de un elemento de la lista
myList[4] = "PERRO"

print("modificacion", myList[4].lower())
myList[0:2] = 1, 2, 3
print("se cambiaron 2 valores y se agrego uno:", myList)
print("-----------")

#Podemos agregar un nuevo elemento a la lista con ".insert" en el indice que queramos
myList.insert(5, "Melon")
print("nuevo elemento", myList)
print("-----------")

#Podemos agregar un elemento al final
myList.append("ASTRO")
print("elemtno al final", myList)
print("-----------")

#Unir dos Listas
#El extend puede unir Listas, con cualquier otro elemento iterable, como un tuple, diccionario, conjuntos, etc
numList = [ 0, 1, 2, 3]
myList.extend(numList)
print("listas unidas: ", myList)
print("-----------")

#Remover Elementos de una lista, con "REMOVE" y con "POP"
myList.remove("ASTRO")
print("sin \"ASTRO\":", myList)

myList.pop(3)
print("sin el indice \"3\": ", myList) 
myList.pop() #remueve el ultimo indice
print("sin especificar: ", myList) 
print("-----------")

#Limpiamos la Lista con "CLEAR"
myList.clear()
print("lista limpiada", myList)
print("-----------")

#Usando un "FOR" para recorrer una lista
myList = ["perros", "gatos", "Monos", "Tortugas", "aguilas"]

for x in myList:
    print(x)

for i in range(len(myList)):
  print(myList[i])
print("-----------")

#Usando un While, para recorrer la lista
#se una la funcion ".len", que determina la longitud de la lista

i = 0 
while i < len(myList):
    print(myList[i])
    i = i + 1
print("-----------")

#Bucle corto para imprimir todos los elementos de la lista 
[print(x) for x in myList]
print("-----------")

#Comprension de Listas: Hacemos una Lista nueva apartir de una existente, 
#Agregando todos los valores que nosotros queramos, marcandolo entre comillas
#podemos especificar que elementos no queremos
newList = [x for x in myList if "os" in x ]
print(newList)
secondList = [x for x in myList if x != "perros" ] 
print(secondList)

sustituyoList = [x if x != "tortugas" else "girafas" for x in secondList]#sustituyo un elemento por otro
print(sustituyoList)
print("-----------")

#Para ordenar alfanumericamente una "lista" usamos el metodo SORT()
myList.sort()
print(myList)
ordenList = [ 7, 90, 55, 55, 4, 3, 0, 1]
ordenList.sort()
print(ordenList)
ordenList.sort(reverse = True) #Para ordenar descendente
print(ordenList)
print("-----------")

#Para Ordenar usando una FUNCION, usando key = function
def myfunc(n):
    return abs(n - 90)

ordenList.sort(key = myfunc)
print(ordenList)
print("-----------")

#cuando ordenamos, ordena primero las mayusculas, si queremos evitar esto, podemos usar una funcion con .lower
myList.sort()
print(myList)
myList.sort( key = str.lower)
print(myList)
print("-----------")

#Con este metodo ".reverse" invertimos la lista, independientemente del orden
print(myList)
myList.reverse()
print(myList)
print("-----------")

#Para copiar una lista, se usa el metodo ".copy"
copyList = myList.copy()
print(copyList)
print("-----------")

#Podemos concatenar 2 listas usando el "+"
list3 = ordenList + myList
print(list3)
print("-----------")

#Con este metodo, sabemos que posicion ocupa un elemento ".index()"
indice = list3.index("Tortugas")
print("\"Tortugas\" ocupa el indice numero:", indice)
print("-----------")

#Con este metodo ".count()" sabemos cuantos elemento hay de esa especie especificada
cantidad = list3.count(55)
print("esta es la cantidad de elementos con el numero \"55\" en nuestra Lista:", cantidad)
print("-----------")




































