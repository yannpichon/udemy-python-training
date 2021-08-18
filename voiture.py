class Voiture:
    def __init__(self):
        self.essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d’essence")

    def roule(self, km):
        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return

        self.essence -= (km * 5) / 100

        if self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")
        
        self.afficher_reservoir()
    
    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")

voiture = Voiture()
voiture.afficher_reservoir()
voiture.roule(1000)
voiture.faire_le_plein()