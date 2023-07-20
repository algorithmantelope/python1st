def generateur_nombres_impairs(n):
    i = 1
    while i <= n:
        yield i
        i += 2

# Utilisation de next() pour obtenir les éléments suivants
nombres_impairs = generateur_nombres_impairs(5)
print(next(nombres_impairs))  # Affiche 1
print(next(nombres_impairs))  # Affiche 3
print(next(nombres_impairs))  # Affiche 5
