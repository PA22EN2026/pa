class Mi_clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumas(self):
        suma = self.__num1 + self.__num2 + self.__num3
        return suma 

    def mayor(self):
        if self.__num1 > self.__num2 and self.__num1 > self.__num3:
            return "El numero 1 es mayor"
        elif self.__num2 > self.__num1 and self.__num2 > self.__num3:
            return "El numero 2 es mayor"
        else:
            return "El numero 3 es mayor"

    def menor(self):
        if self.__num1 < self.__num2 and self.__num1 < self.__num3:
            return "El numero 1 es menor"
        elif self.__num2 < self.__num1 and self.__num2 < self.__num3:
            return "El numero 2 es menor"
        else: 
            return "El numero 3 es menor"

    def iguales(self):
        if self.__num1 == self.__num2 == self.__num3:
            return True 
        else: 
            return False

    def concatenar(self):
        txt1 = str(self.__num1)
        txt2 = str(self.__num2)
        txt3 = str(self.__num3)
        suma = txt1 + txt2 + txt3
        return suma
