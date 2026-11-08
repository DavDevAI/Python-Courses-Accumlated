class Coche: 

    def __init__(self, marca, modelo, color):
        #estandarizando mis atributos a todos privados
        self._marca = marca # 
        self._modelo = modelo #
        self._color = color #

    def conducir(self): 
        #aqui tambien se puede hacer una fdocstring, para introducir mucho más información
        print(f'''Conduciendo el coche: 
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')


    #AQUI SE ILUSTRA COMO EJEMPLO, PERO NO SE USA DENTRO DE LA CLASE, SINO FUERA DE ELLA
    
    # def get_marca(self): #este es un geter, como visto en el otro curso y lenguaje como JS y JSX
    #     return self._marca # lo unico que hace es retornarme el parametro de marca, para poder leer la info del atributo

    #COMENTO EL GET DE ARRIBA PARA DEFINIR ESTE METODO DE MANERA MAS IMPLICITA
    #USO EL DECORADOR 'PROPERTY'

    @property #definir el metodo de manera mas pythonica
    def marca(self):  #definir el metodo get de manera mas pythonica
        return self._marca


    #COMENTO COMO SE HACE DE LA MANERA TEDIOSA EXPLICITA Y LO REEMPLAZAMOS POR EL DECORADOR

    #dejo los metodos seters
    # def set_marca(self, marca): # para poder ahora si acceder al valor y modificar el atributo de marca
    #     self._marca = marca

    @marca.setter
    def marca(self, marca): 
        self._marca = marca
    
        
  
    # def get_modelo(self): 
    #     return self._modelo 
    @property
    def modelo(self): 
        return self._modelo 

    #utlizo un decorador para describir ahora el atributo y que se trata de un setter
    def set_modelo(self, modelo): 
        self._modelo = modelo

    # @modelo.setter
    # def modelo(self, modelo): 
    #     self._modelo = modelo

    # def get_color(self): 
    #     return self._color
    @property
    def color(self):
        return self._color
    

    def set_color(self,color): 
        self._color = color

    
#LOS ATRIBUTOS GET() Y SET () SOLO SE USAN AFUERRA DE LA CLASE, ADENTRO SI, PORQUE ESTAMOS DENTRO DE LA MISMA CLASE

if __name__ == '__main__': 

    coche1 = Coche('Toyota', 'Yaris','Azul')
    coche1.conducir()

    #AHORA SI PARA MODIFICAR EL ATRIB DE MARCA, VAMOS A USAR GET Y SET
    #coche1.set_marca('Toyota 2')
    coche1.set_modelo('Yaris 2')
    coche1.set_color('Azul 2')
    coche1.conducir()

    #EL USO DEL DECORADOR ME AYUDA A SIMPLIFICAR EN LO SIGUIENTE: 
    #Atributo de marca del Coche 1

    print(f'Atributo marca coche 1: {coche1.marca}') # en vez de utilzar get_marca, directamente estoy haciendolo con el decorador
    #es como si puediera acceder directamente al valor del atributo , lo pongo directamente como si fuera publico, pero sabemos que indirectamente
    #esta haciendo a el por el decorador

    coche1.marca = 'Toyota 3'

    print(f'Atributo de marca ya cambiado de coche 1: {coche1.marca}')




    


    