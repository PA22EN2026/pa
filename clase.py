class Capibara:
    def __init__(self, nombre, edad, peso, color, habitat):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__color = color
        self.__habitat = habitat
    

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso

    def get_color(self):
        return self.__color

    def get_habitat(self):
        return self.__habitat
    
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad

    def set_peso(self, peso):
        if peso > 0:
            self.__peso = peso

    def set_color(self, color):
        self.__color = color

    def set_habitat(self, habitat):
        self.__habitat = habitat

    def comer(self, cantidad):
        self.__peso += cantidad
        print(f"{self.__nombre} comió y ahora pesa {self.__peso} kg")

    def crecer(self):
        self.__edad += 1
        print(f"{self.__nombre} ahora tiene {self.__edad} años")
    
    def info(self):
        print("----- CAPIBARA -----")
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Peso: {self.__peso} kg")
        print(f"Color: {self.__color}")
        print(f"Hábitat: {self.__habitat}")

capi1 = Capibara("Capi", 2, 35, "cafe", "rio")
capi1.info()

print("\n--- GETTERS ---")
print("Nombre:", capi1.get_nombre())
print("Edad:", capi1.get_edad())
print("Peso:", capi1.get_peso())
print("Color:", capi1.get_color())
print("Habitat:", capi1.get_habitat())

print("\n--- SETTERS ---")
capi1.set_nombre("Capibara Max")
capi1.set_edad(3)
capi1.set_peso(40)
capi1.set_color("marron")
capi1.set_habitat("laguna")

capi1.info()

print("\n--- METODOS ---")
capi1.comer(3)
capi1.crecer()

print("\n--- FINAL ---")
capi1.info()



    



