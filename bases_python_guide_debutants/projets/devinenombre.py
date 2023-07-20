import random

nombre_a_deviner = random.randint(1, 100)
nombre_devine = False

while not nombre_devine:
    reponse = int(input("Devinez le nombre : "))

    if reponse < nombre_a_deviner:
        print("Plus grand !")
    elif reponse > nombre_a_deviner:
        print("Plus petit !")
    else:
        print("Bravo ! Vous avez deviné le nombre.")
        nombre_devine = True
