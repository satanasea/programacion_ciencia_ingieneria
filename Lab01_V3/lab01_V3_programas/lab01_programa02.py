#Solicite al usuario dos números reales y calcule:
#a. Suma
#b. Resta
#c. Multiplicación
#d. División

def suma (a, b):
    return a + b        

def resta (a, b):
    return a - b        

def multiplicacion (a, b):  
    return a * b

def division (a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    return a / b    

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print(f"Suma: {suma(a, b)}")
print(f"Resta: {resta(a, b)}")
print(f"Multiplicación: {multiplicacion(a, b)}")
print(f"División: {division(a, b)}")
