### SETS ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un Dicionario

my_other_set = {"Johann", "Filot", 43}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("JOFIBA")
print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("JOFIBA")
print(my_other_set)  # Un set no permite repetidos


print("Johann" in my_other_set)
print("johann" in my_other_set)

my_other_set.remove("Johann")
print(my_other_set)

# Eliminar los elementos de un SETS

my_other_set.clear()
print(my_other_set)

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Johann", "Filot", 43}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Java", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)


print(my_new_set.difference(my_set))
