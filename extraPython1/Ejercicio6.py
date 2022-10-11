from Ejercicio3 import isnum
from Ejercicio4 import isChar

def inversa(a):
    trans = ""
    if (isnum(a)):
        print("La entrada es un numero")
        return "Error"
    elif not (isChar(a) and isnum(a)):
        for i in range(len(a)):
            trans = trans + a[(len(a) - 1) - i]
        return trans
    else:
        print("La entrada no deve ser un numero o una sola letra")