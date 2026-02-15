#---PROGRAMA QUE SIMULA UN HEALT CHECK---
#MAIN

latencia = float(input("Latencia en ms>>> "))
uso_cpu = float(input("Uso CPU>>> "))
estado_db = input("La base de datos esta conectada?: ")

if latencia < 200 and uso_cpu < 80 and estado_db.lower() == "si":
    print(True)
else:
    print(False)
