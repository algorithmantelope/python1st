try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Erreur : Fichier non trouvé")
finally:
    file.close()
