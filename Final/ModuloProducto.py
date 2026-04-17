from ClaseProducto import*
from ClaseTienda import*

tien=Tienda()

def altaProducto():
	
	x=input("cargar producto? s/n: ")
	cont=0
	
	while x == "s":
		
		cont=cont+1
		codigo = int(input("ingrese codigo del producto: "))
		marca = input("ingrese marca del producto: ")
		descripcion = input("ingrese descripcion del producto: ")
		presentacion = input("ingrese tipo de presentacion -unidad/ por 6/ por 12: ")
		precio = int(input("ingrese precio por unidad del producto: "))
		
		prod=Producto(cont,codigo, marca, descripcion, presentacion, precio,0)
		tien.agregarProducto(prod)
		
		x=input("cargar producto? s/n: ")
		print("") 
                        
 
lista=tien.verlistaProducto()
def altaPromociones():
	print("Listado de productos disponibles\n")
	for c in lista:
		print(c.verCont(),"-","codigo=",c.verCodigo(),","," marca=",c.verMarca(),",","descripcion=",c.verDescripcion(),",\n"
		"        ""presentacion=",c.verPresentacion(),",","precio=","$",c.verPrecio(),",","descuento=",c.verDescuento(),"%")
                
	Nuevoproducto=int(input("\n seleccione un producto para aplicar descuento: "))
	nuevoDesc=int(input("\n ingrese el porcentaje de descuento para la promocion: "))
                
	for c in lista:
		if c.verCont()==Nuevoproducto:
			c.modDescuento(nuevoDesc)
		else:
			print ("El producto no esta disponible")
                                
def listarProductos():
	print("\n Lista de productos disponibles")
	for c in lista:
		print("\n",c.verCont(),"-","codigo=",c.verCodigo(),","," marca=",c.verMarca(),",","descripcion=",c.verDescripcion(),",\n"
		"        ""presentacion=",c.verPresentacion(),",","precio=","$",c.verPrecio(),",","descuento=",c.verDescuento(),"%")
                
def listarPromociones():
	for c in lista:
		if c.verDescuento()>0:
			print(c.verCont(),"-","codigo=",c.verCodigo(),","," marca=",c.verMarca(),",","descripcion=",c.verDescripcion(),",\n"
			"        ""presentacion=",c.verPresentacion(),",","precio=","$",c.verPrecio(),",","descuento=",c.verDescuento(),"%")
		else:
			print ("Actualmente no hay productos en promocion")
                        
def menuproducto():
	opcion=0
	
	while opcion!="0":
		print ("\n ########################ModuloProducto########################\n 1_Dar de alta producto")
		print (" 2_Dar de alta promocion")
		print (" 3_Listar productos")
		print (" 4_Listar Promociones")
		print (" 0_Atras")

		
		opcion=input("\n Ingrese una opcion: ")
		
		if opcion=="1":
			altaProducto()
			
		if opcion=="2":
			altaPromociones()
			
		if opcion=="3":
			listarProductos()
			
		if opcion=="4":
			listarPromociones()
			

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


