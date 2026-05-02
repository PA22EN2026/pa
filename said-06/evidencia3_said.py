class Miclase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3

    def mayor(self):
        if self.__num1 > self.__num2 and self.__num1 > self.__num3:
            return self.__num1
        elif self.__num2 > self.__num1 and self.__num2 > self.__num3:
            return self.__num2
        else:
            return self.__num3

    def menor(self):
        if self.__num1 < self.__num2 and self.__num1 < self.__num3:
            return self.__num1
        elif self.__num2 < self.__num1 and self.__num2 < self.__num3:
            return self.__num2
        else:
            return self.__num3

    def iguales(self):
        if self.__num1 == self.__num2 == self.__num3:
            return True
        else:
            return False

    def concatenar(self):
        return str(self.__num1) + str(self.__num2) + str(self.__num3)


    def get_num1(self):
        return self.__num1

    def set_num1(self, numero):
        self.__num1 = numero

    def get_num2(self):
        return self.__num2

    def set_num2(self, numero):
        self.__num2 = numero

    def get_num3(self):
        return self.__num3

    def set_num3(self, numero):
        self.__num3 = numero



valores = Miclase(10, 8, 8)

print(f"La suma es: ", valores.sumar())
print(f"El numero mayor es: ", valores.mayor())
print(f"El numero menor es: ", valores.menor())
print(f"Los numeros son iguales? ", valores.iguales())  
print(f"La concatenacion es: ", valores.concatenar())

