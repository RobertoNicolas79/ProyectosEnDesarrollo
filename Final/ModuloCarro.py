from ClasePersona import* 
from ClaseTarjeta import*
from ClaseCliente import*
from ClaseProducto import*
from ClaseCarro import*
from ModuloTarjeta import*
from ModuloCliente import*
from ModuloProducto import*

carro=Carro()


def agregarproductocarro():
	global porcentaje
	global cantidad
	global acumulador	
	listarProductos()
	
	numero=int(input("\n seleccione un producto para añadir al carro de compras: "))
	cantidad=int(input("\n ingrese la cantidad de unidades para comprar: "))

	acumulador=0
	
	for c in lista:
		porcentaje=c.verDescuento()/(100)
		if c.verCont()==numero:
			producto=Producto(c.verCont(),c.verCodigo(),c.verMarca(),c.verDescripcion(),c.verPresentacion(),c.verPrecio(),c.verDescuento())
			carro.agregaralCarro(c)
			acumulador=acumulador+c.verPrecio()*(cantidad)
			acumulador=acumulador*(1-porcentaje)
				
		else:
			print("El codigo ingresado no se encuentra disponible")

def quitarproductocarro():
		
		listarProductos()
	
		codigo=int(input("\n seleccione un producto para quitar del carro de compras: "))
                
		for c in lista:
			if c.verCont()==codigo:
                                
				carro.quitardelCarro(c)
				
	
def vercarro():
	listacarro=carro.verCarro()

	
	for c in listacarro:
		print ("\n CARRO")
		print("\n",c.verCont(),"-","codigo=",c.verCodigo(),","," marca=",c.verMarca(),",","descripcion=",c.verDescripcion(),",\n"
			"        ""presentacion=",c.verPresentacion(),",","precio=","$",c.verPrecio(),",","descuento=",c.verDescuento(),"%","\n ---->Cantidad",cantidad,"\n Monto Total a Pagar: ","$",acumulador)
	
		
def menucompras():
	opcion=0
	
	while opcion!="0":
		print ("\n ########################ModuloCompra########################\n 1_Agregar producto al carro")
		print (" 2_Quitar Producto del carro")
		print (" 3_Ver Carro")
		print (" 0_Atras")
		
		opcion=input("\n Ingrese una opcion: ")
		if opcion=="1":
			agregarproductocarro()
		if opcion=="2":
			quitarproductocarro()
		if opcion=="3":
			vercarro()

		
	







