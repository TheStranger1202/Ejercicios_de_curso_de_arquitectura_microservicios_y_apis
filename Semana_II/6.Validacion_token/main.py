#---ESTE PROGRAMA VALIDA UN TOKEN EN BASE A UNAS REGLAS---
"""Las reglas son: 
1-Tiene mas de 12 caracteres
2-contiene al menos un numero
3-no empieza con la palabra "TEST" 
"""
#IMPORTACIONES
import os

#FUNCIONES
def limpiar_pantalla():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

#MAIN
while True:
    limpiar_pantalla()
    token = input("Ingrese el token de seguridad>>> ")
    if len(token) > 12 and any(x.isdigit() for x in token) and not token.upper().startswith("TEST"):
        print("El token es valido")
        break 
    else: 
        print("Token invalido. Debes seguir las reglas: ")
        print("Debe contener mas de 12 caracteres")
        print("Debe contener al menos un numero")
        print("NO debe empezar con la palabra TEST")
        input()
print("programa finalizado con exito")
input()
limpiar_pantalla()
