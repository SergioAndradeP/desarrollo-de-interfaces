print("Un elefante y un ratón pesan juntos 1001 kg, el elefante pesa 1000 kg más que el ratón. ¿Cuánto pesa el ratón?")
print("a) 0.5 Kg")
print("b) 1 Kg")
print("c) 0.5 g")

opcion=None

while(opcion!="a"):
	opcion=input("Introduce una opcion: ")
	print("Opción incorrecta")
	if(opcion!="a" or opcion!="b" or opcion!="c"):
		print("La opción elegida no está entre las posibilidades")

print("Opción correcta")
