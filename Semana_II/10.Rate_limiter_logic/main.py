#---Programa para saber cual es el maximo de solicitudes por segundo---
print("1. Usuario Premium\n2.Usuario Standard\n0.Servidor en mantenimiento")
opcion = int(input("Diga que tipo de usuario es >>> "))

status_mantenimiento = False

match opcion:
    case 0:
        status_mantenimiento = True
        print("Servidor en mantenimiento...No se permiten peticiones.")
    
    case 1:
        print("Se permiten hasta 1000 peticiones por segundo")
    
    case 2:
        print("Se permiten hasta 100 peticiones por segundo")


