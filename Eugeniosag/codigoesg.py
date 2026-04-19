print("soy eugenio")
class Consultorio:
    def __init__(self,id_consultorio,sucursal,piso,medico):
        self.__id_consultorio=id_consultorio
        self.__sucursal=sucursal
        self.__piso=piso
        self.__medico=medico
        self.__medicamentos=[]
        self.__pacientes=[]