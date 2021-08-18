nombre_1 = nombre_2 = ""

while not (nombre_1.isdigit() and nombre_2.isdigit()):
    nombre_1 = input("Entrez un premier nombre : ")
    nombre_2 = input("Entrez un second nombre : ")
    if not (nombre_1.isdigit() and nombre_2.isdigit()):
        print("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition du nombre {nombre_1} avec le nombre {nombre_2} est égal à {int(nombre_1) + int(nombre_2)}")