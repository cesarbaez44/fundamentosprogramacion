'''
Ejercicio 4
Programa que dados 2 numeros muestre la suma, resta, multiplicacion y division de ambos números

Entradas :
no1
no2

Salidas:
suma,resta,multi,div

'''
no1=input("Escribe el primer número: ")
no1= int (no1)
no2=input("Escribe el segundo número: ")
no2= int (no2)

suma  = no1 + no2
resta = no1-no2
multi = no1*no2
div   =no1/no2

print ("La suma de los numeros son: ",suma)
print ("La resta de los numeros son: ",resta)
print ("La multiplicacion de los numeros son: ",multi)
print ("La division de los numeros son: ",div)