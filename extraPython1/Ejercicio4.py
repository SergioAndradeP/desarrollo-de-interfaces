from Ejercicio3 import isnum

def isChar(s):
    if (len(s) > 1):
        return False
    if (len(s) == 1):
        return True


def isvoc(s):
    vocales = "aeiouáéíóú"
    if not (isnum(s)) and (isChar(s)):
        for i in range(len(vocales)):
            for j in range(len(s)):
                if (vocales[i] == s):
                    return True
                else:
                    return False
    elif (isnum(s)):
        print("El valor es un numero")
    elif not (isChar(s)):
        print("El valor no es solo un caracter")