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
        if self.__num3>el_mayor:
            el_mayor=self.__num3
        return el_mayor
    
    def menor(self):
        el_menor=self.__num1
        if self.__num2< el_menor:
            el_menor=self.__num2
        if self.__num3<el_menor:
            el_menor=self.__num3
        return el_menor
    
    def iguales(self):
        return(self.__num1==self.__num2 or self.__num1==self.__num3 or self.__num2 == self.__num3)
    
    def concatenar(self):
        return f"{self.__num1}{self.__num2}{self.__num3}"
    
numero1=int(input("Ingrese el numero 1: "))
numero2=int(input("Ingrese el numero 2: "))
numero3=int(input("Ingrese el numero 3: "))

Uso_deMIobjeto=Mi_Clase(numero1,numero2,numero3)
print("⊱──────────────────────────────────────────⊰")
print("           ✧ I M P R E S I O N ✧           ")
print("⊱──────────────────────────────────────────⊰")
print(f" ⫸  Suma total: {Uso_deMIobjeto.sumar()}")
print(f" ⫸  Numero mayor: {Uso_deMIobjeto.mayor()}")
print(f" ⫸  Numero menor: {Uso_deMIobjeto.menor()}")
print(f" ⫸  ¿Hay numero iguales?: {Uso_deMIobjeto.iguales()}")
print(f" ⫸  Concatenacion: {Uso_deMIobjeto.concatenar()}")
print("⊱──────────────────────────────────────────⊰")
print("                ⊹ ⊱ ✿ ⊰ ⊹                ")

    
        
        