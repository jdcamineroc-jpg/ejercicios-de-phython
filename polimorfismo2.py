class tomate:
     def tipo(self):
         print("vegetal")
     def color(self):
        print("rojo")

class manzana:
    def tipo(self):
        print("fruta")
    def color(self):
        print("rojo")


def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = tomate()
funcion(nuevo_tomate)
nuevo_manzana = manzana()
funcion(nuevo_manzana)


