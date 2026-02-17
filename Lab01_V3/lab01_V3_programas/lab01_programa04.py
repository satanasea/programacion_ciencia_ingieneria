#Crear un programa que:
#a. Solicite el precio de un producto (con decimales).
#b. Solicite la cantidad comprada.
#c. Convierta los datos al tipo correcto.
#d. Calcule el total a pagar.
#e. Muestre el resultado en pantalla.

def pago_total (precio, cantidad):
    return precio * cantidad

precio = float(input("Ingresa el precio unitario: "))
cantidad = int(input("Ingresa la cantidad: "))
print(f"Pago total: {pago_total(precio, cantidad)}")