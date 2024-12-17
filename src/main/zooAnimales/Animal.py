class Animal:
    _totalAnimales = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1
        Animal._listado.append(self)

    @classmethod
    def totalPorTipo(cls):
        return (f"Mamiferos : {Mamifero.cantidadMamiferos()}\n"
                f"Aves : {Ave.cantidadAves()}\n"
                f"Reptiles : {Reptil.cantidadReptiles()}\n"
                f"Peces : {Pez.cantidadPeces()}\n"
                f"Anfibios : {Anfibio.cantidadAnfibios()}")

    def toString(self):
        return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, "
                f"habito en {self._habitat} y mi genero es {self._genero}")

    @classmethod
    def getListado(cls):
        return cls._listado