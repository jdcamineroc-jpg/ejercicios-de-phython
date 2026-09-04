class Animal:
    def  __init__(self, name):
        self.name = name

    def tipo_animal(self):
        pass


class leon(Animal):
    def tipo_animal(self):
        print('mufasa es un animal salvaje')

class perro(Animal):
    def tipo_animal(self):
        print('firulais es un animal domestico')

nuevo_animal = leon('mufasa')
nuevo_animal.tipo_animal()

nuevo_animal2 = perro('firulais')
nuevo_animal2.tipo_animal()