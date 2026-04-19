print("soy eugenio")
class Consultorio:
    def __init__(self,id_consultorio,sucursal,piso,medico):
        self.__id_consultorio=id_consultorio
        self.__sucursal=sucursal
        self.__piso=piso
        self.__medico=medico
        self.__medicamentos=[]
        self.__pacientes=[]
    
    def agregar_medicamento(self, id_medicamento ,nombre_medicamento, precio):
        medicamento = {"id_medicamento": id_medicamento, "nombre": nombre_medicamento, "precio": precio}
        self.__medicamentos.append(medicamento)
        print("Agregado")
    
    def mostrar_medicamentos(self):
        for medicamento in self.__medicamentos:
            print(medicamento)
            
    def agregar_paciente(self,id_paciente,nombre_paciente,):
        paciente = {"ID":id_paciente, "nombre": nombre_paciente}
        self.__pacientes.append(paciente)
        print("Agregado")
    
    def mostrar_pacientes(self):
        for paciente in self.__pacientes:
            print(paciente)
        