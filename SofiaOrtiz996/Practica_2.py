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
        return num_mayor
    
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
        return num_menor
    
    def iguales(self):
        if self.__num1==self.__num2 and self.__num1==self.__num3 and self.__num2==self.__num3:
            print("Son iguales")
        else:
            print ("no son iguales")
    
    def concatenar (self):
        return str(self.__num1)+str(self.__num2)+str(self.__num3)

numeros=Mi_Clase(10,10,10)

print("***Menu***")
print("1.-Sumar/2.-mayor/3.- Menor/4.-Iguales/5.-concatenar")
opcion= int(input("Que opcion elige"))
if opcion==1:
    print("Suma:", numeros.sumar())
elif opcion ==2:
    print("Mayor:", numeros.mayor())
elif opcion==3:
    print("Menor:", numeros.menor())
elif opcion==4:
    print("¿Son iguales?:", numeros.iguales())
elif opcion==5:
    print("Concatenación:", numeros.concatenar())