# Pedimos al usuario que ingrese la cantidad de horas
horas = float(input("Ingresa la cantidad de horas: "))

# Realizamos los cálculos
minutos = horas * 60
segundos = horas * 3600

# Mostramos los resultados
print(f"{horas} hora(s) equivale a:")
print(f"- {minutos} minutos")
print(f"- {segundos} segundos")