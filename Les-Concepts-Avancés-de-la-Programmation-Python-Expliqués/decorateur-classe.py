class DecorateurDeClasse:
    def __init__(self, classe):
        self.classe = classe

    def __call__(self, *args, **kwargs):
        instance = self.classe(*args, **kwargs)
        instance.__dict__.update(self.__dict__)
        return instance

@DecorateurDeClasse
class ExempleDeClasse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print(f"Valeur de x : {self.x}")
        print(f"Valeur de y : {self.y}")

ex = ExempleDeClasse(10, 20)
ex.afficher()
