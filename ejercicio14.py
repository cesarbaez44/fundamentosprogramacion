'''
Ejercicio 14
Programa que pida un número de 2 cifras e invierta los digitos

Entrada: 
num1

Salida: 
invertido
'''
num1 = input("\nIngrese un número: ")
num1 = int (num1)

decena = (num1) / 10
unidad = (num1) % 10

invertido = (unidad * 10) + decena

print ("El numero invertido es:",invertido)