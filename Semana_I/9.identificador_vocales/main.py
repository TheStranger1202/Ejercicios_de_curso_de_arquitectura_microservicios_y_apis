#---PROGRAMA PARA IDENTIFICAR UNA VOCAL---
#MAIN

vocals = ["A","E","I","O","U"]

char = input("Ingresa un caracter: ")

if char.upper() in vocals:
    print("Es una vocal")
else:
    print("No es una vocal")
