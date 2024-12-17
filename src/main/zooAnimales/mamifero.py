class Mamifero(Animal):
    _listado = []
    leones = 0
    caballos = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.caballos += 1
        return cls(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Mamifero.leones += 1
        return cls(nombre, edad, "selva", genero, True, 4)

    def isPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas