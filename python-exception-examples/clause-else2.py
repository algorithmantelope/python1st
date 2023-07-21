try:
    # Code qui peut générer une exception
    result = num1 / num2
except ZeroDivisionError:
    print("Erreur : Division par zéro")
else:
    print("Le résultat de la division est :", result)
