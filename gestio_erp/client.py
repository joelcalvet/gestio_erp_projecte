from gestio_erp.comanda import Comanda

class Client:
    # Aquesta funció s'executa quan creem un nou client i inicialitza les seves dades
    def __init__(self, id_client, nom, correu):
        self.id_client = id_client
        self.nom = nom
        self.correu = correu
        self.comandes = []

    # Afegeix una nova comanda a la llista de comandes del client
    # Comprova que la classe de l'objecte que ens passen sigui realment una comanda
    def afegir_comanda(self, comanda):
        if not isinstance(comanda, Comanda):
            raise TypeError("Només es poden afegir objectes de tipus Comanda.")
        self.comandes.append(comanda)

    # Ens retorna la llista de comandes del client
    def consultar_comandes(self):
        return self.comandes

    # Aquesta funció ens diu com volem que es mostri un client quan l'imprimim
    def __str__(self):
        return f"Client: {self.nom}, Correu: {self.correu}, Comandes: {len(self.comandes)}"
