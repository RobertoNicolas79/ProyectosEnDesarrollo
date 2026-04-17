from ClasePersona import * 

class Cliente(Persona):
	def __init__(self,cont,nombre,apellido,dni,nacimiento):
		super().__init__(cont,nombre,apellido,dni)
		self.__nacimiento=nacimiento
	
	def verfechaNac(self):
		return self.__nacimiento
		
	def modfechaNac(self,oNacimiento):
		self.__nacimiento=oNacimiento
		
	
