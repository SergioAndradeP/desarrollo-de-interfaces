from fibonacci import funcion_fibonacci
from fibonacci2 import funcion_fibonacci2

opcion=input("""Introduce una opcion
a) Función fibonacci 1 (Recursiva)
b) Función fibonacci 2 (No recursiva)\n\n""")

while(opcion!="a" and opcion!="b"):
	print("Opción incorrecta")
	opcion=input("Introduce una opción correcta: ")
	
if(opcion=="a"):
	numero = int(input("Introduce el enésimo término de la sucesión de fibonacci que quieres calcular: "))
	while(numero<0):
		if(numero<0):
			print("El número introducido no es positivo")
		numero = int(input("Introduce el enésimo término de la sucesión de fibonacci que quieres calcular: "))
	print(str(funcion_fibonacci(numero)))
else:
	numero = int(input("Introduce el enésimo término de la sucesión de fibonacci que quieres calcular: "))
	while(numero<0):
		if(numero<0):
			print("El número introducido no es positivo")
		numero = int(input("Introduce el enésimo término de la sucesión de fibonacci que quieres calcular: "))
	print(str(funcion_fibonacci2(numero)))
