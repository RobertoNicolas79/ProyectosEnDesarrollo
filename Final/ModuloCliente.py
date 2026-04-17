from ClaseTienda import*
from ClaseCliente import*
from ClasePersona import*

tienda=Tienda()
def agregarcliente():

	pregunta=input("Agregar cliente s/n?: ")
	cont=0
	
	while pregunta=='s':
    
		cont=cont+1
		nombre=input("Ingrese nombre: ")
		apellido=input("Ingrese apellido: ")
		dni=input("Ingrese DNI: ")
		fecha=input("Ingrese fecha de nacimiento: ")
		
		cliente=Cliente(cont,nombre,apellido,dni,fecha)
		tienda.agregarCliente(cliente)
		
		pregunta=input("Agregar cliente s/n?: ")
	
cli=tienda.verlistaCliente()

def verificarcliente():
	
	cliente=input("\n Ingrese dni del cliente: ")
	k=False
	for c in cli:
		if c.verDni()==cliente:
			print("\n CLIENTE \n",c.verCont(),")",c.verNombre(),c.verApellido(),"--->",c.verDni())
			k=True
	if k==False:
		print("El cliente no existe")
		agregarcliente()
			
			
def vercliente():
	print ("\n LISTA CLIENTES")
	
	for c in cli:
		print (c.verCont(),")",c.verNombre(),c.verApellido(),"--->",c.verDni())



	

