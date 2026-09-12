#Salario semanal

def calcularSalario(pago_diario, dias_trabajados):
    total = pago_diario * dias_trabajados
    return total

if __name__ == "__main__":
    pago_diario = 30
    dias_trabajados = 7
    resultado = calcularSalario(pago_diario, dias_trabajados)
    print(resultado)