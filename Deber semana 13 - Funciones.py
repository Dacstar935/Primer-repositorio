def calcular_promedio(datos):
    # Diccionario para almacenar los promedios de cada ciudad
    promedios = {}

    # Recorrer cada ciudad en los datos
    for ciudad in datos:
        total = 0  # Acumulador para la suma de temperaturas
        cantidad = 0  # Contador de temperaturas registradas

        # Recorrer cada semana de temperaturas de la ciudad
        for semana in datos[ciudad]:
            # Recorrer cada temperatura del día
            for temp in semana:
                total += temp  # Sumar la temperatura al total
                cantidad += 1  # Aumentar el contador

        # Calcular el promedio dividiendo el total entre la cantidad de registros
        promedios[ciudad] = total / cantidad

    # Retornar el diccionario con los promedios calculados
    return promedios


# Datos de prueba con temperaturas semanales de Quito, Guayaquil y Cuenca
datos = {
    "Quito": [[15, 16, 14, 13, 12, 11, 10], [16, 17, 18, 15, 14, 13, 12], [14, 15, 13, 12, 11, 10, 9],
              [17, 16, 15, 14, 13, 12, 11]],
    "Guayaquil": [[30, 32, 31, 29, 28, 27, 30], [31, 33, 34, 32, 30, 29, 28], [29, 30, 28, 27, 26, 25, 24],
                  [32, 31, 30, 28, 29, 27, 26]],
    "Cuenca": [[22, 23, 21, 20, 19, 18, 21], [23, 24, 25, 22, 21, 20, 19], [21, 22, 20, 19, 18, 17, 16],
               [24, 23, 22, 21, 20, 19, 18]]
}

# Llamar a la función para calcular los promedios\promedios = calcular_promedio(datos)

# Imprimir los promedios de temperatura por ciudad
print(calcular_promedio(datos))
