print("VicCamposZ")

class Alumnos: 
     def __init__(self, matricula, nombre, carrera, semestre, edad):
        self.__matricula = matricula
        self.__nombre = nombre
        self.__carrera = carrera
        self.__semestre = semestre
        self.__edad = edad

     def get_matricula(self):
        return self.__matricula
 
     def et_nombre(self):
        return self.__nombre

     def get_carrera(self):
        return self.__carrera

     def get_semestre(self):
        return self.__semestre

     def get_edad(self):
        return self.__edad
     
     def set_matricula(self, matricula):
         self.__matricula = matricula
     
     def set_nombre(self, nombre):
        self.__nombre = nombre

     def set_carrera(self, carrera):
        self.__carrera = carrera

     def set_semestre(self, semestre):
        self.__semestre = semestre

     def set_edad(self, edad):
        self.__edad = edad