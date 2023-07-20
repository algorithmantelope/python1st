import time

def mesure_temps_execution(func):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()
        print(f"Temps d'exécution : {fin - debut} secondes")
        return resultat
    return wrapper

@mesure_temps_execution
def calcul_carre(n):
    return n ** 2

resultat = calcul_carre(5)
print(resultat) # Affiche le carré de 5 et le temps d'exécution
