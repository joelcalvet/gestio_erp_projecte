class Producte:
    # S'utilitza per inicialitzar els atributs de l'objecte.
    def __init__(self, nom):
        self.nom = nom

    # Imprimeix una representació en cadena de l'objecte.
    def __str__(self):
        return f"Producte: {self.nom}"
