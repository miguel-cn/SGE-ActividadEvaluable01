

# Función que recibe 2 números y devuelve la suma
def suma(a, b):
    return a + b

# Función que recibe una lista y modifica los valores doblando cada elemento
def modificar_lista(lista):
    for i in range(len(lista)):
        lista[i] *= 2

# Función que recibe una lista y devuelve una copia de la lista modificada
def duplicar_valores(lista):
    # Crear una copia de la lista para no modificar la original
    lista_copia = lista.copy()
    for i in range(len(lista_copia)):
        lista_copia[i] *= 2
    return lista_copia

# Ejemplo de uso
num1 = 5
num2 = 7
resultado = suma(num1, num2)
print( num1, "+", num2, "=", resultado)

lista = [1, 2, 3, 4, 5]
print("Lista original antes de modificar:", lista)
modificar_lista(lista)
print("Lista original después de modificarla:", lista)

lista_copia = duplicar_valores(lista)
print("Copia de la lista original duplicando los valores:", lista_copia)
print("Lista original después de obtener la copia:", lista)