# autor : Skop
# fecha: 10/11/2022
# acción : Elaborar un algoritmo que utilizando un procedimiento imprima la cantidad de veces que le indiques una frase ingresada. 

#Modulo especifico Repeticion
def Repeticion(fras,canti):
    cont=0   # 1 inicialización
    while cont < canti:     # 2 condición
          cont = cont + 1  # 3 actualización
          print(fras) # 4 instrucción

# Programa Principal
frase=input("Ingresa la frase: ")
cantidad=int(input("Ingrese la cantidad de veces que deseas repetirla: "))
Repeticion(frase, cantidad)   # llamar al procedimiento Repeticio
