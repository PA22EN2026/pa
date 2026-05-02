class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3 
    
    def get_num1(self):
        return self.__num1

    def get_num2(self):
        return self.__num2

    def get_num3(self):
        return self.__num3
    
    def set_num1(self, num1):
        self.__num1 = num1

    def set_num2(self, num2):
        self.__num2 = num2

    def set_num3(self, num3):
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
    
    
obj = Mi_Clase(5, 10, 5)

print("Num1:", obj.get_num1())
print("Num2:", obj.get_num2())
print("Num3:", obj.get_num3())

print("Suma:", obj.sumar())
print("Mayor:", obj.mayor())
print("Menor:", obj.menor())
print("¿Son iguales?:", obj.iguales())
print("Concatenación:", obj.concatenar())
    


