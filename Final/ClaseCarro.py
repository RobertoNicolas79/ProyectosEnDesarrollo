from ClasePersona import* 
from ClaseTarjeta import*
from ClaseCliente import*
from ClaseProducto import*
from ModuloTarjeta import*
from ModuloCliente import*
from ModuloProducto import*

class Carro():
	
	def __init__(self):
		self.__listaCarro=[]
		
	def agregaralCarro(self,prod):
		self.__listaCarro.append(prod)
	def quitardelCarro(self,prod):
		self.__listaCarro.remove(prod)
	def verCarro(self):
		return self.__listaCarro
