### STRINGS ###

my_string = "Mi String"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_other_string + " " + my_other_string)

my_new_line_string = "Este en un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# FORMATEO

name, surname, age = "Johann", "Filot", 43

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# DESEMPAQUETADO DE CARATERES

lenguaje = "python"
a, b, c, d, e, f = lenguaje
print(a)
print(f)

# DIVISION

language_slice = lenguaje[1:3]
print(language_slice)

language_slice = lenguaje[1:]
print(language_slice)

language_slice = lenguaje[-2]
print(language_slice)

# REVERSE

reversed_language = lenguaje[::-1]
print(reversed_language)

# FUNCIONES

print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("t"))
print(lenguaje.isnumeric())
print("1".isnumeric())
print(lenguaje.lower())
print(lenguaje.upper().isupper())
print(lenguaje.startswith("py"))
