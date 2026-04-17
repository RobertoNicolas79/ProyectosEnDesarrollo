from ClasePersona import * 
from ClaseTarjeta import *
from ClaseCliente import *
from ClaseProducto import *

class Tienda():
	
	def __init__(self):
	
		self.__listaTarjeta=[]
		self.__listaCliente=[]
		self.__listaProducto=[]
		
	
	def agregarTarjeta(self,tarjeta):
		self.__listaTarjeta.append(tarjeta)
	def borrarTarjeta(self,tarjeta):
		self.__listaTarjeta.remove(tarjeta)
	def verlistaTarjeta(self):
		return self.__listaTarjeta
	
	def agregarCliente(self,cliente):
		self.__listaCliente.append(cliente)
	def borraCliente(self,cliente):
		self.__listaCliente.remove(cliente)
	def verlistaCliente(self):
		return self.__listaCliente

	def agregarProducto(self,producto):
		self.__listaProducto.append(producto)
	def borrarProducto(self,producto):
		self.__listaProducto.remove(producto)
	def verlistaProducto(self):
		return self.__listaProducto
		
		
			
        
		
	
