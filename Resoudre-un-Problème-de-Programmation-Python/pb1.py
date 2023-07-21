def somme_elements_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

# Exemple d'utilisation de la fonction
ma_liste = [1, 2, 3, 4, 5]
resultat = somme_elements_liste(ma_liste)
print("La somme des éléments de la liste est :", resultat)
