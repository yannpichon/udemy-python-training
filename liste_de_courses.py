from pathlib import Path
import json

choix = ""
menu = """Choisissez parmi les 5 options suivantes :
1. Ajouter un élément à la liste de courses
2. Retirer un élément de la liste de courses
3. Afficher les éléments de la liste de courses
4. Vider la liste de courses
5. Quitter le programme """

file_liste = Path.cwd() / "liste.json"

if file_liste.is_file():
    with open(file_liste) as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []

while not (choix == 5):
    print(menu)
    choix = input("Votre choix : ")

    if (choix == "1"):
        article = input("Entrez le nom d'un article à ajouter dans la liste de courses : ")
        if article in liste_de_courses:
            print(f"L'article {article} est déjà présent dans la liste.")
        else:
            liste_de_courses.append(article)
            print(f"L'article {article} a bien été ajouté à la liste.")
    elif (choix == "2"):
        article = input("Entrez le nom d'un article à retirer de la liste de courses : ")
        if article in liste_de_courses:
            liste_de_courses.remove(article)             
            print(f"L'article {article} a bien été supprimé de la liste.")
        else:
            print(f"L'article {article} n'est pas dans la liste.")
    elif (choix == "3"):
        numero_article = 1
        if not liste_de_courses == []:
            print(f"Voici le contenu de votre liste : ")
            for article in liste_de_courses:
                print(f"{numero_article}. {article}")
                numero_article += 1
        else: 
            print('Votre liste ne contient aucun élément.')
    elif (choix == "4"):
        if not liste_de_courses == []:
            liste_de_courses = []
            print("La liste a été vidée de son contenu.")
        else:
            print('Votre liste ne contient aucun élément.')
    elif (choix == "5"):
        print("A bientôt !")
        with open(file_liste,"w") as f:
            json.dump(liste_de_courses,f)
        break
    else:
        print("Choix incorrect.")