def diviser(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError as e:
        print(f"Erreur : {e}")
        print("Impossible de diviser par zéro.")
        resultat = None
    return resultat

nombre1 = 10
nombre2 = 0

res = diviser(nombre1, nombre2)

if res is not None:
    print(f"Le résultat de la division est : {res}")
