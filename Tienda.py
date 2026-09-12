# calculo de tienda

def  calcularTotal (precio, cantidad):
    Total = (precio * cantidad)
    return Total 

if __name__ == "__main__":
    precio = 10 
    cantidad = 5
    resultado = calcularTotal( precio , cantidad)
    print(resultado)