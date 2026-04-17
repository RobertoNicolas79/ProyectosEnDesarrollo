class Persona:
	
	def __init__(self,cont,nombre,apellido,dni):
		self.__cont=cont
		self.__nombre=nombre
		self.__apellido=apellido
		self.__dni=dni
		
	def verCont(self):
		return self.__cont
	def verNombre(self):
		return self.__nombre
	def verApellido(self):
		return self.__apellido
	def verDni(self):
		return self.__dni
		
	def modCont(self,oCont):
		self.__cont=oCont
	def modNombre(self,oNombre):
		self.__nombre=oNombre
	def modApellido(self,oApellido):
		self.__apellido=oApellido
	def modEdad(self,oDni):
		self.__dni=oDni
	
	
