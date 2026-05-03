class Practica:
    def __init__(self, num1,num2,num3):
        self.__num1=num1
        self.__num2=num2
        self.__num3=num3
    
    def get_num1(self):
        return self.__num1

    def set_num1(self,num1):
        self.__num1=num1

    def get_num2(self):
        return self.__num2

    def set_num2(self,num2):
        self.__num2=num2

    def get_num3(self):
        return self.__num3

    def set_num3(self,num3):
        self.__num3=num3

    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3

    def mayor(self):
        if self.__num1 >= self.__num2 and self.__num1 >= self.__num3:
                return self.__num1
        elif self.__num2 >= self.__num1 and self.__num2 >= self.__num3:
            return self.__num2
        else:
            return self.__num3 

    def menor(self):
        if self.__num1 <= self.__num2 and self.__num1 <= self.__num3:
            return self.__num1
        elif self.__num2 <= self.__num1 and self.__num2 <= self.__num3:
            return self.__num2
        else:
            return self.__num3

    def iguales(self):
        return self.__num1 == self.__num2 == self.__num3

    def concatenar(self):
        return str(self.__num1)+ str(self.__num2)+ str(self.__num3)  


numeros=Practica(1,2,3)

numeros.set_num1(77)
numeros.set_num2(22)
numeros.set_num3(66)

print(f"La suma de los numeros es:",numeros.sumar())
print(f"El numero mayor es:", numeros.mayor())
print(f"El numero menor es:", numeros.menor())
print(f"Los numeros son iguales:",numeros.iguales())
print(f"Concatenacion de los numeros:",numeros.concatenar())




