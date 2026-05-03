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
     if self._num1 >= self.num2 and self.num1 >= self._num3:
            return self.__num1
        elif self._num2 >= self.num1 and self.num2 >= self._num3:
            return self.__num2
        else:
            return self.__num3
