# Aquesta classe reperesenta un error que succeeix quan intento
# afegir un producte que ja existeix
class ProducteJaExistent(Exception):
    pass

# Aquesta classe reperesenta un error que succeeix quan intento
# modificar un producte però no existeix
class ProducteNoExistent(Exception):
    pass
