class Numeros:
      def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

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
        return self.__num1 == self.__num2 and self.__num2 == self.__num3  
      def concatenar(self):
        return str(self.__num1) + str(self.__num2) + str(self.__num3)

obj = Numeros(5, 9, 3)

print("Suma:", obj.sumar())
print("Mayor:", obj.mayor())
print("Menor:", obj.menor())
print("Iguales:", obj.iguales())
print("Concatenar:", obj.concatenar())