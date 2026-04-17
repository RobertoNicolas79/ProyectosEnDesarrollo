# clase Alumno
from clasePer import *
class Alumno(Persona):
    def __init__(self, nom,ed,doc,pr):
        super().__init__(nom,ed,doc)
        self.__prom=pr
        self.__horarios=dict()
        self.__horarios['lunes']=[]

   
    def verProm(self):
        #Retorna el promedio de un alumno
        return self.__prom

    def modiProm(self,p):
        #Modifica el promedio de un alumno
        self.__prom=p

    def verHorarios(self,dia):
        return self.__horarios[dia]

    def agregarhor(self,dia,hora,mat):
        self.__horarios[dia].append([hora,mat])

    def modifhorario(self,dia,hora,otraM):
        for a in self.__horarios[dia]:
            if a[0]==hora:
                a[1]=otraM
            
            
  
