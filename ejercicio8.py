'''
Ejercicio 8
Un vendedor quiere saber cuanto dinero obtendra por el %10 de comision de las 3 ventas que realiza en el mes
mas su sueldo base

Entrada: 
sueldob, venta1, venta2, venta3

Salida: 
comision_total, total
'''

sueldob = input("\nIngrese el sueldo base: ")
sueldob = int (sueldob)

venta1 = input("\nIngrese el monto de la primer venta: ")
venta1 = int (venta1)
venta2 = input("Ingrese el monto de la segunda venta: ")
venta2 = int (venta2)
venta3 = input("Ingrese el monto de la tercer venta: ")
venta3 = int (venta3)

comision = 0.10
comision_total = (venta1 + venta2 + venta3) * comision

total = sueldob + comision_total

print ("\nLa comisión total de las 3 ventas fue: ",comision_total)
print ("El total de dinero que ganara será: ",total) 