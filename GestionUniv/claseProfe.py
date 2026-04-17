# clase Profesor
from clasePer import *
class Profesor(Persona):
    def __init__(self, nom,ed,doc,cargo):
        super().__init__(nom,ed,doc)
        self.__cargo=cargo
        self.__horarios=dict()
        self.__horarios['lunes']=[]

   
    def verCargo(self):
        #Retorna el cargo de un profesor
        return self.__cargo

    def modiCargo(self,p):
        #Modifica el cargo de un profesor
        self.__cargo=p

    def verHorarios(self,dia):
        return self.__horarios[dia]

    def agregarhor(self,dia,hora,mat):
        self.__horarios[dia].append([hora,mat])

    def modifhorario(self,dia,hora,otraM):
        for a in self.__horarios[dia]:
            if a[0]==hora:
                a[1]=otraM
            
            
  
