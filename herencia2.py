class Telefono:
    def __int__(self):
        pass

    def llamar(self):
        print("Llamando...")

    def ocupado(self):
        print("Ocupado...")

class camara:
    
    def __int__(self):
        pass

    def fotografia(self):
        print("fotografia...")

    def grabar_video(self):
        print("Grabando video...")

class reproductor:
    
    def __int__(self):
        pass

    def reproducir_musica(self):
        print("Reproduciendo musica...")

    def reproducir_video(self):
        print("Reproduciendo video...")


class celular(Telefono, camara, reproductor):
    def __del__(self):
        print("Telefono celular apagado...")


movil = celular()
print(movil.fotografia())