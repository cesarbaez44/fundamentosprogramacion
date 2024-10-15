'''
Ejercicio 9
Una tienda ofrece un descuento de 15% sobre el total de la compra 
Un cliente desea saber cuanto pagará finalmente sobre su compra

Entrada: 
total_compra

Salida: 
total_a_pagar
'''
total_compra = input ("\nIngrese el total de su compra: ")
total_compra = int (total_compra)

descuento = total_compra * 0.15

total_a_pagar = total_compra - descuento

print ("\nSu total a pagar es de: ", total_a_pagar) 