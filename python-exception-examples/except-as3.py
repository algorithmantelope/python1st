def convertir_en_entier(chaine):
    try:
        nombre = int(chaine)
        print(f"La conversion de '{chaine}' en entier a réussi.")
    except ValueError as e:
        print(f"Erreur : {e}")
        print(f"La conversion de '{chaine}' en entier a échoué.")
        nombre = None
    return nombre

entree_utilisateur = input("Entrez un nombre entier : ")
resultat = convertir_en_entier(entree_utilisateur)

if resultat is not None:
    print(f"Le résultat de la conversion est : {resultat}")
