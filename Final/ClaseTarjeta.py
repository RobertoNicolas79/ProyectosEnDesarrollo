class Tarjeta:
	
	def __init__(self,cont,nomTar,banco,cantforPago,cantCuota,interes):
		self.__cont=cont
		self.__nomTar=nomTar
		self.__banco=banco
		self.__cantforPago=cantforPago
		self.__cantCuota=cantCuota
		self.__interes=interes
		
	
	def verCont(self):
		return self.__cont
	def vernomTar(self):
		return self.__nomTar
	def verBanco(self):
		return self.__banco
	def vercantforPago(self):
		return self.__cantforPago
	def vercantCuota(self):
		return self.__cantCuota
	def verInteres(self):
		return self.__interes
		
	def modCont(self,oCont):
		self.__cont=oCont
	def modnomTar(self,onomTar):
		self.__nomTar=onomTar
	def modBanco(self,oBanco):
		self.__banco=oBanco
	def modcantforPago(self,ocantforPago):
		self.__cantforPago=ocantforPago
	def modcantCuota(self,ocantCuota):
		self.__cantCuota=ocantCuota
	def modInteres(self,oInteres):
		self.__interes=oInteres
	
	
		
	
		
