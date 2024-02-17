# Operador is:
cadena = "hola"
if(cadena is "hola"):
    print("La cadena es hola.")
# El operador is funciona como un símbolo matemático de igual

# Operador in:
frase = "hola, qué tal?"
if(cadena in frase):
    print("La cadena hola se halla en la frase: "+frase)
lista = frase.split()
if(cadena in lista):
    print("La cadena hola se halla en la lista: "+frase)
# Este operador se usa para comprobar si un valor se halla
# en una serie de valores. Esto incluye cadenas y colecciones
# como, en este caso, una lista.

# Operador not:
# is not:
if(cadena is not "hola"):
    print("La cadena no es hola.")
# not in:
if(cadena not in lista):
    print("La cadena hola se halla en la lista: "+frase)
# El operador not se combina con los operadores in e is
# para comprobar si dos valores NO son iguales o si un
# valor NO se encuentra en una serie de valores
