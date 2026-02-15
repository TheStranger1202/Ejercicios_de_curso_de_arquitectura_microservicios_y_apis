#---ESTE PROGRAMA DEVUELVE EL TIEMPO DE ESPERA PARA REINTENTAR UNA LLAMADA DE MICROSERVICIO---

n = int(input("Cuantos intentos van?: "))
counter = 0
a, b = 0, 1
while counter < n:
    print(a)
    a,b = b, a + b
    counter += 1

