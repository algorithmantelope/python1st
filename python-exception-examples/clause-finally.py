try:
    fichier = open("mon_fichier.txt", "r")
    contenu = fichier.read()
    print("Contenu du fichier :", contenu)
except FileNotFoundError:
    print("Erreur : Le fichier n'a pas été trouvé.")
finally:
    fichier.close()
    print("Fermeture du fichier.")
