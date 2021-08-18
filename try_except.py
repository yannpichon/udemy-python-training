file = input("Entrez un fichier à ouvrir : ")

try:
    f = open(file,'r')
    print(f.read())
except FileNotFoundError as e:
    print(f"Fichier introuvable : {e}")
except UnicodeDecodeError as e:
    print(f"Le fichier ne peut pas être ouvert : {e}")
else:
    f.close()