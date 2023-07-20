def calculer_remise(prix, pourcentage):
    remise = prix * pourcentage / 100
    prix_apres_remise = prix - remise
    return prix_apres_remise

prix_initial = float(input("Entrez le prix initial de l'article : "))
pourcentage_remise = float(input("Entrez le pourcentage de remise : "))

prix_final = calculer_remise(prix_initial, pourcentage_remise)

print(f"Le prix après remise est de {prix_final:.2f} euros.")
