import os
os.system("clear")

# Usamos "ELIF" como un "Si No"
a = 33
b = 33
if a < b:
    print("\"a\" is greater than \"b\"")
elif a == b:
    print("\"a\" and \"b\" are equal")
print("--------------")

# Usamos "ELSE" para capturar las condiciones no capturadas anteriormente ("entonces")
a = 250
b = 100
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:  # No usa una condicion, concluye las anteriores
    print("a is greater than b")
print("--------------")

# Podemos escribir codigo como una "Conditional Expression"     
print("\"a\" es mayor") if b < a else print("'\b\' es mayor") # en una misma linea
c = 250
print("\'a\'") if a > c else print("=") if a > c else print("\'b\'") # Varias alternativas en misma linea
print("--------------")

# Anidando "IF"
if a > b:
    print("250 above one hundred")
    if a == c:
        print("\'a\' and \'c\' are equal")
    else:
        print("'\"b\' not above '\c\'")
print("--------------")


    


