from claseAlu import *
from claseProfe import *

class Mate:
    def __init__(self,nomb,nivel):
        self.__nombre=nomb
        self.__nivel=nivel
        self.__conalu=[]
        self.__prof=Profesor('',0,0,'')

    def verNom(self):
        return self.__nombre

    def verNivel(self):
        return self.__nivel

    def verProfe(self):
        return self.__prof

    def verConAlu(self):
        return self.__conalu
    
    def modNom(self,n):
        self.__nombre=n

    def modNivel(self,n):
        self.__nivel=n

    def modProf(self,otrop):
        self.__prof=otrop

    def inscribir(self,alu):
        self.__conalu.append(alu)

    def borrar(self,alu):
        self.__conalu.remove(alu)

    def existe(self,alu):
        return alu in self.__conalu()
        
