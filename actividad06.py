# Lista de tamaño y peso:
datos = [
    [180, 80],
    [160, 70],
    [175, 75],
    [180, 70],
    [170, 65]
]

# Explicación de la key function:
# Se usa para especificar el valor según el cual se ordenará la lista
# cuando se ordena una lista. Recibe un argumento (que es cada
# elemento de la lista) y devuelve el valor para comparar elementos.
# La "key function" es transforma los elementos de la lista en valores
# comparables y ordenables según el criterio elegido.

# Ordenar la lista por mayor altura y menor peso
datos_ordenados = sorted(datos, key=lambda x: (-x[0], x[1]))
# Invertir los signos de los argumentos llevaría a ordenar por menor altura y mayor peso
datos_ordenados2 = sorted(datos, key=lambda x: (x[0], -x[1]))

# Prueba:
print("Lista ordenada por mayor altura y menor peso:")
for elemento in datos_ordenados:
    print("Altura:", elemento[0], "- Peso:", elemento[1])

print("Lista ordenada por menor altura y mayor peso:")
for elemento in datos_ordenados2:
    print("Altura:", elemento[0], "- Peso:", elemento[1])