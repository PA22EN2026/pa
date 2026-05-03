class Mi_clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
    def sumar(self):
        suma = self.__num1 + self.__num2 + self.__num3
        print("Suma:", suma)
    def mayor(self):
        if self.__num1 >= self.__num2 and self.__num1 >= self.__num3:
            print("Mayor:", self.__num1)
        elif self.__num2 >= self.__num1 and self.__num2 >= self.__num3:
            print("Mayor:", self.__num2)
        else:
            print("Mayor:", self.__num3)
    def menor(self):
        if self.__num1 <= self.__num2 and self.__num1 <= self.__num3:
            print("Menor:", self.__num1)
        elif self.__num2 <= self.__num1 and self.__num2 <= self.__num3:
            print("Menor:", self.__num2)
        else:
            print("Menor:", self.__num3)
    def iguales(self):
        if self.__num1 == self.__num2 and self.__num2 == self.__num3:
            print("Son iguales")
        else:
            print("Son diferentes")
    def concatenar(self):
        concatenacion = str(self.__num1) + str(self.__num2) + str(self.__num3)
        print("Concatenación:", concatenacion)

objeto = Mi_clase(10,20,30)
