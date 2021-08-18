from random import randint

nombre_mystere = randint(0,100)
essais_restants = 5

print("*** Le jeu du nombre mystère ***")
while essais_restants > 0:
    print(f"Il te reste {essais_restants} essai(s)")
    
    reponse = input("Devine le nombre : ")

    if not reponse.isdigit():
        print("Veuillez entrer un nombre valide")
        continue

    reponse = int(reponse)

    if reponse > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {reponse}")
        essais_restants-=1
    elif reponse < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {reponse}")
        essais_restants-=1
    else:
        break

if essais_restants == 0:
    print(f"Dommage ! Le nombre mystère était {nombre_mystere}")
else:
    print(f"Bravo ! Le nombre mystère était bien {nombre_mystere} !")
    print(f"Tu as trouvé le nombre en {6-essais_restants} essai(s)")

print(f"Fin du jeu.")