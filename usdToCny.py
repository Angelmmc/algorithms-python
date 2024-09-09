def usd_to_cny(usd):
    # Tasa de conversión
    conversion_rate = 6.75
    # Convertir USD a CNY
    cny = usd * conversion_rate
    # Devolver el resultado con 2 decimales y el texto 'Chinese Yuan'
    return f"{cny:.2f} Chinese Yuan"

# Ejemplo de uso
usd = int(input("Introduce la cantidad en USD: "))
print(usd_to_cny(usd))
