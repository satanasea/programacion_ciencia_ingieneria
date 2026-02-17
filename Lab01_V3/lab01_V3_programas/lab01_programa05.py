#Escriba un programa que:
#a. Lea un número entero.
#b. Si el número es mayor que 0, muestre el mensaje:
#c. “El número es positivo”.

def numeros_positivos (numero):      
    if numero > 0:
        return "El número SI es positivo."
    else:
        return "El número NO es positivo."
    
numero = float(input("Ingresa un número para verificar si es positivo: "))
print(numeros_positivos(numero))


