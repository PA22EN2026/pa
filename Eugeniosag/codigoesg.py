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
    
    def costo_total(self):
        total=0
        for i in self.__medicamentos:
            total = total + i["precio"]
        return total
    
    def info(self):
        print(f"ID: {self.__id_consultorio}")
        print(f"Sucursal: {self.__sucursal}")
        print(f"Piso: {self.__piso}")
        print(f"Médico: {self.__medico}")
        
    def get_id_consultorio(self):
        return self.__id_consultorio

    def get_sucursal(self):
        return self.__sucursal

    def get_piso(self):
        return self.__piso

    def get_costo(self):
        return self.__costo

    def get_medico(self):
        return self.__medico

    def get_medicamentos(self):
        return self.__medicamentos

    def get_pacientes(self):
        return self.__pacientes