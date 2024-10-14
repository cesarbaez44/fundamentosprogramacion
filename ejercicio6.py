'''
Ejercicio 6
Programa que calcule la media de 3 números pedidos por teclado

Entrada: num1, num2, num3

Salida: media
'''

num1 = input("Ingrese el primer numero: ")
num1 = int (num1)
num2 = input("Ingrese el segundo numero: ")
num2 = int (num2)
num3 = input("Ingrese el tercer numero: ")
num3 = int (num3)

media = (num1 + num2 + num3)/3

print ("La media de los 3 numeros ingresados es: ",media)