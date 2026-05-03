class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3
    def mayor(self):
        if self.__num1 >= self.__num2 and self.__num1 >= self.__num3 :
            return self.__num1
        elif self.__num2 >= self.__num1 and self.__num2 >= self.__num3:
            return self.__num2
        else:
            return self.__num3
    def menor(self):
        return min(self.__num1, self.__num2, self.__num3)
    def iguales(self):
        if self.__num1 == self.__num2 == self.__num3:
            return True
        else: 
            return False
    def concatenar(self):
        return str(self.__num1) + str(self.__num2) + str(self.__num3)

prueba = Mi_Clase(10, 20, 50)
print(f"La suma es: {prueba.sumar()}")
print(f"El mayor es: {prueba.mayor()}")
print(f"El menor es: {prueba.menor()}")
print(f"¿Los números son iguales?: {prueba.iguales()}")
print(f"Concatenar números: {prueba.concatenar()}")