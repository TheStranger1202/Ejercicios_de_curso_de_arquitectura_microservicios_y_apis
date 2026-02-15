#---UNA CALCULADORA CON DOS FUNCIONES EXTRA---
#Importaciones
import os

#FUNCIONES
def pedir_numero():
    a = int(input(">> "))
    return a

def pedir_opcion():
    a = int(input(">>> "))
    return a

def limpiar_pantalla():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def sumar(a,b):
    
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a // b

def fibonacci(c):
    counter = 0
    a, b = 0, 1
    while counter < c:
        print(a)
        a, b = b, a + b
        counter += 1

def conversion_bases(c):
    print(f"La conversion del resultado a binario es: {bin(c)}")
    print(f"La conversion del resultado a hexadecimal es: {hex(c)}")
#MAIN
while True:
    limpiar_pantalla()
    print("CALCULADORA ESPECIAL")
    print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n0.Salir")
    opcion = pedir_opcion()
    
    if opcion == 0:
        break

    if opcion in (1,2,3,4):
            a, b = pedir_numero(), pedir_numero()

    match opcion:
        case 1: resultado = sumar(a,b)
        case 2: resultado = restar(a,b)
        case 3: resultado = multiplicar(a,b)
        case 4: resultado = dividir(a,b)

    print(f"El resultado es: {resultado}")
    print("Que quieres hacer con el resultado obtenido?")
    print("1.Serie Fibonacci\n2.Conversion de bases\n0.Salir del programa")
    sub_opcion = pedir_opcion()
    
    if opcion == 0:
        break

    match sub_opcion:
        case 1:
            fibonacci(resultado)
            input()
            limpiar_pantalla()
        case 2:
            conversion_bases(resultado)
            input()
            limpiar_pantalla()
    
    print("1.Volver al inicio\n2.Terminar programa")
    final_opcion = pedir_opcion()
    if final_opcion == 2:
        break
   
limpiar_pantalla()
