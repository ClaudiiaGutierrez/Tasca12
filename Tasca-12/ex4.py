# Definición de la clase Animal con métodos básicos
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass  
    def __str__(self):
        return f"{self.nombre} ({self.__class__.__name__}), edad: {self.edad}"

# Clase Perro que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"  # Poner el ladrido en  hacer_sonido específico para Perro

# Clase Gato que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"  # Poner el Miau en hacer_sonido específico para Gato

# Clase Vaca que hereda de Animal
class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muuu!"  # Poner el MUU para hacer_sonido específico para Vaca

# Función principal que crea instancias de diferentes animales y los utiliza
def pex4():
    perro = Perro("Tobi", 6)  # El  Perro tiene  el nombre "Tobi" y edad 5
    gato = Gato("Michi", 4)   # El  Gato  tiene el nombre "Michi" y edad 4
    vaca = Vaca("Persiana", 5)  # La Vaca tiene el nombre "Persiana" y edad 5

    animales = [perro, gato, vaca]  # Lista que los objectos

    for animal in animales:
        if isinstance(animal, Animal):  # Verifica si el objeto es  de la clase Animal
            print(f"{animal} dice: {animal.hacer_sonido()}")  # Imprime la representación del animal y el sonido que hace
        else:
            print(f"Objeto {animal} no es una instancia de Animal")  # Mensaje si el objeto no pertenece a Animal

# Programa principal que llama a la función pex4 para ejecutar el ejemplo
if __name__ == "__main__":
    pex4()
