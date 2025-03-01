def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Definir una matriz 3x3
matriz = [
    [9, 7, 3],
    [4, 1, 8],
    [6, 2, 5]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar
fila_a_ordenar = int(input("Ingrese el número de la fila a ordenar (0-2): "))

# Ordenar la fila seleccionada
bubble_sort(matriz[fila_a_ordenar])

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
