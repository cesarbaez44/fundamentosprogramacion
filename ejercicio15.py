'''
Ejercicio 15
programa que dadas 2 variables numericas: A y B que el usuario debe teclear
intercambie los valores de ambas variables y muestre cuanto vale al final

Entrada: 
A, B

Salida: 
A, B
'''
A = input("\nIngrese el primer valor de A: ")
A = int (A)
B = input("Ingrese el primer valor de B: ")
B = int (B)

Temp = A
A = B 
B = Temp

print ("El valor final de A es:", A) 
print ("El valor final de B es:", B)