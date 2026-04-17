from clasePer import *
from claseAlu import *
from claseMater import *
from claseProfe import *


class Universidad:

    def __init__(self,name):
        self.__nomb=name
        self.__conProf=[]
        self.__conAlu=[]
        self.__conMat=[]

    def verName(self):
        return self.__nomb

    def modName(self,o):
        self._name=o
        
    def verMat(self):
        return self.__conMat
    
    def agregaAl(self,alu):
        self.__conAlu.append(alu)

    def agregaProfe(self,pro):
        self.__conProf.append(pro)

    def agregaMat(self,mat):
        self.__conMat.append(mat)

    def inscribe(self,mat,alu):
        pos=self.__conMat.index(mat)     #busca la posicion de la materia
        self.__conMat[pos].inscribir(alu) #inscribe al alumno en la materia

    def asignaProfe(self,mat,pr):
        pos=self.__conMat.index(mat)     #busca la posicion de la materia
        self.__conMat[pos].modProf(pr)  #inscribe al profesor en la materia

    def listaAlumnos(self,mat):
        pos=self.__conMat.index(mat)     #busca la posicion de la materia
        pro=self.__conMat[pos].verProfe()   #toma el profesor de la materia
        alus=self.__conMat[pos].verConAlu()   #toma el conj de alumnos de la materia
        print('Materia: ',mat.verNom(),'\n')
        print('Profesor: ',pro.verNomB(),'\n')
        print('Listado de alumnos\n')
        for a in alus:
            print (a.verNomB())

        
        

        
        


        
