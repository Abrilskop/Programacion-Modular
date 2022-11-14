# autor : Skop
# fecha: 13/11/2022
# acción : Elaborar un algoritmo que utilizando procedimientos halle las operaciones con 2 números ingresados (suma, resta, multiplicación, división, cociente y residuo mediante restas sucesivas), el usuario indica cuando terminar.

# Programa Principal
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

#Modulo especifico Suma
def Suma(n1,n2):
    Suma=n1+n2
    print(f"La suma de los 2 numeros es: ",Suma)

#Modulo especifico Resta
def Resta(n1,n2):
    Resta=n1-n2
    print(f"La resta de los 2 numeros es: ",Resta) 

#Modulo especifico Multiplicacion
def Multiplicacion(n1,n2):
    Multiplicacion=n1*n2
    print(f"La multiplicacion de los 2 numeros es: ",Multiplicacion) 

#Modulo especifico Division
def Division(n1,n2):
    Division=n1/n2
    print(f"La division de los 2 numeros es: ",Division) 

#Modulo especifico Cociente
def Cociente(n1,n2):
    Cociente=n1*n2
    print(f"La multiplicacion de los 2 numeros es: ",Cociente) 

#Modulo especifico Residuo
def Residuo(n1,n2):
    Residuo=n1*n2
    print(f"La multiplicacion de los 2 numeros es: ",Residuo) 



Suma(num1, num2)   # llamar al procedimiento Suma
Resta(num1, num2)   # llamar al procedimiento Resta
Multiplicacion (num1, num2)   # llamar al procedimiento Multiplicacion
Division (num1, num2)   # llamar al procedimiento Division
Cociente(num1, num2)   # llamar al procedimiento Cociente
Residuo(num1, num2)	   # llamar al procedimiento Residuo