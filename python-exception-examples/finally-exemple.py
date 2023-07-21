try:
    # Code qui peut générer une exception
    file = open("fichier.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé")
else:
    print("Contenu du fichier :", content)
finally:
    file.close()
    print("Fermeture du fichier")
