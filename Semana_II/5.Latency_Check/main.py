#---PROGRAMA PARA SABER SI UN UMBRAL DE LATENCIA SE SOBREPASA---

string = input("Ingresa las latencias que obtuviste, separalas con una coma:\n")
umbral_critico = float(input("Cual es el umbral critico de latencia para tu tarea?: "))

latencias = [float(x.strip()) for x in string.split(",")]

promedio = sum(latencias) / len(latencias)

critical_state = False

if promedio > umbral_critico:
    critical_state = True

for n in latencias:
    if n >= 3 * promedio:
        critical_state = True

print(f"Critical latency state: {critical_state}")
