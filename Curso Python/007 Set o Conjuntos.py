
import os
os.system("clear")

# "Set" o "Conjuntos"
# Es uno de los 4 tipos para almacenar colecciones de DATOS en Phyton, 
''' Es un Conjunto Desordenado, inmutable y no indexada
    Sus Elementos prestablecidos, no se pueden modificar, 
    pero se pueden eliminar elementos y agregar nuevos elementos'''
# Se escriben con {"llaves"}
# No permite elementos duplicados
# Son <class set>


unSet = {"apple", "lemon", "cherry", 'green','blue'}
print(unSet)

print("asi sabemos su longitud: ", len(unSet))
print(type(unSet))
print(unSet)
print("----------")

# Acceder a sus elementos (no es posible hacerlo mediante  "indices" o "claves")
# Se una un FOR o preguntando mediante un IN el elemento buscado

for x in unSet:
    print("estos son los valores: ", x)

if "banana" in unSet:
    print("Yeah, banana is in this \"set\":")
else:
    print("\"banana\" there isnt in this set")
print("----------")

# Para agregar un elemento a un conjunto se usa .ADD
unSet.add("melon")
print(unSet)
print("----------")

# Para unir dos SET, uso .UPDATE. 
# Tambien sirve para unir a un SET, una lista, diccionario o tuple
otroSet = {'dog', 'cat', 'wolf'}
unSet.update(otroSet)
print(unSet)
print("----------")

# Para borrar un elemento uso .REMOVE o .DISCARD
unSet.remove("wolf") #.remove tira error el codigo, cuando el elemento no existe en el SET
unSet.discard("dog")
unSet.discard("cow") # .discard no tira error
print(unSet)
print("----------")

# Con este metodo se crea un nuevo SET apartir de la union de dos SET  .union
# Pero elimina los elementos duplicados
set4 = {'cat', 'dog','car', 'blue', 'green'}
set3 = unSet.union(set4)
print(set3)
print("----------")

# Con este metodo solo mantenemos los elementos duplicados 
x = {80,90,100,50,45,80}
b = {100,45,90,89,35,21}
z = x.difference(b)
print('con metodo \"difference\", guardamos los elementos que son diferentes:', z)
x.intersection_update(b)
print('guarde solo duplicados: ', x) 
print("----------")







