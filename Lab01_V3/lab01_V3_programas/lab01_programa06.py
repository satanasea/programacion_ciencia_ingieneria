#Desarrolle un programa que:
#a. Pida la nota final de un estudiante.
#b. Si la nota es mayor o igual a 60, muestre:
#c. “Aprobado”.
#d. De lo contrario, muestre:
#e. “Reprobado”.

def chequeo_nota (nota):
    if nota >= 60:
        return "APROBADO"
    else:
        return "DESAPROBADO"

nota = float(input("Ingresa una nota para verificar: "))
print(chequeo_nota(nota))