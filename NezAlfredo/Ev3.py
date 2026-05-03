#Profe ya tenía el código pero no sabía como acceder al repositorio del grupo y le pedí ayuda a unos compañeros
class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

 # Getters
    def get_num1(self):
        return self.__num1

    def get_num2(self):
        return self.__num2

    def get_num3(self):
        return self.__num3
    
 # Setters
    def set_num1(self, valor):
        self.__num1 = valor

    def set_num2(self, valor):
        self.__num2 = valor

    def set_num3(self, valor):
        self.__num3 = valor
    
  # Métodos
    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3
    
    def mayor(self):
        return max(self.__num1, self.__num2, self.__num3)