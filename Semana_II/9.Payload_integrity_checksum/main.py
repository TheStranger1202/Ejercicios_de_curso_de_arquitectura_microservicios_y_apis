#---PROGRAMA PARA SABER SI UN MENSAJE FUE ALTERADO---

string = input("Ingrese el mensaje: ")
valor_numerico = 0

for char in string:
    valor_numerico = valor_numerico + ord(char)

if valor_numerico % 2 == 0:
    print("Paquete integro")

else:
    print("Paquete chimbo")
