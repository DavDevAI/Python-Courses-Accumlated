# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    # def get_marca(self):
    #     return self._marca

    @property # Definir el metodo get de manera mas pythonica
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Azul 2'
    coche1.conducir()
    # Atributos dinámicos del objeto 

    #intentar agregar un nuevo atributo 

    setattr(coche1, 'nuevo_atributo', 'valor nuevo atributo') #aqui estoy agregandole o metiendole adentro de ese objeto de esa clase
    #2 nuevos atributos llamados 'nuevo atributo ' y 'valor nuevo atributo' aparte de los que ya trae definidos arriba en la clase de donde 
    #se deriva, si compruebo, imprimo ese nuevo atributo y de cierta manera le estoy agregando una nueva forma a la clase que trae adentro ese objeto
    #ya que mute ese objeto agrgandole ese nuevo atributo, e imprimiendolo me puedo dar cuenta que existe
    coche1.conducir()
    print(coche1.nuevo_atributo)
    #por el momento ese nuevo atributo solo es aplicable y accesible para solo ese objeto el objeto de coche 1, por lo que no se podria acceder 
    #a este nuevo atributo que cree desde el otro objeto
    coche1.nuevo_atributo2 = 'Valor nuevo del atributo 2'
    print(coche1.nuevo_atributo2)

    #le puedo preguntar a Python cuales son los atributos ya sea nuevos o existentes que tengo para este Objeto que acabo de manipular: 

    print(f'Atributos del coche1: {coche1.__dict__}') #usamos el atributo magico de 'dict' porque es dunderscore

    
    
    coche2 = Coche('Chevrolet','Trax','Blanco')
    coche2.conducir()
