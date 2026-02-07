#---Programa que indica a que servidor pertenece un ID---

N = int(input("Ingresa el ID unico: "))

if N % 2 == 0:
    print("Servidor A")
else:
    print("Servidor B")
