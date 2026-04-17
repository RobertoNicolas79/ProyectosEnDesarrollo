class Producto():
	def __init__(self, cont, codigo, marca, descripcion, presentacion, precio, descuento):
		self.__cont=cont
		self.__codigo=codigo
		self.__marca = marca	
		self.__descripcion = descripcion
		self.__presentacion = presentacion 
		self.__precio = precio
		self.__descuento=descuento
        
	def verCont(self):
		return self.__cont
	def verCodigo(self):
		return self.__codigo
	def verMarca(self):
		return self.__marca
	def verDescripcion(self):
		return self.__descripcion
	def verPresentacion(self):
		return self.__presentacion
	def verPrecio(self):
		return self.__precio
	def verDescuento(self):
		return self.__descuento
        
	def modCont(self, otroCont):
		self.__cont=otroCont
	def modCodigo(self, otroCodigo):
		self.__codigo = otroCodigo
	def modMarca(self, otraMarca):
		self.__marca = otraMarca
	def modDescripcion(self, otraDescripcion):
		self.__descripcion = otraDescripcion
	def modPresentacion(self, otrapresentacion):
		self.__presentacion = otraPresentacion
	def modPrecio(self, otroPrecio):
		self.__precio = otroPrecio
	def modDescuento(self, otroDescuento):
		self.__descuento = otroDescuento
