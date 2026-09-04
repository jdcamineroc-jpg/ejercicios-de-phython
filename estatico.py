import math

class pastel:
    def  __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    def __str__(self):
        return (f'Pastel({self.ingredientes}, 'f'{self.tamaño})')

    def area(self):
        return self.tamaño_area(self.tamaño)
    @staticmethod
    def tamaño_area(A): 
        return A ** 2 * math.pi
    
nuevo_pastel = pastel(['harina', 'azucar', 'huevo'], 5)

print(nuevo_pastel.tamaño_area(4))