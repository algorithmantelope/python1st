def valider_arguments(condition):
    def decorateur(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not condition(arg):
                    raise ValueError(f"La valeur {arg} ne respecte pas la 
condition de validation.")
            resultat = func(*args, **kwargs)
            return resultat
        return wrapper
    return decorateur

def est_positif(nombre):
    return nombre > 0

def est_pair(nombre):
    return nombre % 2 == 0

@valider_arguments(est_positif)
def diviser(a, b):
    return a / b

@valider_arguments(est_pair)
def multiplier(a, b):
    return a * b

try:
    resultat_division = diviser(10, 2)
    print(f"Résultat de la division : {resultat_division}")
except ValueError as e:
    print(e)

try:
    resultat_multiplication = multiplier(5, 3)
    print(f"Résultat de la multiplication : {resultat_multiplication}")
except ValueError as e:
    print(e)
