from fibonacci import funcion_fibonacci

numero = int(input("Introduce el enésimo término de la sucesión de fibonacci que quieres calcular: "))
while(numero<0):
	if(numero<0):
		print("El número introducido no es positivo")
	numero = int(input("Introduce el enésimo término de la sucesión de fibonacci que quieres calcular: "))
print(str(funcion_fibonacci(numero)))
