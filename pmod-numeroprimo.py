# autor : Skop
# fecha: 12/11/2022
# acción : Elaborar un algoritmo que utilizando un procedimiento determine si un número ingresado es primo o no.

#Modulo especifico Nprimo
def Nprimo(num,prim):
    if(num % prim==0): # % = mod  
        print(f"El numero {num} es primo de {prim}")
    else:
        print(f"El numero {num} no es primo de {prim}")

# Programa Principal
numero=int(input("Ingrese un numero: "))
primo=int(input("Ingrese el siguiente numero: "))
Nprimo(numero,primo)   # llamar al procedimiento Nprimo