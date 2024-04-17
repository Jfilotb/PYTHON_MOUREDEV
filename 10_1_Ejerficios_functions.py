# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludo():
    print("Hola amiga!")
    return


saludo()

# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.


def name(nombre):
    print("Hola", nombre, "!.")
    return


name('Ana Milena')

# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.


def factorial(n):
    num = 1
    for i in range(n):
        num *= i + 1
    return num


print(factorial(4))
print(factorial(20))

# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.


def iva_fact(cant_sin_iva, porcentaje=21):
    return cant_sin_iva + cant_sin_iva * porcentaje / 100


print(iva_fact(1000, 10))
print(iva_fact(1000))

# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.


def area_of_circle(r):
    PI = 3.1415
    return PI * r ** 2


def volumen_cilindro(r, altura):
    return area_of_circle(r) * altura


print(volumen_cilindro(3, 5))


# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def media(list_media):
    return sum(list_media)/len(list_media)


print(media([1, 2, 3, 4, 5]))
print(media([3.5, 4.3, 9.7, 2.5, 5.3, 6.9]))


# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

# SOLUCION 1

def list_cuadrado(cuadrado):
    list = []
    for i in cuadrado:
        list.append(i**2)
    return list


print(list_cuadrado([1, 2, 3, 4, 5]))

# SOLUCION 2


def list_cuadrad(*cuadrado):
    list = []
    for i in cuadrado:
        list.append(i**2)
    return list


print(list_cuadrad(2.3, 5.7, 6.8, 9.7, 12.5, 15.6))


# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario
# con su media, varianza y desviación típica.

def med_variacion(measures):
    list = []
    for i in measures:
        list.append(i**2)
    return list


def diccio_vari(vrias_medidas):
    dic = {}
    dic['media'] = sum(vrias_medidas)/len(vrias_medidas)
    dic['varianza'] = sum(med_variacion(vrias_medidas)) / \
        len(vrias_medidas) - dic['media'] ** 2
    dic['desviacion tipica'] = dic['varianza'] ** 0.5
    return dic


print(diccio_vari([1, 2, 3, 4, 5]))

# SOLUCION ALTERNATIVA


def med_variacion(*measires):
    list = []
    for i in measires:
        list.append(i ** 2)
        return list


def diccio_vari(*vrias_medidas):
    dic = {}
    dic['media'] = sum(vrias_medidas)/len(vrias_medidas)
    dic['varianza'] = sum(med_variacion(*vrias_medidas)) / \
        len(vrias_medidas) - dic['media'] ** 2
    dic['desviacion tipica'] = dic['varianza'] ** 0.5


print(diccio_vari(2.3, 5.7, 6.8, 9.7, 12.5, 15.6))

# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.


def maximo_como_divisor(x, y):
    num = 0
    while (y > 0):
        num = y
        y = x % y
        x = num
    return x


def minimo_como_multiplo(x, y):
    if x > y:
        number = x
    else:
        number = y
    while (number % x != 0) or (number % y != 0):
        number += 1
    return number


print(maximo_como_divisor(24, 36))
print(minimo_como_multiplo(24, 36))

# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.


def to_decimal(x):
    x = list(x)
    x.reverse()
    decimal = 0
    for i in range(len(x)):
        decimal += int(x[i]) * 2 ** i
    return decimal


def to_binario(y):
    binario = []
    while y > 0:
        binario.append(str(y % 2))
        y //= 2
    binario.reverse()
    return ''.join(binario)


print(to_decimal('10110'))
print(to_binario(22))
print(to_decimal(to_binario(22)))
print(to_binario(to_decimal('101110')))


# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que
#  contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior
# y devuelva una tupla con la palabra más repetida y su frecuencia.

def count_words(text):
    text = text.split()
    words = {}

    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words


def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq


text = 'Como quieres que te quieras si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))
