from ClasePersona import * 
from ClaseTarjeta import *
from ClaseCliente import *
from ClaseProducto import *
from ModuloTarjeta import *
from ModuloCliente import *
from ModuloProducto import *
from ModuloCarro import*

def Menu():
	
	opcion=100
	
	while opcion!="0":
		
		print("\n ########################Tienda Trucha########################\n 1_Producto")
		print(" 2_Compras")
		print(" 3_Tarjetas")
		print(" 0_Salir")
		opcion=input("\n Ingrese una opcion: ")
		
		if opcion=="1":
			menuproducto()
			
		if opcion=="2":
			op=100
			while op!="0":
				
				print("\n ########################ModuloCompra########################\n 1_Agregar producto al carro")
				print(" 2_Identificar cliente")
				print(" 0_Atras")
				op=input("\n Ingrese una opcion: ")
				
				if op=="1":
					menucompras()
				if op=="2":
					verificarcliente()
		
		if opcion=="3":
			menutarjeta()
Menu()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
