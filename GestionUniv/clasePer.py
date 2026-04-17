# clase Persona

class Persona:
    def __init__(self, nom,ed,doc):
        self.__nombre=nom
        self.__edad=ed
        self.__dni=doc

    def verNomB(self):
        #Retorna el nombre de una persona
        return self.__nombre

    def verEdad (self):
        #Retorna la edad de una persona
        return self.__edad

    def verDni(self):
        #Retorna el dni de una persona
        return self.__dni

    def modiNom(self,n):
        #Modifica el nombre de una persona
        self.__nombre=n

    def modiEdad(self,e):
        #Modifica la edad de una persona
        self.__edad=e

    def modiDni(self,d):
        #Modifica el dni de una persona
        self.__dni=d

