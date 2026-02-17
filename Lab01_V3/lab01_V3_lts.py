import utils_V3_lts as utils

usr = input("Ingresa tu usuario: ")
carrera = input("Ingresa tu carrera: ")
print(f"\nBienvenido, {usr}!")

while True:

    utils.msg_menu()
    opcion=str(input("Ingresa opción: "))
 
    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"Suma: {utils.suma(a, b)}")
        print(f"Resta: {utils.resta(a, b)}")
        print(f"Multiplicación: {utils.multiplicacion(a, b)}")
        print(f"División: {utils.division(a, b)}")

    elif opcion == "2":
        distancia = float(input("Ingresa la distancia (m): "))
        tiempo = float(input("Ingresa el tiempo (s): "))
        print(f"Velocidad: {utils.velocidad(distancia, tiempo)} m/s")

    elif opcion == "3":
        precio = float(input("Ingresa el precio unitario: "))
        cantidad = int(input("Ingresa la cantidad: "))
        print(f"Pago total: {utils.pago_total(precio, cantidad)}")

    elif opcion == "4":
        numero = float(input("Ingresa un número para verificar si es positivo: "))
        print(utils.numeros_positivos(numero))  

    elif opcion == "5":
        nota = float(input("Ingresa una nota para verificar: "))
        print(utils.chequeo_nota(nota))
    else:
        utils.salir()