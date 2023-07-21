class MonException(Exception):
    pass

def verifier_nombre(n):
    if n < 0:
        raise MonException("Le nombre ne peut pas être négatif.")
    return n

try:
    num = int(input("Entrez un nombre positif : "))
    resultat = verifier_nombre(num)
    print("Le nombre est :", resultat)
except MonException as e:
    print("Erreur :", e)
