### Classe représentant une voiture

# Utilisation de PascalCase pour les noms de classe
class Voiture:
    """Classe représentant une voiture."""
    
    # Attribut de classe pour compter les voitures créées
    nombre_de_voitures = 0  

    def __init__(self, couleur: str, carburant: str, vitesse_max: int):
        """Initialise les attributs de la voiture."""
        self._couleur = couleur  
        self._carburant = carburant  
        self._vitesse_max = vitesse_max
        self._vitesse_actuelle = 0  # Ajout pour éviter l'erreur dans accelerer()
        Voiture.nombre_de_voitures += 1  

    # Getter et setter pour la couleur
    @property
    def couleur(self):
        return self._couleur
    
    @couleur.setter
    def couleur(self, nouvelle_couleur):
        if isinstance(nouvelle_couleur, str):
            self._couleur = nouvelle_couleur
        else:
            raise ValueError("La couleur doit être une chaîne de caractères.")

    def accelerer(self, vitesse: int):
        """Accélère sans dépasser la vitesse max."""
        if vitesse < 0:
            raise ValueError("La vitesse doit être positive.")
        self._vitesse_actuelle = min(self._vitesse_actuelle + vitesse, self._vitesse_max)
        print(f"La voiture accélère à {self._vitesse_actuelle} km/h.")

    def afficher_info(self):
        """Affiche les informations de la voiture."""
        print(f"Voiture {self._couleur}, {self._carburant}, vitesse max {self._vitesse_max} km/h.")

    @classmethod
    def get_nombre_de_voitures(cls):
        """Retourne le nombre total de voitures créées."""
        return cls.nombre_de_voitures

    @staticmethod
    def est_une_couleur_valide(couleur):
        """Vérifie si une couleur est valide."""
        return isinstance(couleur, str) and len(couleur) > 1


# Héritage : VoitureSport hérite de Voiture
class VoitureSport(Voiture):
    """Classe représentant une voiture sportive."""
    
    def __init__(self, couleur: str, carburant: str, vitesse_max: int, turbo: bool):
        """Initialise une voiture sportive avec l'option turbo."""
        super().__init__(couleur, carburant, vitesse_max)
        self._turbo = turbo  # Attribut privé

    def activer_turbo(self):
        """Active le turbo et augmente la vitesse max."""
        if self._turbo:
            self._vitesse_max += 50
            print("Turbo activé ! Nouvelle vitesse max :", self._vitesse_max)


### Exemple d'utilisation

# Création d'instances de Voiture
voiture1 = Voiture("Rouge", "Essence", 180)
voiture2 = Voiture("Bleue", "Diesel", 160)

# Affichage des informations
voiture1.afficher_info()
voiture2.afficher_info()

# Modification de la couleur
voiture1.couleur = "Noir"
print("Nouvelle couleur :", voiture1.couleur)

# Accélération
voiture1.accelerer(50)
voiture1.accelerer(100)  # Ne dépassera pas 180 km/h

# Vérification du nombre de voitures créées
print("Nombre total de voitures :", Voiture.get_nombre_de_voitures())

# Vérification d'une couleur valide avec la méthode statique
print("Couleur valide ?", Voiture.est_une_couleur_valide("Vert"))

# Création d'une voiture sportive
voiture_sport = VoitureSport("Jaune", "Électrique", 220, turbo=True)

# Affichage des infos de la voiture sportive
voiture_sport.afficher_info()

# Activation du turbo
voiture_sport.activer_turbo()
