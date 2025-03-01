# Definir una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print (matriz)
# Valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar: "))

encontrado = False

# Buscar el valor en la matriz
for f in range(3):
    for c in range(3):
        if matriz[f][c] == valor_buscado:
            print(f"El valor {valor_buscado} se encuentra en la posición ({f}, {c})")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print("El valor no se encuentra en la matriz.")
