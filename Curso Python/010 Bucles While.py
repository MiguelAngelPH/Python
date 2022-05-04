import os
os.system("clear")

# Los dos ciclos primitivos son "WHILE" Y "FOR"
# Con un "WHILE" podemos ejecutar acciones, mientras una condicion sea verdadera
i = 1
while i < 6:
    print(i)
    i += 1
print("--------------")

# Podemos parar el proceso de un "WHILE" con un proceso "BREAK", incluso si la condicion del "WHILE" es verdadera
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("--------------")

# Con el proceso "CONTINUE" obviamos un paso, y sin embargo sigue contando
i = 1
while i < 6:
    i += 1
    if i == 4:
        continue # con esta instruccion se salta el "i = 4"
    print(i)
print("--------------")

# Cuando el "WHILE" haya salido de su condicion, podemos terminar con un "ELSE" ejecutando una accion
i = 0
while i < 6:
    print(i)
    i += 1
else: 
    print("\'i\' is no longer less than \'6\'")
print("--------------")
print("--------------")

# Un 'BUCLE FOR' es usado para iterar sobre una secuencia ("listas, tuples, diccionarios, sets")
# Se ejecuta una vez, por cada elemento de una 'lista, tuples, etc'

# Imprime cada elemento
fruits = ['banana', 'orange', 'cherry', 'apple', 'lemon']
for x in fruits:
    print(x)
print("--------------")

# Tambien es posible hacer un "FOR" para recorrer una cadena de texto
for x in fruits[1]:
    print(x)
print("--------------")

# Podemos usar un "BREAK" dentro de un "FOR"
for x in fruits:
    print(x)
    if x == "cherry":
        break
print("--------------")

# Usando la funcion "RANGE()"
# Esta devuelve un conjunto de numeros
# Nosotros establecemos el limite
for x in range(4):
    print(x) # imprime desde el 0 y asi llegaria al '3'
print("--------------")

'''Al usar un 'RANGE' podemos declarar:
    en donde empezara, donde termina y en
    cuanto va a ir aumentando el contador
'''
for x in range(5, 27, 4):
    print(x)
print("--------------")

''' Al igual que en un "WHILE": 
    podemos utilizar un "ELSE" 
    para concluir una vez que el bucle
    haya finalizaod su sentencia
'''
# Nota: Si lo antecede un "BREAK" el "ELSE" no funcionara
for x in range(3):
    print(x)
else:
    print("Finally finished the bucle")
print("--------------")

# "BUCLES" anidados
# El 'BUCLE' interno se repetira una vez cada ciclo del 'BUCLE' externo
adje = ['red', 'yellow', 'green']
for x in fruits:
    for y in adje:
        print(x, y)
print("--------------")





    







