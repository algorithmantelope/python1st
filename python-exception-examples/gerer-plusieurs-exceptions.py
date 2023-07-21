try:
    num1 = int(input("Entrez un nombre : "))
    num2 = int(input("Entrez un autre nombre : "))
    resultat = num1 / num2
    print("Le résultat de la division est :", resultat)
except (ValueError, ZeroDivisionError):
    print("Erreur : Entrez des nombres valides et assurez-vous que le 
dénominateur n'est pas zéro.")
