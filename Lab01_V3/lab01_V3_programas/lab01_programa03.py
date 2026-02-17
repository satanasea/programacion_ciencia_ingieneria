#Un laboratorio de física desea calcular la velocidad de
#un objeto. La fórmula es:
#El programa debe:
#a. Solicitar la distancia (en metros)
#b. Solicitar el tiempo (en segundos)
#c. Calcular la velocidad
#d. Mostrar el resultado

def velocidad (distancia, tiempo):
    if tiempo == 0:
        print("Error: El tiempo no puede ser cero.")
        return None
    return distancia / tiempo

distancia = float(input("Ingresa la distancia (m): "))
tiempo = float(input("Ingresa el tiempo (s): "))
print(f"Velocidad: {velocidad(distancia, tiempo)} m/s")
