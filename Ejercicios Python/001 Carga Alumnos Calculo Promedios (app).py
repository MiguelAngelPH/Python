import os
os.system("clear")


# Cumplir con los siguientes requerimientos
# Requerimientos:
# Cargar el nombre del alumno y sus dos notas en una lista
# Las notas tienen que ser una sub lista:
# ejemplos
# ["Juan", [5,7], "Pedro", [6,8], "Maria", [4, 10]]
# Cuando calcula el promedio, debe agregarlo a la sub lista.
# Ejemplos
# ["Juan", [5,7,6], "Pedro", [6,8,7], "Maria", [4, 10, 7]]





notas = []

i = 0
while True:
    print("Menu del Instituto")
    print("     1. Ingrese Nombre y dos notas del alumno")
    print("     2. Calcular el promedio de sus notas")
    print("     3. Mostrar la lista de alumnos con sus notas")
    print("     4. Salir")
    print(" ")

    op = input("-> Elija su opcion ")

    try:
        op = int(op)
    except:
        print("Caracter invalido", op)

    print("Usted selecciono la opcion:", op)

    if op == 1:
        print("       -> Opcion 1")
        nombre = str(input(" Ingrese su nombre: "))
        notas.append(nombre)
        nota1 = int(input(" Ingrese su nota oral: "))
        nota2 = int(input(" Ingrese su nota escrita: "))
        notas.append([nota1, nota2])
        print(nombre, nota1, nota2)
        input("presione enter")
    
    elif op == 2:
        print("       -> Opcion 2")
 
       
        for elementos in notas:
            if isinstance(elementos, list):
                if (len(elementos) == 2):
                    promedio = (elementos[0] + elementos[1]) / 2
                    elementos.append(promedio)
        print(notas)
           
            

    elif op  == 3:
        print("       -> Opcion 3")
        print(notas)
        print ("cantidad de elementos ", len(notas))

    elif op == 4:
        print("       -> Salir, vuelva prontos")
        break
    else:
        print("Fijate bien, esa opcion no existe")

    print(" ")

    input("Enter para continuar")
    os.system("cls")

print (notas)