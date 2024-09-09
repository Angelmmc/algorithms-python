import math

def litres(time):
    # Calcula el número de litros y redondea hacia abajo
    return math.floor(time * 0.5)

# Ejemplo de uso
time = float(input("Introduce el tiempo en horas: "))
print(f"Litros que beberá Nathan: {litres(time)}")