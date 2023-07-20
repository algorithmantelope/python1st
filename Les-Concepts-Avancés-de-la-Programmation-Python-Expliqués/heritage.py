class ChienDeCourse(Chien):
    def __init__(self, nom, age, vitesse):
        super().__init__(nom, age)
        self.vitesse = vitesse

    def courir(self):
        return f"{self.nom} court à une vitesse de {self.vitesse} km/h!"
