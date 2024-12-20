from gestio_erp.producte import Producte
from gestio_erp.errors import ProducteJaExistent, ProducteNoExistent

class Comanda:
    # Llista dels estats possibles per a una comanda
    ESTATS = ["Pendent", "Enviada"]

    def __init__(self, id_comanda):
        # Identificador únic de cada comanda
        self.id_comanda = id_comanda
        # Un diccionari per guardar els productes i les seves quantitats
        self.productes = {}
        # Inicialment les comandes està pendents
        self.estat = self.ESTATS[0]

    def afegir_producte(self, producte, quantitat=1):
        # Comprovo que el que l'objecte que ens passen sigui de la classe Producte
        if not isinstance(producte, Producte):
            raise TypeError("Només es poden afegir objectes de tipus Producte.")
        # Comprovo si el producte ja està a la comanda
        if producte.nom in self.productes:
            raise ProducteJaExistent(f"El producte {producte.nom} ja existeix a la comanda.")
        # Afegeixo el producte a la comanda amb la quantitat
        self.productes[producte.nom] = quantitat

    def modificar_quantitat(self, producte, quantitat):
        # Comprovo si el producte ja està a la comanda
        if producte.nom not in self.productes:
            raise ProducteNoExistent(f"El producte {producte.nom} no existeix a la comanda.")
        # Actualitzo la quantitat del producte
        self.productes[producte.nom] += quantitat

    def modificar_estat(self, nou_estat):
        # Comprovem si el nou estat és vàlid
        if nou_estat not in self.ESTATS:
            raise ValueError("Estat no vàlid.")
        # Canviem l'estat de la comanda
        self.estat = nou_estat

    def consultar_resum(self):
        # Creo una cadena amb tots els productes i les seves quantitats
        resum = ", ".join(f"{prod}: {q}" for prod, q in self.productes.items())
        # Retornem un resum de la comanda amb el seu identificador, estat i llista de productes
        return f"Comanda {self.id_comanda} [{self.estat}]: {resum}"

    def __str__(self):
        # Quan imprimeixo una comanda, mostro el resum
        return self.consultar_resum()
