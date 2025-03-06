import random

ciudades = ["Quito", "Cuenca", "Guayaquil"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2

matriz_temperaturas = []
for i in range(len(ciudades)):
    matriz_temperaturas.append([])
    for j in range(semanas):
        matriz_temperaturas[i].append([])
        for k in range(len(dias)):
            matriz_temperaturas[i][j].append(random.randint(10, 35))

for i in range(len(ciudades)):
    print("\nPromedios semanales de temperatura para", ciudades[i])
    for j in range(semanas):
        suma = 0
        for k in range(len(dias)):
            suma += matriz_temperaturas[i][j][k]
        promedio = suma / len(dias)
        print("  Semana", j + 1, ":", round(promedio, 2), "°C")