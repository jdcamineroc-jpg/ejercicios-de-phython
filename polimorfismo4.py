# polimorfismo con herencia

class ave:
    def volar(self):
        print("la mayorias de las ave puede volar pero algunas no pueden volar")

class aguila(ave):
    def volar(self):
        print("El aguila puede volar alto")

class gallina(ave):
    def volar(self):
        print("La gallina no puede volar")

objeto_ave = ave()
objeto_aguila = aguila()
objeto_gallina = gallina()
objeto_ave.volar()
objeto_aguila.volar()
objeto_gallina.volar()