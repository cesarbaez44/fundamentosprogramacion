'''
Ejercicio 11
Programa que pida al usuario 2 números y muestre la distancia entre ellos 
(el valor absoluto de su diferencia) de modo que el resultado sea siempre positivo

Entrada: 
n1, n2

Salida: 
distancia
'''
num1 = input("Ingrese el primer numero: ")
num1 = int (num1)
num2 = input("Ingrese el segundo numero: ")
num2 = int (num2)

distancia = abs(num1-num2)

print ("La distancia es de: ",distancia)