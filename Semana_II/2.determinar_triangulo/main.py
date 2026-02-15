#---PROGRAMA QUE DETERMINA EL TIPO DE TRIANGULO---

print("Indique los tres angulos del triangulo: ")


a1, a2, a3 = int(input(">>> ")), int(input(">>> ")), int(input(">>> "))

if a1 + a2 + a3  == 180:
    if a1 == a2 and a2 == a3:
        print("Es un triangulo equilatero")
    
    elif (a1 == a2 and a1 != a3) or (a2 == a3 and a1 != a3) or (a1 == a3 and a2 != a3):
        print("Es un triangulo isosceles")
    
    elif a1 != a2 and a1 != a3 and a2 != a3:
        print("Es un triangulo escaleno")
    
    if a1 == 90 or a2 == 90 or a3 == 90:
        print("Tambien es un triangulo rectangulo")

else:
    print("No es un triangulo")


