matriz = [
 
[10, 7, 6],
 
[2, 6, 8],
 
[6, 5, 7],
 
]
 
numero = int (input ("ingrese número"))
 
Encontrar = False
for fila in matriz:
    for valor in fila:
        if valor == numero:
            Encontrar= True
if Encontrar:
    print("El numero si esta en la matriz")
else:
    print("No se encuentra en la matriz")