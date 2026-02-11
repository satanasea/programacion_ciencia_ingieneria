import sys

##def msg_goodbye(usr):
##    print(f"Goodbye, {usr}!")

def msg_menu():
    print("\nMenu:")
    print("1.  Calculadora basica para numeros reales")
    print("2.  Calculadora de velocidad m/s")
    print("3.  Calculo de pago total")
    print("0.  salir")

def salir():
    print("Saliendo del programa. ¡Hasta luego!")
    sys.exit()

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

def velocidad (distancia, tiempo):
    if tiempo == 0:
        print("Error: El tiempo no puede ser cero.")
        return None
    return distancia / tiempo

def pago_total (precio, cantidad):
    return precio * cantidad
