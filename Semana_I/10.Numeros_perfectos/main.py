# ---PROGRAMA QUE VERIFICA SI UN NUMERO ES PERFECTO---
# MAIN
n = int(input("Ingresa un numero: "))
divisores = []

for i in range(1, n):
    if n % i == 0:
        divisores.append(i)

suma_divisores = sum(divisores)
if suma_divisores == n:
    print(f"{n} es un numero perfecto.")
else:
    print(f"{n} no es un numero perfecto.")
