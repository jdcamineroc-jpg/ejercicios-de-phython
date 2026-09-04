class calculadora:
    def __init__(self ,numero):
        self.n = numero   
        self.datos = [0 for i in range(numero)]

    def ingresar_datos(self):
            self.datos = [int(input('ingresar datos '+str(i+1)+ ' = '))for i in range(self.n)]

class op_basicas(calculadora):
    def __init__(self,):
        calculadora.__init__(self,2)

    def suma(self):
        a,b, = self.datos 
        s = a + b 
        print('el resultado es:',s)
       
            
    
    def resta(self):
        a,b, = self.datos 
        r = a - b 
        print('el resultado es:',r)

    

class raiz(calculadora):
     def __init__(self,):
          calculadora.__init__(self,1)

     def cuadrada(self):
        import math
        a, = self.datos
        print('el resultado es:',math.sqrt(a))


ejemplos = raiz()
print(ejemplos.ingresar_datos())
print(ejemplos.cuadrada())
