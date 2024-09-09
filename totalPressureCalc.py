def calcular_presion_total(M1, M2, m1, m2, V, T):
    # Convertir la temperatura de Celsius a Kelvin
    T_K = T + 273.15
    # Constante de los gases R en dm³·atm·K⁻¹·mol⁻¹
    R = 0.082
    # Calcular la presión total usando la fórmula dada
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_K / V
    return P_total

# Ejemplo de uso:
M1 = float(input("Introduce la masa molar del primer gas (M1) en g/mol: "))
M2 = float(input("Introduce la masa molar del segundo gas (M2) en g/mol: "))
m1 = float(input("Introduce la masa del primer gas (m1) en gramos: "))
m2 = float(input("Introduce la masa del segundo gas (m2) en gramos: "))
V = float(input("Introduce el volumen del recipiente (V) en dm³: "))
T = float(input("Introduce la temperatura (T) en °C: "))

P_total = calcular_presion_total(M1, M2, m1, m2, V, T)
print(f"La presión total ejercida por los gases es: {P_total:.2f} atm")
