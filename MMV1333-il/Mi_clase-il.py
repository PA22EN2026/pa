class Mi_clase:
    def __init__(self,num1,num2,num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    @property
    def num1(self):
        return self.__num1
    
    @num1.setter
    def num1(self,nuevo):
        self.__num1 = nuevo

    @property
    def num2(self):
        return self.__num2
    
    @num2.setter
    def num2(self,nuevo):
        self.__num2 = nuevo

    @property
    def num3(self):
        return self.__num3
    
    @num3.setter
    def num3(self,nuevo):
        self.__num3 = nuevo

