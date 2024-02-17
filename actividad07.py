import random

class Car:
    def __init__(self, num) -> None:
        self.matricula = num
        self._color = random.choice(["red", "white","black", "pink", "blue"])# Lista de colores posibles
    
    # Método para cambiar el color
    def pintar(self, color):
        if(color in ["red", "white","black", "pink", "blue"]):
            self._color = color
            print("El coche con matrícula "+str(self.matricula)+" ha sido pintado con el color:"+color)
        else:
            # Si no existe ese color:
            print("El color "+color+" no está disponible.")
            print("Colores disponibles: red, white, black, pink, blue")
    
    def imprimir(self):
        print("***Coche***")
        print("Matrícula:", self.matricula)
        print("Color:", self._color)

    # Getter de color
    @property
    def color(self):
        return self._color
    
# Programa:
n = int(input("Introduce el número de coches que quieres crear: "))

# Creación de las instancias:
coches = []
for i in range(n):
    coches.append(Car(i+1))

# Mostrar los 10 primeros coches (o todos si hay menos):
if n>10:
    n=10
for i in range(n):
    coches[i].imprimir()

# Cambiar color de 10 coches (o todos si hay menos):
colores = ["red", "white", "blue", "purple"] # El color purple no estará disponible
for i in range(n):
    coches[i].pintar(random.choice(colores))