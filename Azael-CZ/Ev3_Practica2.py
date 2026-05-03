class Mi_clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        suma = self.__num1 + self.__num2 + self.__num3
        return print(f"La suma los numeros es: {suma}")
    
    def mayor(self):
        if self.__num1 > self.__num2 and self.__num1 > self.__num3:
            print(f"El numero mayor es: {self.__num1}")
        elif self.__num2 > self.__num1 and self.__num2 > self.__num3:
            print(f"El numero mayor es: {self.__num2}")
        elif self.__num3 > self.__num2 and self.__num3 > self.__num1:
            print(f"El numero mayor es: {self.__num3}")

    def menor(self):
        if self.__num1 < self.__num2 and self.__num1 < self.__num3:
            print(f"El numero menor es: {self.__num1}")
        elif self.__num2 < self.__num1 and self.__num2 < self.__num3:
            print(f"El numero menor es: {self.__num2}")
        elif self.__num3 < self.__num2 and self.__num3 < self.__num1:
            print(f"El numero menor es: {self.__num3}") 

    def iguales(self):
        if self.__num1 == self.__num2 and self.__num1 == self.__num3 and self.__num2 == self.__num3:
            print("Los tres numeros son iguales")
        else:
            print("Los tres numeros no son iguales")

    def concatenar(self):
        num = str(self.__num1) + str(self.__num2) + str(self.__num3)
        print(num)

    def get_num1 (self):
        return self.__num1
    def set_num1 (self, num1):
        self.__num1 = num1

    def get_num2 (self):
        return self.__num2
    def set_num2 (self, num2):
        self.__num2 = num2

    def get_num3 (self):
        return self.__num3
    def set_num3 (self, num3):
        self.__num3 = num3