import os
from re import X
from turtle import clear
os.system("clear")

# Los Diccionarios de usan para guardar valores en Pares "CLAVE: VALOR"
# Es modificable, ordenado y no admite duplicados.
# Puede contecer una lista dentro
# Se escriben con {llaves}
# Son <class dict>

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964,
    "colors": ["red", "white","blue"]
}
print(thisdict)
print(type(thisdict))
print("------------")

# Asi accedo a uno de sus valores y conozco la cantidad de sus claves
print(thisdict['model'])
print(thisdict['colors'][1]) #asi accedo a la lista de una de las claves
print("Cantidad de Valores:", len(thisdict))
print("------------")

# Asi accedo a sus elementos
x = thisdict['model']
print(x)

y = thisdict.get('year')
print(y)

z = thisdict.keys() # Me devuelve las claves existentes 
print(z)
a = thisdict.values()
print(a) # Me devuelve los "Valores"
b = thisdict.items()
print(b) # Me devuelve en forma de Tupla
print("------------")

# Para comprobar si existe una clave
if "model" in thisdict:
  print("si, model es una de las claves")
print("------------")

# Para cambiar un valor
thisdict['year'] = 1998
print("diccionario cambiado:", thisdict)
thisdict.update({"model": "Ka"})
print("diccionario cambiado otra vez:", thisdict) # puedo hacerlo de esta manera
print("------------")

# Asi agrego una nueva clave
thisdict["transmission"] = "Manual"
print(thisdict)
thisdict.update({"A/C":["Yes","No"]}) #Con .UPDATE tambien puedo anadir claves
print(thisdict)
print("------------")

# Remover Claves
thisdict.pop('transmission')
print(thisdict)
del thisdict["A/C"]
print(thisdict)
print("------------")

# Un BUCLE en un diccionario
for d in thisdict:
    print(d) #imprime solo las claves
    print(thisdict[d]) #imprime solo los valores
for e, f in thisdict.items():  # tambien puedo imprimir ambos
    print (e, f)
print("------------")

# Diccionarios dentro de otros diccionarios; Diccionarios anidados
theDogs = {
    "Dog1" : {
        "Name" : "Astro",
        "Age" : 2
    },
    "Dog2" :{
        "Name" : "Woody",
        "Age" : 6
    },
    "Dog3" : {
        "Name" : "Ringo",
        "Age"  : 7
    }
}
print(theDogs)
print("------------")

# Es posible crear varios diccionarios y agregarlos a uno nuevo
Family = {
    "Name" : "Maga",
    "Age" : 24
}

Life = {
    "Girl Friend" : Family,
    "Pets" : theDogs
}

for e, f in Life.items():
    print (e)
    print (f)
print("------------")








