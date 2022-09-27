from random import randrange
p1=randrange(1,4)
p2=randrange(1,4)
while(p2==p1):
	p2=randrange(1,4)

puntuacion=0

if(p1==1 or p2==1):
	print("Un elefante y un ratón pesan juntos 1001 kg, el elefante pesa 1000 kg más que el ratón. ¿Cuánto pesa el ratón?")
	print("a) 0.5 Kg")
	print("b) 1 Kg")
	print("c) 0.5 g")
	print("\n")

	opcion=input("Introduce una opcion: ")

	while(opcion!="a" and opcion!="b" and opcion!="c"):
		print("La opción elegida no está entre las posibilidades")
		print("\n")
		opcion=input("Introduce una opcion: ")
		print("\n")
			
	if(opcion=="a"):
		print("Opción correcta")
		print("\n")
		puntuacion+=10
	else:
		print("Opcion incorrecta")
		print("\n")
		puntuacion-=5

if(p1==2 or p2==2):
	print("Quien ganó el mundial de League of legends en la temporada 3?")
	print("a) Fnatic")
	print("b) G2")
	print("c) SK Telecom T1")
	print("\n")

	opcion=input("Introduce una opcion: ")
	print("\n")

	while(opcion!="a" and opcion!="b" and opcion!="c"):
		print("La opción elegida no está entre las posibilidades")
		print("\n")
		opcion=input("Introduce una opcion: ")
		print("\n")
			
	if(opcion=="c"):
		print("Opción correcta")
		print("\n")
		puntuacion+=10
	else:
		print("Opcion incorrecta")
		print("\n")
		puntuacion-=5

if(p1==3 or p2==3):	
	print("Cual es la capital de Suiza?")
	print("a) Roma")
	print("b) Berna")
	print("c) Berlín")
	print("\n")

	opcion=input("Introduce una opcion: ")
	print("\n")

	while(opcion!="a" and opcion!="b" and opcion!="c"):
		print("La opción elegida no está entre las posibilidades")
		print("\n")
		opcion=input("Introduce una opcion: ")
		print("\n")
			
	if(opcion=="b"):
		print("Opción correcta")
		print("\n")
		puntuacion+=10
	else:
		print("Opcion incorrecta")
		print("\n")
		puntuacion-=5
	
print("Tu puntuación total es: "+str(puntuacion))

