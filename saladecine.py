#Sala de cine 
#Nombre: Joel Alexander Zavala Pachay 
#Curso: Primero "e"

asientos = [[0 for columna in range(4)] for fila in range(3)]

fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

if 0 <= fila <= 2 and 0 <= columna <= 3:
    if asientos[fila][columna] == 1:
        print("Ese asiento ya estaba reservado.")
    else:
        asientos[fila][columna] = 1
        print("Asiento reservado con exito.")
else:
    print("Fila o columna fuera de rango. No se realizo la reserva.")
 
print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()