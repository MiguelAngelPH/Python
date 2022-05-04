import os
os.system("clear")

#Conversion del tipo de una variable
print("Variables Originales: ")
x = 1
y = 2.8
z = 1j

print("sus Tipos: ")
print(x, type(x))
print(y, type(y))
print(z, type(z))

print("---------")
print("convertimos el tipo de dato de nuestras variables")

#convierto a X en float
a = float(x)

#convierto a Y en int
b = int(y)

#convierto a X en complex:
c = complex(x)

print("sus nuevos tipos: ")
print(a, "=", type(a))
print(b, "=", type(b))
print(c, "=", type(c))

print("---------")

print("---------")
#PARA SACAR UN NUMERO RANDOM
print("Un numero RANDOM")
import random
print(random.randrange(1, 10))

print("---------")



