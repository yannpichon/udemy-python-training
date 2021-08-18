from random import randint

hp = hp_enemy = 50
potions = 3
skip_turn = False

while True:

    if skip_turn:
        print("Vous passez votre tour ...")
        skip_turn = False
    else:
        choice = input("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")

        if not choice in ["1","2"]:
            continue

        if choice == "1":
            damage = randint(5,10)
            hp_enemy -= damage
            print(f"Vous avez infligé {damage} points de dégats à l'ennemi")
        elif potions > 0:
            heal = randint(15,50)
            hp += heal
            potions -= 1
            skip_turn = True
            print(f"Vous récupérez {heal} points de vie ({potions} restante(s))")
        else:
            print("Vous n'avez plus de potion ...")
            continue

    if hp_enemy <= 0:
        print("Tu as gagné !")
        break

    damage_enemy = randint(5,15)
    hp -= damage_enemy
    print(f"L'ennemi vous a infligé {damage_enemy} points de dégats")

    if hp <= 0:
        print("Tu as perdu !")
        break
 
    print(f"Il vous reste {hp} points de vie.")
    print(f"Il reste {hp_enemy} points de vie à l'ennemie.")
    print("--------------------------------------")

print("Fin du jeu.")