class ValeurNegativeError(Exception):
    def __init__(self, message, valeur):
        super().__init__(message)
        self.valeur = valeur

def diviser(a, b):
    if b < 0:
        raise ValeurNegativeError("La valeur de b ne peut pas être 
négative", b)
    return a / b

try:
    resultat = diviser(10, -2)
except ValeurNegativeError as e:
    print(f"Erreur : {e}")
    print(f"Valeur incorrecte : {e.valeur}")
else:
    print("Le résultat de la division est :", resultat)
