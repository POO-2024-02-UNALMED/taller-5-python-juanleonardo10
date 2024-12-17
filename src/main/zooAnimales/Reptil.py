class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @staticmethod
    def cantidadReptiles():
        return len(Reptil._listado)

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil.iguanas += 1
        return cls(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes += 1
        return cls(nombre, edad, "jungla", genero, "gris", 2)

    def getLargoCola(self):
        return self._largoCola