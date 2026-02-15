#---Calculadora de costo de transporte en tiempo real---

#DICCIONARIO DE BASE
vehiculos = {"[1]pickup": 6.00,"[2]gandola":7.00,"[3]mudanza":10.00}

#FUNCIONES
def iterar_dic(dic):
    for clave, valor in dic.items():
        print(clave, valor)

#MAIN
print("Los vehiculos disponibles son: ")
iterar_dic(vehiculos)
opcion = int(input("selecciona un vehiculo: "))

distancia = float(input("\nCuantos kilometros se recorrieron?: "))
costo_distancia = 1.50 * distancia

match opcion:
    case 1:
        base = vehiculos["[1]pickup"]
    case 2:
        base = vehiculos["[2]gandola"]
    case 3: 
        base = vehiculos["[3]mudanza"]

#Precio base(precio por vehiculo), costo por distancia(recargo por cada kilometro), precio total

print(f"\nEl precio base es ${base}, el costo por distancia es de ${costo_distancia}")
print(f"Por lo tanto el precio total es de: ${base + costo_distancia}\n")

