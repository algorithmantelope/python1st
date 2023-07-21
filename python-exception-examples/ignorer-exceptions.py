def division(a, b):
    try:
        resultat = a / b
        print(f"Le résultat de la division {a} / {b} est : {resultat}")
    except ZeroDivisionError:
        pass
        # Nous ignorons l'exception et continuons l'exécution

# Exemples d'utilisation de la fonction division
division(10, 2)
division(5, 0)  # Cette division par zéro lève une exception, mais elle 
est ignorée
division(8, 4)
