class ProprietePersonnalisee:
    def __init__(self, getter, setter=None, deleter=None):
        self.getter = getter
        self.setter = setter
        self.deleter = deleter

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.getter is not None:
            return self.getter(instance)
        raise AttributeError("Cette propriété n'a pas de méthode de 
lecture.")

    def __set__(self, instance, value):
        if self.setter is not None:
            self.setter(instance, value)
        else:
            raise AttributeError("Cette propriété n'a pas de méthode 
d'écriture.")

    def __delete__(self, instance):
        if self.deleter is not None:
            self.deleter(instance)
        else:
            raise AttributeError("Cette propriété n'a pas de méthode de 
suppression.")

class ExempleAvecPropriete:
    def __init__(self):
        self._x = 0

    @ProprietePersonnalisee
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("La valeur de x ne peut pas être négative.")
        self._x = value

    @x.deleter
    def x(self):
        self._x = 0

ex = ExempleAvecPropriete()
ex.x = 10
print(ex.x)  # Affiche : 10

ex.x = -5  # Lève une exception ValueError
