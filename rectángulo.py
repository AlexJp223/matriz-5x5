# Calcular el área de un rectángulo.

def calcularArea(base, altura):
    Total = (base * altura )
    return Total

if __name__ == "__main__":
    base = 8
    altura = 4 
    resultado = calcularArea (base, altura)
    print("Resultado del Area: ", resultado)