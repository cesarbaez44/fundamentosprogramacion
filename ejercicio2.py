'''
Crear un programa que calcule area y perimtro de un rectangulo

Entradas:
base: integer
altura: integer

salidas:
area: integer
perimetro: integer
'''
base = input("Ingresa la base: ")
base= int (base)
altura= input("Ingresa la Altura: ")
altura= int (altura)
area= base*altura
perimetro= (base * altura) * 2
print ("El area del rectangulo es: ",area)
print ("El perimtro del rectangulo es: ",perimetro)
