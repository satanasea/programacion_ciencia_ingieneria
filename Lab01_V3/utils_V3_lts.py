import sys


def msg_menu():
    print("\nMenu:")
    print("1.  Calculadora basica para numeros reales")
    print("2.  Calculadora de velocidad m/s")
    print("3.  Calculo de pago total")
    print("4.  Verificador de numeros positivos")
    print("5.  Verificaciòn de nota")
    print("0.  salir\n")

def salir():
    print("Saliendo del programa. ¡ Bye!")
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

def numeros_positivos (numero):      
    if numero > 0:
        return "El número SI es positivo."
    else:
        return "El número NO es positivo."

def chequeo_nota (nota):
    if nota >= 60:
        return "APROBADO"
    else:
        return "DESAPROBADO"  

