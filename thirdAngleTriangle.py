def third_angle(angle1, angle2):
    # La suma de los ángulos de un triángulo es siempre 180
    return 180 - (angle1 + angle2)

# Ejemplo de uso
angle1 = int(input("Introduce el primer ángulo: "))
angle2 = int(input("Introduce el segundo ángulo: "))
print(f"El tercer ángulo es: {third_angle(angle1, angle2)}")
