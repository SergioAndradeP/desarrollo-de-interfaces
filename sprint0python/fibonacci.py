def funcion_fibonacci(n):
	if n<=1:
		return n
	else:
		return funcion_fibonacci(n-1) + funcion_fibonacci(n-2)

numero = int(input("Introduce el enésimo término de la sucesión de fibonacci que quieres calcular: "))
while(numero<0):
	if(numero<0):
		print("El número introducido no es positivo")
	opcion = input("Introduce el enésimo término de la sucesión de fibonacci que quieres calcular: ")
print(str(funcion_fibonacci(numero)))
