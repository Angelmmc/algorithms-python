#Calcula la edad del perro y el gato en años humanos
def calculate_pet_ages(humanYears):
    # Calcular los años de los gatos
    if humanYears == 1:
        catYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
    else:
        #Como tiene más de 2 años entonces se suma la edad mas los años restantes con la equivalencia
        catYears = 15 + 9 + (humanYears - 2) * 4

    # Calcular los años de los perros
    if humanYears == 1:
        dogYears = 15
    elif humanYears == 2:
        dogYears = 15 + 9
    else:
        dogYears = 15 + 9 + (humanYears - 2) * 5

#Devuelve una lista de los valores
    return [humanYears, catYears, dogYears]

humanYears = int(input("Especifica la edad en años humanos: "))
result = calculate_pet_ages(humanYears)
print("Los años humanos son: " + str(result[0]))
print(f"Los años del perro son: {result[2]}")
print(f"edad del gato son: {result[1]}")

# # Ejemplo de uso:
# print(calculate_pet_ages(1))  # Output: [1, 15, 15]
# print(calculate_pet_ages(2))  # Output: [2, 24, 24]
# print(calculate_pet_ages(15))  # Output: [10, 56, 64]
# #Imprime tipo de dato devuelto por la función
# print(type(calculate_pet_ages(1)))

