'''
Ejercicio 7
Programa un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde

Entrada: 
total_minutos

Salida: 
horas, minutos
'''
total_minutos = input("Ingrese el total de minutos a convertir: ")
total_minutos = int (total_minutos)

horas= total_minutos / 60
minutos = total_minutos % 60

print ("El total de minutos ingresado corresponde a: ",horas, "y",minutos, "minutos")