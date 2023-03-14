import random

class Pokemon:
    def __init__(self, nom, type_pokemon):
        self.nom = nom
        self.type = type_pokemon
        self.points_de_vie = 100
        self.niveau = 1
        self.puissance_attaque = 0
        self.defense = 0

    def afficher_infos(self):
        print("Nom:", self.nom)
        print("Points de vie:", self.points_de_vie)
        print("Type:", self.type)
        print("Niveau:", self.niveau)
        print("Puissance d'attaque:", self.puissance_attaque)
        print("Défense:", self.defense)

class PokemonNormal(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "normal")
        self.points_de_vie = 90
        self.puissance_attaque = 20
        self.defense = 10

class PokemonFeu(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "feu")
        self.points_de_vie = 70
        self.puissance_attaque = 25
        self.defense = 5

class PokemonEau(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "eau")
        self.points_de_vie = 90
        self.puissance_attaque = 15
        self.defense = 15

class PokemonTerre(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "terre")
        self.points_de_vie = 70
        self.puissance_attaque = 5
        self.defense = 20

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def verifier_pokemon_en_vie(self):
        if self.pokemon1.points_de_vie <= 0:
            return self.pokemon2
        elif self.pokemon2.points_de_vie <= 0:
            return self.pokemon1
        else:
            return None

    def choisir_aleatoire_attaque(self):
        return random.randint(0, 1)

    def calculer_degats(self, attaquant, defenseur):
        if attaquant.type == "normal":
            multiplicateur = 1
        elif attaquant.type == "feu":
            if defenseur.type == "eau":
                multiplicateur = 0.5
            elif defenseur.type == "terre":
                multiplicateur = 2
            else:
                multiplicateur = 1
        elif attaquant.type == "eau":
            if defenseur.type == "feu":
                multiplicateur = 2
            elif defenseur.type == "terre":
                multiplicateur = 0.5
            else:
                multiplicateur = 1
        elif attaquant.type == "terre":
            if defenseur.type == "eau":
                multiplicateur = 2
            elif defenseur.type == "feu":
                multiplicateur = 0.5
            else:
                multiplicateur = 1

        degats = attaquant.puissance_attaque * multiplicateur
        return degats

pikachu = PokemonEau("Pikachu")
bulbasaur = PokemonTerre("Bulbasaur")

pikachu.afficher_infos()
bulbasaur.afficher_infos()

combat = Combat(pikachu, bulbasaur)

