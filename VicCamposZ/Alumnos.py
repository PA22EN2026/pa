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
 
     def get_nombre(self):
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

     def mayor_edad(self):
      if self.__edad >= 18:
        return "Es mayor de edad"
      else:
        return "Es menor de edad"
     def cambiar_carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera

     def info(self):
        return f"Matricula: {self.__matricula}, Nombre: {self.__nombre}, Carrera: {self.__carrera}, Semestre: {self.__semestre}, Edad: {self.__edad}"
     
alumno1 = Alumnos(123, "Victoria", "Programacion", 2, 18)

print("Informacion")
print(alumno1.info())


print("Mayoria edad")
print(alumno1.mayor_edad())
print("*cambiar carrera*")
alumno1.cambiar_carrera("Administracion")
print(alumno1.info())
print("Midificar alumno")
alumno1.set_nombre("Abigail")
alumno1.set_edad(19)
print(alumno1.info())
print("*Usando Getters*")
print("Nombre:", alumno1.get_nombre())
print("Edad:", alumno1.get_edad())
print("Carrera:", alumno1.get_carrera())