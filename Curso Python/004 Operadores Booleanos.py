import os
os.system("clear")

#Booleanos
b=2
c=5
d = b>c
print(b>c)

if b > c:
    print("b es mayor que c")
else:
    print("c es mayor q b")
print("--------------")

#podemos evaluar si una variable es verdadera "casi todos los valores son true"
print(bool(b))
print(bool(d))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print("funcion:", bool(myobj))
print("--------------")

#Una funcion puede devolver un valor booleano
def myFunction() :
  return True

print("valor de la funcion : ", myFunction())
print("--------------")

#Ejecutar un codigo, apartir del valor booleano de una funcion
if myFunction():
    print("valor \"if\" funcion: YES")
else:
    print("no")
print("--------------")

#con esta funcion integrada comprobamos el tipo de dato de una variable, devuelve valor booleano
x = 200
print(isinstance(x, str))
print("--------------")

