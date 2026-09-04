class estudiantes:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre  
        self.apellido = apellido   
        self.edad = edad  

    def __repr__(self):
        return f" hola que tal, soy {self.nombre} {self.apellido} y tengo {self.edad} años"


nuevo_estudiante = estudiantes('victor', 'lopez', 17)
print(f"{nuevo_estudiante !r}")
