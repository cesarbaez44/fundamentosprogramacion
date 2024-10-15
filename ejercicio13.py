'''
Ejercicio 13
Programa que pida un número y que muestre su raiz cuadrada y su raiz cubica

Entrada: 
num1

Salida: 
raizCua
raizCub
'''

num1 = input("\nIngrese un número: ")
num1 = int (num1)

raizCua = num1 ** (1/2)
raizCub = num1 ** (1/3)

print("\nLa raiz cuadrada del numero es: ",raizCua)
print("La raiz cubica del numero es: ",raizCub)
