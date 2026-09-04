# polimorfismo con metodos

class colombia:
    def capital(self):
        print("Bogota")
    def idioma(self):
        print("Español")

class francia:
    def capital(self):
        print("Paris")
    def idioma(self):
        print("Frances")


colombiano = colombia()
frances = francia()

for pais in (colombiano, frances):
    pais.capital()
    pais.idioma()