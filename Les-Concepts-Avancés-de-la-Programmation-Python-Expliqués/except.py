try:
    num = int(input("Entrez un nombre : "))
    result = 10 / num
except ValueError:
    print("Erreur : Entrée invalide, veuillez saisir un nombre")
except ZeroDivisionError:
    print("Erreur : Division par zéro")
