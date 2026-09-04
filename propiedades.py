class empleado:
    def __init__(self, nombre, edad, salario):
        self.__nombre = nombre
        self.__edad = edad
        self.__salario = salario

    def __getnombre(self):
        return self.__nombre

    def __getedad(self):
        return self.__edad

    def __getsalario(self):
        return self.__salario

    def __setnombre(self, nombre):
        self.__nombre = nombre

    def __setedad(self, edad):
        self.__edad = edad

    def __setsalario(self, salario):
        self.__salario = salario

    def __delnombre(self):
        del self.__nombre

    def __deledad(self):
        del self.__edad

    def __delsalario(self):
        del self.__salario
    nombre = property (fget= __getnombre,
                        fset= __setnombre,
                        fdel= __delnombre,
                       doc="Soy la Propiedad del 'nombre'")

    salario = property(fget= __getsalario,
                       doc="Soy la Propiedad del 'salario'")

empleado1 = empleado ("Juan", 30, 50000)
empleado1.nombre = "Pedro"
print(empleado1.nombre,empleado1.salario)
help(empleado1)

# empleado1 = empleado("Juan", 30, 50000)
# print(empleado1.getnombre(), ',', empleado1.getedad(), ', ', empleado1.getsalario())
# empleado1.setnombre("Pedro")
# print(empleado1.getnombre(), ',', empleado1.getedad(), ', ', empleado1.getsalario())