# Primero hay que importar la librería sys para poder sobrecargar métodos
import sys
# Con la expresión *args la función tomará cualquier cantidad de argumentos
def suma(*args):
    total = 0
    for num in args:
        total += num
    return total

# Prueba:
print("Nada:",suma())
print("Suma de 1:", suma(1))
print("Suma de 1 y 2:", suma(1, 2))
print("Suma de 1, 2, 3 y 4:", suma(1, 2, 3, 4))
print("Suma de 10, 20, 30, 40 y 50:", suma(10, 20, 30, 40, 50))