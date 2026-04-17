from ClaseTienda import *
from ClaseTarjeta import *



tienda=Tienda()


def agregartarjeta():
	pregunta=input("Agregar tarjeta s/n?: ")
	cont=0
	while pregunta=="s":
		cont=cont+1
		nomTar=input("Ingresar nombre de la tarjeta: ")
		banco=input("Ingrese nombre del banco: ")
		cantforPago=int(input("Ingrese cantidad de formas de pago: "))
		
		cantfor=cantforPago
		num=1
		while cantfor>0:
			
			print("Forma de pago Nº",num)
			cantCuota=int(input("Ingrese cantidad de cuotas: "))
			interes=int(input("Ingrese interes por cuota: "))
			
			tarjeta=Tarjeta(cont,nomTar,banco,cantforPago,cantCuota,interes)
			tienda.agregarTarjeta(tarjeta)
			
			num=num+1
			cantfor=cantfor-1
			if cantfor==0:
				break
		
		pregunta=input("Agregar Tarjeta s/n?: ")
		
tar=tienda.verlistaTarjeta()

def interes():
	for t in tar:
		print("\n Tarjetas Disponibles")
		print ("\n",t.verCont(),")","[Tarjeta Nombre:",t.vernomTar(),"/","Banco:",t.verBanco(),"/","Cantidad formas pago:",t.vercantforPago(),
		"\n        ",t.vercantCuota(),"Cuotas con un",t.verInteres(),"% de interes")	
		
	tarjetaint=int(input("\n Ingrese una tarjeta para aplicar interes: "))
	interespor=int(input("\n Ingrese beneficio para la tarjeta: "))
	m=False	
	for t in tar:
		if t.verCont()==tarjetaint:
			t.modInteres(interespor)
			m=True
		
	if m==False:
		print ("La tarjeta no esta disponible")
		
def vertarjetas():	
	print ("LISTA DE TARJETAS: ")
	for t in tar:
		print ("\n",t.verCont(),")","[Tarjeta Nombre:",t.vernomTar(),"/","Banco:",t.verBanco(),"/","Cantidad formas pago:",t.vercantforPago(),
		"\n        ",t.vercantCuota(),"Cuotas con un",t.verInteres(),"% de interes")
	

def menutarjeta():
	opcion=0
	
	while opcion!="0":
		print ("\n ########################ModuloTarjeta########################\n 1_Dar de alta tarjeta")
		print (" 2_Dar de alta beneficio")
		print (" 3_Listar tarjetas")
		print (" 0_Atras")
		
		opcion=input("\n Ingrese una opcion: ")
		
		if opcion=="1":
			agregartarjeta()
			
		if opcion=="2":
			interes()
			
		if opcion=="3":
			vertarjetas()
			
		

	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
