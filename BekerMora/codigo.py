print("soy beker")
class Videojuego:

    def __init__(self, nombre, genero, precio, plataforma, horas):
        self.__nombre = nombre
        self.__genero = genero
        self.__precio = precio
        self.__plataforma = plataforma
        self.__horas = horas

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_genero(self):
        return self.__genero

    def get_precio(self):
        return self.__precio

    def get_plataforma(self):
        return self.__plataforma

    def get_horas(self):
        return self.__horas

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_genero(self, genero):
        self.__genero = genero

    def set_precio(self, precio):
        self.__precio = precio

    def set_plataforma(self, plataforma):
        self.__plataforma = plataforma

    def set_horas(self, horas):
        self.__horas = horas

    # Método 1
    def descuento(self, cantidad):
        self.__precio = self.__precio - cantidad

    # Método 2
    def agregar_horas(self, tiempo):
        self.__horas = self.__horas + tiempo

    # Método info
    def info(self):
        print("Nombre:", self.__nombre)
        print("Genero:", self.__genero)
        print("Precio:", self.__precio)
        print("Plataforma:", self.__plataforma)
        print("Horas jugadas:", self.__horas)


# Prueba de la clase

juego1 = Videojuego("Minecraft", "Sandbox", 800, "PC", 20)

print("DATOS ORIGINALES")
juego1.info()

juego1.descuento(100)
juego1.agregar_horas(5)

print("\nDATOS ACTUALIZADOS")
juego1.info()
