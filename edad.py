# Verificar si una persona es mayor de edad.

def verificarMayoriaEdad(edad, edadMinima):
    if edad >= edadMinima:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"

if __name__ == "__main__":
    edad = 20
    edadMinima = 18
    resultado = verificarMayoriaEdad(edad, edadMinima)
    print("Verificación:", resultado)