#---PROGRAMA QUE CALCULA LA DISTANCIA ENTRE DOS NODOS DE UN PLANO CARTESIANO---
import math
print("Ingrese las primeras coordenadas: ")
x1, y1 = float(input(">>> ")), float(input(">>> "))

print("Ingrese las segundas coordenadas: ")
x2, y2 = float(input(">>> ")), float(input(">>> "))

dx = x2 - x1
dy = y2 - y1

distancia = math.sqrt(dx**2 + dy**2)

rango_proximidad = distancia < 10

print(rango_proximidad)
