#---PROGRAMA PARA VALIDAR TRANSACCIONES ANTES DE REGISTRARLAS---

#MAIN
metodo = {"Pago movil": 0, "Tarjeta": 0}
counter_for = 1

print("Seleccione el metodo con el que va a pagar: ")
for n in metodo:
    print(f"[{counter_for}]{n}")
    counter_for = counter_for + 1
    

opcion = int(input(">>> "))

match opcion:
    case 1:
        while True:
            try:
                metodo["Pago movil"] = (input("Ingrese la clave de validacion: "))
                longitud = len(metodo["Pago movil"])
            
                if not metodo["Pago movil"].isdigit():
                    raise TypeError("La clave de validacion debe contener caracteres numericos")

                if len(metodo["Pago movil"]) != 8:
                    raise ValueError("La clave de validacion debe tener 8 caracteres")
            
                print("Clave de validacion verificada")
                break

            except(TypeError, ValueError) as e:
                print(f"Clave invalida {e}")
    case 2:
        while True:
            try:
                metodo["Tarjeta"] = (input("Ingrese la clave de validacion: "))
                longitud = len(metodo["Tarjeta"])
            
                if not metodo["Tarjeta"].isdigit():
                    raise TypeError("La clave de validacion debe contener caracteres numericos")

                if len(metodo["Tarjeta"]) != 16:
                    raise ValueError("La clave de validacion debe tener 16 caracteres")
            
                print("Clave de validacion verificada")
                break

            except(TypeError, ValueError) as e:
                print(f"Clave invalida {e}")
