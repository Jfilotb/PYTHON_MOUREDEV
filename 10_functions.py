### FUNCTIONS ###

'''
Functions: Una función es un bloque reutilizable de código o declaraciones de programación diseñadas 
para realizar una determinada tarea. Para definir o declarar una función, Python proporciona la palabra 
clave def . La siguiente es la sintaxis para definir una función. El bloque de funciones de código se
ejecuta solo si se llama o invoca la función.
'''


def my_functons():
    print("Esto es una funcion")


my_functons()


def sum_two_values(frist_values, second_values):
    print(frist_values + second_values)


sum_two_values(14, 20)


def sum_two_values_return(num1, num2):
    return num1 + num2


my_result = sum_two_values_return(10, 5)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Filot", name="Johan")


# LLAMADOS POR DEFECTOS

def print_name_with_defaut(name, suename, alias="Sin alias"):
    print(f"{name} {suename} {alias}")


print_name_with_defaut("Johann", "Filot", "JOFIBA")
print_name_with_defaut("Johann", "Filot")


def print_texts(*texts):
    for text in texts:
        print(text)


print_texts("Hola", "Ana", "Milena")

# DECLARAR Y LLAMAR A UNA FUNCION

# SYNTAX / DECLARAR A FUNCION


'''def function_name():
    Condes
    codes


# calling a function
function_name()'''

# FUNCTION SIN PARAMETROS (Lfuncion se puede declarar sin parametros)

# Ejemplos


def generate_full_name():
    frist_name = 'Johann'
    last_name = 'Filot'
    space = ' '
    full_name = frist_name + space + last_name
    print(full_name)


generate_full_name()  # calling a function


def add_two_number():
    num_one = 3
    num_two = 2
    total = num_one + num_two
    print(total)


add_two_number()

# FUNCION CON PARAMETROS:

'''En una función podemos pasar diferentes tipos de datos (número, cadena, booleano, lista, tupla,
diccionario o conjunto) como parámetro

Parámetro único: si nuestra función toma un parámetro, debemos llamar a nuestra función con un argumento'''

'''def function_name(parametros):
    Condes
    codes
calling a function
function_name(argumentos)'''


def greetings(name):
    message = name + ', welcome to Python for Everyone'
    return message


print(greetings("Johann Filot"))


def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(90))


def square_number(x):
    return x * x


print(square_number(2))


def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area


print(area_of_circle(5))


def sum_of_number(n):
    total = 0
    for i in range(n+1):
        total += i
        print(total)


print(sum_of_number(10))
print(sum_of_number(100))


def calculate_age(current_year, brith_year):
    age = current_year - brith_year
    return age


print('Age: ', calculate_age(2024, 1979))


#  DEVOLVER UN VALOR BOOLEANO

def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False


print(is_even(10))
print(is_even(7))

# DEVOLVER UNA LISTA


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(100))

# FUNCION CON PARAMETRO PREDETERMINADO


def greetings(name='Milena'):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings())
print(greetings('Stiven'))


def weigth_of_object(mass, gravity=9.81):
    weigth = str(mass * gravity) + ' N'
    return weigth


print('Peso de un objeto en Newtons', weigth_of_object(100))
print('Peso de un objeto en Newtons', weigth_of_object(100, 1.62))


# Función como parámetro de otra función

# You can pass functions around as parameters
def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))  # 27
