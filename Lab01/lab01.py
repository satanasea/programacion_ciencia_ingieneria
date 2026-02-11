import utils

usr = input("Ingresa tu usuario: ")
carrera = input("Ingresa tu carrera: ")
print(f"\nBienvenido, {usr}!")

while True:

    utils.msg_menu()
    opcion=int(input("Ingresa opción: "))
 
    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"Suma: {utils.suma(a, b)}")
        print(f"Resta: {utils.resta(a, b)}")
        print(f"Multiplicación: {utils.multiplicacion(a, b)}")
        print(f"División: {utils.division(a, b)}")

    elif opcion == 2:
        d = float(input("Ingresa la distancia (m): "))
        t = float(input("Ingresa el tiempo (s): "))
        print(f"Velocidad: {utils.velocidad(d, t)} m/s")
    
    elif opcion == 3:
        precio = float(input("Ingresa el precio unitario: "))
        cantidad = int(input("Ingresa la cantidad: "))
        print(f"Pago total: {utils.pago_total(precio, cantidad)}")

    if opcion == 0:
        utils.salir()