from ast import arg
import os
os.system("clear")

def space():
    print("---------")

# Funciones
# Recibe datos: "parametros" 
# Devuelve datos en forma de resultado
# Se le llama cuando se le necesita
# Se define usando la palabra clave "DEF :"

def my_function():
    print("Hello, from my function!")

my_function()
space()

# Tambien podemos pasar informacion en forma de argumentos
# Estos argumentos se ponen entre parentesis, despues del nombre de la funcion
# Se pueden mandar dos argumentos o mas
def my_2function(args, args2):
    print( "Los argumentos que pase: ", args, ":", args2 )

my_2function("Email", "day@hola.com")
my_2function("Name", "Miguel Angel")
my_2function("adress", "Buenos Aires")

space()

# Si al definir la firma de la funcion no se sabe la cantidad de argumentos
# Se agrega un "*" antes del nombre del parametro
# Permite agregar args en forma de Tupla
def my_3function(* kids):
    print('the youngest child is:' + kids[2]) #accede al indice

my_3function("Tobias", "Emil", "Linus")
space()

# Se pueden agregar argumentos a cada clave
def my_4function(child1, child2, child3):
    print("the youngest child is:" + child3)

my_4function(child1 = "Tobias", child3 = "Emil", child2 = "brian")
space()

def my_5function( **kid):
    print("His last name is: " + kid["lastN"])

my_5function(firstN = "Mike", lastN = "Perez", 
            firstN1 = "Brian", lastN2 = "Smith")
space()

# Podemos pasar cualquier tipo de datos a una funcion
# Cuando este dentro de la funcion, seguira siendo mismo tipo de dato de su creacion
def my_6function (Food):
    print("El parametro es del tipo:", type(fruits))
    for x in Food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_6function(fruits)
space()

# Devolver un resultado con "RETURN"
def my_7function(x):
    return 5 * x

print(my_7function(5))
print(my_7function(8))
print(my_7function(2))
space()