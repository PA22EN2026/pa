class Mi_Clase:
    def __init__(self,num1,num2,num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3
    
    def mayor(self):
        return max(self.__num1, self.__num2, self.__num3)
    
    def menor(self):
        return min(self.__num1, self.__num2, self.__num3)
    
    def iguales(self):
        return self.__num1 == self.__num2 == self.__num3
    
    def concatenar(self):
        return str(self.__num1) + str(self.__num2) + str(self.__num3)
    


# pruebas del código

mi_clase = Mi_Clase(8, 12, 8)

print("Suma:", mi_clase.sumar())
print("Mayor:", mi_clase.mayor())
print("Menor:", mi_clase.menor())
print("¿Son iguales?:", mi_clase.iguales())
print("Concatenación:", mi_clase.concatenar())  
