#---CALCULADORA_GANANCIAS---

#MAIN

precio = float(input("En cuanto vendes los productos?: "))
costo = float(input("Cuanto te cuesta fabricar los productos?: "))

ganancia_neta = precio - costo

print(f"La ganancia neta de tu producto es: {ganancia_neta}")
