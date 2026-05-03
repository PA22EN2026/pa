class Mi_Clase:
    def __init__(self,numero1,numero2,numero3):
        self.__num1= numero1
        self.__num2= numero2
        self.__num3= numero3
    def sumar(self):
        return self.__num1+self.__num2+self.__num3
    
    def mayor(self):
        el_mayor=self.__num1
        if self.__num2> el_mayor:
            el_mayor=self.__num2
        if self>el_mayor:
            el_mayor=self.__num3
        return el_mayor
    
    def menor(self):
        el_menor=self.__num1
        if self.__num2> el_menor:
            el_menor=self.__num2
        if self>el_menor:
            el_menor=self.__num3
        return el_menor
    
        
        