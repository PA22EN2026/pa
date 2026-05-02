class Mi_clase:
    def __init__(self,num1,num2,num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
    
    #Getters y setters
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
    
    #Funcion suma
    def sumar(self):
        suma = self.__num1 + self.__num2 + self.__num3
        return print(f"La suma de los numeros es {suma}")
    
    #funcion mayor
    def mayor(self):
        if self.__num1 > self.__num2 and self.__num1 > self.__num3:
            return print(f"El numero mayor es {self.__num1}")
        elif self.__num2 > self.__num1 and self.__num2 > self.__num3:
            return print(f"El numero mayor es {self.__num2}")
        else:
            return print(f"El numero mayor es {self.__num3}")
    
    #funcion menor
    def menor(self):
        if self.__num1 < self.__num2 and self.__num1 < self.__num3:
            return print(f"El numero menor es {self.__num1}")
        elif self.__num2 < self.__num1 and self.__num2 < self.__num3:
            return print(f"El numero menor es {self.__num2}")
        else:
            return print(f"El numero menor es {self.__num3}")
        
    #funcion igual
    def igual(self):
        if self.__num1 == self.__num2 and self.__num1 == self.__num3:
            return print(True)
        else:
            return print(False)
        
    #funcion concatenar
    def concatenar(self):
        concat = str(self.__num1) + str(self.__num2) + str(self.__num3)
        return print(f"El resultado de los numero concatenados es {concat}")
    
#prueba de las funciones 
prueba = Mi_clase(3,5,15)
prueba.sumar()
prueba.mayor()
prueba.menor()
prueba.igual()
prueba.concatenar()
