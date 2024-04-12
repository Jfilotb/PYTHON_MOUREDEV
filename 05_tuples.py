### TUPLES ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (43, 1.69, "Johann", "Filot")
my_other_tuple = (43, 42, 21, 20)
print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError


print(my_tuple.count("Filot"))
print(my_tuple.index("Johann"))

# my_tuple[2] = 1.90 indexError 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

# se cambia a una lista para trabajar (actualizar la tupla)
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Jofiba"
my_tuple.insert(1, "Blanco")
my_tuple = tuple(my_tuple)  # aca la volvemos a comvertir en tupla
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
