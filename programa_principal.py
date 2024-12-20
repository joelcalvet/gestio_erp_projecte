from gestio_erp import Client, Comanda, Producte

# Crear clients
anna = Client(1, "Anna", "anna@example.com")
pere = Client(2, "Pere", "pere@example.com")
joan = Client(3, "Joan", "joan@example.com")

# Crear productes amb els seus noms
bicicleta = Producte("bicicleta")
casc = Producte("casc")
guants = Producte("guants")
maillot = Producte("maillot")
roda = Producte("roda")
pantalons = Producte("pantalons")

# Crear comandes amb la seva quantitat
comanda1 = Comanda(101)
comanda1.afegir_producte(bicicleta, 1)
comanda1.afegir_producte(casc, 2)

comanda2 = Comanda(102)
comanda2.afegir_producte(guants, 1)

comanda3 = Comanda(103)
comanda3.afegir_producte(maillot, 1)
comanda3.afegir_producte(roda, 2)

comanda4 = Comanda(104)
comanda4.afegir_producte(guants, 2)

# Assignar comandes a clients
anna.afegir_comanda(comanda1)
anna.afegir_comanda(comanda2)

pere.afegir_comanda(comanda3)
pere.afegir_comanda(comanda4)

# Mostrar resultats dels clients elegits recorrent un bucle
print("COMANDES DELS CLIENTS")
for client in [anna, pere, joan]:
    print(f"Comandes del client {client.nom}: {len(client.consultar_comandes())}")
    for comanda in client.consultar_comandes():
        print(comanda)

# Errors
try:
    comanda1.afegir_producte(bicicleta, 1)
except Exception as e:
    print(e)

try:
    comanda1.modificar_quantitat(Producte("patinet"), 2)
except Exception as e:
    print(e)

# Modificar estat i quantitats
comanda1.modificar_estat("Enviada")
comanda1.modificar_quantitat(bicicleta, 1)
comanda1.modificar_quantitat(casc, 2)
comanda1.afegir_producte(pantalons, 1)

# Mostro les comandes dels clients després de modificar-les
print("\nCOMANDES DELS CLIENTS (ACTUALITZADES)")
for client in [anna, pere, joan]:
    print(f"Comandes del client {client.nom}: {len(client.consultar_comandes())}")
    for comanda in client.consultar_comandes():
        print(comanda)
