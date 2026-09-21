from notas import promedio, aprobo
Nota1= float(input("Ingrese la nota1: "))
Nota2= float(input("Ingrese la nota2: "))
Nota3= float(input("Ingrese la nota3: "))
Rpromedio= promedio(Nota1, Nota2, Nota3)
print(" promedio: ", Rpromedio)
print(" aprobado o reprobado: ", aprobo(Rpromedio))
 