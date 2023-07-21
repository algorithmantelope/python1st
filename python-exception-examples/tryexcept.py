try:
    num1 = int(input("Entrez un nombre : "))
    num2 = int(input("Entrez un autre nombre : "))
    resultat = num1 / num2
    print("Le résultat de la division est :", resultat)
except ZeroDivisionError:
    print("Erreur : Division par zéro n'est pas autorisée.")
except ValueError:
    print("Erreur : Entrez uniquement des nombres entiers.")
