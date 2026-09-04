class cliente:
    def __init__(self):
        self.__codigo = 3323


    def __cuenta(self):
        print("El codigo del cliente es: ")


    def getcodigo(self):
        return self.__codigo


persona = cliente()
print(persona._cliente__codigo)  # This will raise an AttributeError because __codigo is private
persona._cliente__cuenta() # esto da un error porque __cuenta es un método privado y no se puede acceder directamente desde fuera de la clase. y para que se pueda acceder a el se debe crear un método público que lo llame. y eso se hace

