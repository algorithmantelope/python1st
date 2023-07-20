import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits
    mot_de_passe = ''.join(random.choice(caracteres) for i in 
range(longueur))
    return mot_de_passe

longueur_mot_de_passe = int(input("Entrez la longueur du mot de passe souhaitée : "))
mot_de_passe_genere = generer_mot_de_passe(longueur_mot_de_passe)

print(f"Votre mot de passe généré est : {mot_de_passe_genere}")
