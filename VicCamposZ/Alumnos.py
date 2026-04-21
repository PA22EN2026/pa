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