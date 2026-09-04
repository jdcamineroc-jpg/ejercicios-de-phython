class mamifero:
    def __init__(self, nombre):
        print(nombre,"es un animal de sangre caliente")

class leon(mamifero):
    def __init__(self):
        print("es un animal salvaje y feroz")
        super().__init__('simba')

nuevo_leon = leon()
