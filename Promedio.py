# calcular el promedio de tres notas

def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

print ("calculadora de promedio")
n1 = float(input("Ingresa la primera nota: "))
n2 = float(input("Ingresa la segunda nota: "))
n3 = float(input("Ingresa la tercera nota: "))

resultado = calcular_promedio(n1, n2, n3)

print (f"Tu promedio es: {resultado: .2f}")