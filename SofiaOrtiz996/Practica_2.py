class Mi_Clase:
    def __init__(self,num1,num2,num3):
        self.__num1=num1
        self.__num2=num2
        self.__num3=num3

    def sumar (self):
        return self.__num1+ self.__num2+self.__num3

    def mayor(self):
        if self.__num1>self.__num2:
            if self.__num1>self.__num3:
                num_mayor=self.__num1
            else:
                num_mayor=self.__num3
        else:
            if self.__num2>self.__num3:
                num_mayor=self.__num2
            else:
                num_mayor=self.__num3
    
    def menor(self):
        if self.__num1<self.__num2:
            if self.__num1<self.__num3:
                num_menor=self.__num1
            else:
                num_menor=self.__num3
        else:
            if self.__num2<self.__num3:
                num_menor=self.__num2
            else:
                num_menor=self.__num3
    
    def iguales(self):
        if self.__num1==self.__num2 and self.__num1==self.__num3 and self.__num2==self.__num3:
            print("Son iguales")
        else:
            print ("no son iguales")
    
    def concatenar (self):
        return str(self.__num1)+str(self.__num2)+str(self.__num3)