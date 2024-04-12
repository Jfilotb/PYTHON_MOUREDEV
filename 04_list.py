### LISTS ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [43, 42, 21, 20, 80, 73, 20]

print(my_list)
print(len(my_list))

my_other_list = [43, 1.69, "Johann", "Filot"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(20))
# print(my_other_list[5])  IndexError
# print(my_other_list[-5]) IndexError


age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("IngDatos")
print(my_other_list)

my_other_list.insert(2, "Azul")
print(my_other_list)

my_other_list[2] = "Amarillo"
print(my_other_list)

"""my_other_list.remove("Blanco")
print(my_other_list)

my_list.remove(20)
print(my_list)"""

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)
