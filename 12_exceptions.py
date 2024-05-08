### EXCEPTIONS HANDLING ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# TRY EXCEPT
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # esto se ejecuta si se produce una excepcion
    print("Se ha producido un error")


# TRY EXCEPT ELSE finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # esto se ejecuta si no se produce una execpcion
    print("La ejecucion continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")

# Exectiones ppor tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")


# CAPTURA DE LA INFORMACION DE LA EXECEPCION

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)
