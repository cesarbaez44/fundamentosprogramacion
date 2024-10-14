'''
Ejercicio 5
Programa que convierta un valor dado en grados Fahrenheit a grados Celcius

Entradas:
Grados Fahrenheit / fahren

Salidas:
Grados Celcius / cel
'''
fahren=input("Ingrese la temperatura en grados Fahrenheit: ")
fahren = int (fahren)

cel = (fahren - 32) /1.8

print ("La conversion a grados celcius es: ",cel)