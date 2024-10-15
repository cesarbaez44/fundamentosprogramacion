'''
Ejercicio 10
Un alumno desea saber cual será su calificación final en la materia de algoritmos
Dicha calificacion se compone de los siguientes porcentajes:

55% del promedio de sus calificaciones parciales
30% de la calificación del examen final
15% de la calificación de un trabajo final

Entrada: 
calif_p1, calif_p2, calif_p3, examenfinal, trabajofinal

Salida: 
calif_final
'''
calif_p1 = input ("Ingrese la calificación del parcial 1: ")
calif_p1 = int (calif_p1)
calif_p2 = input ("Ingrese la calificación del parcial 2: ")
calif_p2 = int (calif_p2)
calif_p3 = input ("Ingrese la calificación del parcial 3: ")
calif_p3 = int (calif_p3)

examenfinal = input ("\nIngrese la calificación del examen final: ")
examenfinal = int (examenfinal)

trabajofinal = input ("\nIngrese la calificación del trabajo final: ")
trabajofinal = int (trabajofinal)

promparciales = (calif_p1 + calif_p2 + calif_p3)/3 

calif_final = (promparciales * 0.55) + (examenfinal * 0.33) + (trabajofinal * 0.15)

print ("\nSu calificación final fue de: ",calif_final)