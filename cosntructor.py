# class persona:
#     pass
#     def __init__(self,nombre,anos):
#         self.nombre = nombre
#         self.anos = anos
#     def descricion(self):
#         return '{} tiene {} anos'.format(self.nombre,self.anos)

#     def cometario (self, frase):
#         return '{} dice: {}'.format(self.nombre,frase)



# doctor = persona('jose',26)

# print(doctor.descricion())
# print(doctor.cometario('hola, como estan?'))


#modifica un atributo

class email:
    def __init__(self):
        self.enviado = False
    def envia_correo(self):
        self.enviado = True

mi_correo = email()
#print(mi_correo.enviado)
mi_correo.envia_correo()
print(mi_correo.enviado)       