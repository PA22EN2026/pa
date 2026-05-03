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
        elif self.__num2 > self.__num2 and self.__num1 > self.__num3:
            print(f"El numero mayor es: {self.__num2}")
        elif self.__num3 > self.__num2 and self.__num1 > self.__num1:
            print(f"El numero mayor es: {self.__num3}")