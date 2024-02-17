import hashlib

# Función para convertir la contraseña a formato hash
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Utilizando una lista
usuarios_lista = []
contrasenas_lista = []

# Creación de dos listas, una de nombres de usuarios,
# otra de sus contraseñas. Al usuario del índice 0 de
# usuarios_lista le corresponde la contraseña del índice
# 0 de contrasenas_lista y así consecutivamente hasta el
# último índice.
usuarios_lista.append("usuario1")
contrasenas_lista.append(hash_password("password1"))
usuarios_lista.append("usuario2")
contrasenas_lista.append(hash_password("password2"))
usuarios_lista.append("usuario3")
contrasenas_lista.append(hash_password("password3"))
usuarios_lista.append("usuario4")
contrasenas_lista.append(hash_password("password4"))
usuarios_lista.append("usuario5")
contrasenas_lista.append(hash_password("password5"))

# Consulta en la lista
consulta_usuario = "usuario3"
consulta_contrasena = "password3"
# Existe usuario3?
if consulta_usuario in usuarios_lista:
    # indice es donde se ha encontrado al usuario en usuarios_lista
    indice = usuarios_lista.index(consulta_usuario)
    # La contraseña esta en ese indice en contrasenas_lista?
    if contrasenas_lista[indice] == hash_password(consulta_contrasena):
        # Si lo está:
        print("Acceso concedido para el usuario", consulta_usuario)
    else:
        # Si no lo está:
        print("Contraseña incorrecta para el usuario", consulta_usuario)
else:
    # Si no encuentra el usuario3:
    print("Usuario no encontrado")

# Utilizando un diccionario
usuarios_diccionario = {}

usuarios_diccionario["usuario1"] = hash_password("password1")
usuarios_diccionario["usuario2"] = hash_password("password2")
usuarios_diccionario["usuario3"] = hash_password("password3")
usuarios_diccionario["usuario4"] = hash_password("password4")
usuarios_diccionario["usuario5"] = hash_password("password5")

# Consultas en el diccionario
consulta_usuario = "usuario5"
consulta_contrasena = "password5"
# Comprueba si existe el usuario
if consulta_usuario in usuarios_diccionario:
    # Comprueba si el usuario tiene esa contraseña
    if usuarios_diccionario[consulta_usuario] == hash_password(consulta_contrasena):
        # La tiene
        print("Acceso concedido para el usuario", consulta_usuario)
    else:
        # No la tiene
        print("Contraseña incorrecta para el usuario", consulta_usuario)
else:
    # No existe el usuario
    print("Usuario no encontrado")
