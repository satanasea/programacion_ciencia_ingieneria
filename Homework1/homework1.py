import utils

name="Nao"
age=17
height=1.60

print("\nIngresa 2 numeros para calcular su suma resta division multiplicacion: ")   
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print(f"Suma: {utils.suma(a, b)}")
print(f"Resta: {utils.resta(a, b)}")
print(f"Multiplicación: {utils.multiplicacion(a, b)}")
print(f"División: {utils.division(a, b)}")


print("\nIngresa un numero para verificar si es mayor a 10 o es igual a 5:")
numero=float(input("Ingresa un número: "))
if numero > 10:
    print("El número es mayor que 10.")
elif numero == 5:
    print("El número es igual a 5.")