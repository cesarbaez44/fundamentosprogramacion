
'''
Ejercicio 3
Programa que calcula la hipotenusa de un trianguloo rectangulo a partir de sus catetos 

Entradas :
Cateto1
Cateto2

Salidas:
Hipotenusa

Analisis:
Se resuelve con el teorema de pitagoras

'''
import math
cateto1=input("Escribe el cateto 1: ")
cateto1 = int (cateto1)
cateto2=input("Escribe el cateto 2: ")
cateto2 = int (cateto2)
hipotenusa = cateto1 *  cateto1 + cateto2 * cateto2
hipotenusa = hipotenusa ** (1/2)    #Forma 1 de elevar al cuaadrado/hipotenusa
hipotenusa = math.sqrt (hipotenusa) #Forma 2 de elevar al cuaadrado/hipotenusa

print ("La hipotenusa es: ",hipotenusa)