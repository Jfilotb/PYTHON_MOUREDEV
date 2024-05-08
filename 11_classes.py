### CLASSES ###

class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person('Johann', "Filot")
print(my_person.full_name)
my_person.walk()

my_other_person = Person('Johann', 'Filot', 'JOFIBA')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Stiven Filot Diaz (Estudia auxiliar de vuelo)"
print(my_other_person.full_name)
