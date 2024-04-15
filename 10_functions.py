### FUNCTIONS ###

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
