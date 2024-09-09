import math

def age_range(age):
    if age <= 14:
        # Usar la fórmula alternativa para edades <= 14
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        # Usar la fórmula estándar para edades > 14
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)

    return f"{min_age}-{max_age}"

# Ejemplos de uso
print(age_range(27))  # 20-40
print(age_range(5))  # 4-5
print(age_range(17))  # 15-20
