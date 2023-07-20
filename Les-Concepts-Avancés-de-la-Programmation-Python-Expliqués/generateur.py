def generateur_carres(n):
    for i in range(n):
        yield i ** 2

# Utilisation du générateur
carres = generateur_carres(5)
for carre in carres:
    print(carre)
