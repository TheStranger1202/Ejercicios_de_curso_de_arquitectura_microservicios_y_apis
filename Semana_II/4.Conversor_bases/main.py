#---ESTE PROGRAMA CONVIERTE DE DECIMAL A BINARIO Y HEXADECIMAL

#FUNCIONES
def conversor(decimal, base):
    string_conversor = "0123456789ABCDEF"
    resultado = ""
    
    if decimal == 0:
        return "0"

    while decimal > 0:
        indice = decimal % base
        resultado = string_conversor[indice] + resultado
        decimal = decimal // base
    return resultado

#MAIN
decimal = int(input("Ingresa el numero decimal que vas a convertir>>> "))

binario = conversor(decimal,2)
hexadecimal = conversor(decimal, 16)

print(f"La conversion a binario es: {binario}")
print(f"La conversion a hexadecimal es: {hexadecimal}")

