# autor : Skop
# fecha: 9/11/2022
# acción : Elaborar un algoritmo que utilizando un procedimiento halle las suma de 2 números ingresados.

# Modulo especifico Suma
def Suma(num1, num2):
    sumat=num1+num2
    print(f"La suma es:",sumat)


# Programa Principal
Numero1=int(input("ingrese el primer numero: "))
Numero2=int(input("ingrese el segundo numero: "))
Suma(Numero1, Numero2)   # llamar al procedimiento

