import os
os.system("clear")

# Revision tipos de DATOS (VARIABLES).
# Acceso a subindices.

var1 = []      # lista
var2 = "hola"  # string
var3 = 3       # entero
var4 = 7.5     # punto flotante
var5 = True    #logico

print("var1 es:", type(var1))
print("var2 es:", type(var2))
print("var3 es:", type(var3))
print("var4 es:", type(var4))
print("var5 es:", type(var5))

print("-------")

if isinstance(var1, str):
    print("var1 es: string")
else:
    if isinstance(var1, list):
        print("var1 es una lista, bravvooo")

print("-------")

var1.append("primer dato")
var1.append("perros dato")
var1.append([5, 7])

print("Acceso subindice",var1[2][1])

# que largo tendrá mi lista var1?
print("la lista var1 contiene:", len(var1), "elementos")
print(var1)

if isinstance(var1, list):
    if len(var1)==2:
        print("aahhhhh, el largo de la lista es de dos elementos.")

print (len(var1))
