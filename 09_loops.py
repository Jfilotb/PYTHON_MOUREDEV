### LOOPS O BUCLES ###

# WIHLE

my_condiction = 0

while my_condiction < 10:
    print(my_condiction)
    my_condiction += 1
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condiction < 20:
    my_condiction += 1
    if my_condiction == 15:
        print("Se detiene la ejecucion")
        break

    print(my_condiction)

print("La ejecucion continua")

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# FOR

my_list = [43, 42, 21, 20, 80, 73, 20]

for element in my_list:
    print(element)

# Tuple guarda elementos que no se pueden tocar
my_tuple = (43, 1.69, "Johann", "Filot")

for element in my_tuple:
    print(element)

my_set = {"Johann", "Filot", 43}  # Set guarda elementos que no sean repetidos

for element in my_set:
    print(element)

my_dict = {"Nombre": "Johann", "Apellido": "Filot", "Edad": 43,
           1: "Python"}  # Diccionario de forma clave valor

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para mi dicionario a finalizado")


for element in my_dict:
    print(element)
    if element == "Edad":
        continue
else:
    print("El bucle for para mi dicionario a finalizado")
