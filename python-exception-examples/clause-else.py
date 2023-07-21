try:
    num1 = int(input("Entrez un nombre : "))
    num2 = int(input("Entrez un autre nombre : "))
except ValueError:
    print("Erreur : Entrez uniquement des nombres entiers.")
else:
    resultat = num1 / num2
    print("Le résultat de la division est :", resultat)
