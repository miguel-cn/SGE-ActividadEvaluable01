#Importar la librería necesaria para hacer las copias
import copy

# Clonar listas
original = [1, 2, 3, 4, 5, 6, 7, 8]
shallow_copy = copy.copy(original)  # Shallow copy
deep_copy = copy.deepcopy(original) # Deep copy
# La diferencia entre shallow y deep copy es cómo se tratan los
# objetos que se encuentran en la lista copiada.
# Mientras que copy.copy(x) solo hace una copia de x y hace
# referencias a los objetos anidados en x, copy.deepcopy(x) hace
# una copia tanto de x como de los objetos anidados, en lugar de
# simplemente referenciarlos.

# Añadir elementos
original.append("hola") # Esta línea añade la cadena "hola" al final de la lista
print(original) 


# Eliminar elementos
elemento = original.pop() # La función pop elimina el último elemento y lo devuelve
print(elemento)
original.remove(1) # Remove elimina el valor pasado como parámetro


# Crear una lista nueva con los 4 últimos elementos de una lista
ultimos_cuatro = original[-4:]
print(ultimos_cuatro)


# Convertir las palabras de una cadena (separadas por espacio) a una lista
cadena = "Estamos separadas por espacios"
lista = cadena.split(" ") 
# El método split toma el caracter enviado como
# parámetro y lo usa de punto de división para
# crear nuevas sub cadenas. Es decir, la primera
# cadena será "Estamos", ya que después hay un
# espacio, y la siguiente será "separadas", pues
# solo las separa un espacio (si fuera más de un
# espacio seguiría funcionando de la misma forma).
# El espacio se toma como referencia pero no se
# incluye en ningún valor.
lista2 = cadena.split() # El valor default del parámetro de .split() es un espacio en blanco
print(lista)
print(lista2)


# Comentarios con una línea.


'''
Comentarios
multilínea
'''