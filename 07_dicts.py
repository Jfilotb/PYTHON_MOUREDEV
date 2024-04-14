###  DICTIONARIES ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(tuple(my_other_dict))

my_other_dict = {"Nombre": "Johann", "Apellido": "Filot", "Edad": 43, 1: "Python"}

my_dict = {
    "Nombre": "Johann",
    "Apellido": "Filot",
    "Edad": 43,
    "Lenguaje": {"Python", "swift", "Kotlin"},
    1: 1.69
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

my_dict["Nombre"] = "Enrique"
print(my_dict["Nombre"])
print(my_dict[1])
my_dict["Calle"] = "Calle enamorados"
print(my_dict)
