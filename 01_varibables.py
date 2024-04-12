# Variables

my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Conctenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variable en una sola linea !CUIDADO CON ABUSAR DE ESTA SINTAXIS!
name, surname, alias, age = "Johann", "Filot", "JOFIBA", 43
print("Me llamo:", name, surname, ". Mi edad es:",
      age, "años. Y mi alias es:", alias)


# Input

'''name = input('What is your name: ') # Cual es tu nombre
age = input('How old are you? ') # Cuantos años tienes

print(name)
print(age)'''

# Forzamos el Tipo
addres: str = "Mi direccion"
addres = 32
print(type(addres))
