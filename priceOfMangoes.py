def mango(quantity, price):
    # Número de mangos que se pagan (cada 3 mangos, 2 son pagados)
    paid_mangos = quantity - (quantity // 3)
    # Calcular el costo total
    total_cost = paid_mangos * price
    return total_cost

# Ejemplo de uso
quantity = int(input("Introduce la cantidad de mangos: "))
price = int(input("Introduce el precio por mango: "))
print(f"El costo total es: ${mango(quantity, price)}")
