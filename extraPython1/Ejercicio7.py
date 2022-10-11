from Ejercicio6 import inversa

def isPalindromo(a):
    inv = inversa(a)
    if (inv == a):
        return True
    else:
        return False