'''
Ejercicio 12
Programa que pida al usuario 2 pares de números x1,y1 y x2,y2, estos representan dos puntos en el plano
Calcula y muestra la distancia entre ellos 

Entrada: 
x1, y1, x2, y2

Salida: 
distancia
'''
x1 = input("Ingrese el valor de x1: ")
x1 = int (x1)
y1 = input("Ingrese el valor de y1: ")
y1 = int (y1)

x2 = input("\nIngrese el valor de x2: ")
x2 = int (x2)
y2 = input("Ingrese el valor de y2: ")
y2 = int (y2)

difx = x1 - x2
dify = y1 - y2

difxx = difx * difx
difyy = dify * dify

distancia = (difxx + difyy) ** (1/2)

print ("\nLa distancia es: ",distancia)