'''
ENCAPSULAMIENTO: 

El encapsulamiento, nos permite ocultar la informacion que almacena un objeto, tambien conocido como el estado de un objeto o status del objeto


Para aplicar el concepto del encapsulamiento se deben de aplicar 2 caracteristicas: 

    1) Atributos protegidos o privados: 
    self._nombre #Quiero que sea atributo protegido -> un solo guion bajo lo hace protegido
    self.__apellido #Quiero que sea atributo privado -> el doble guion bajo lo hace privado

    2) Crear los metodos conocidos como get(leer) y set (modificar)



todo esto nos permite evitar acceder directamente a la informacion de una clase , por cada atributo protegido en nuestra clase
ponemos nuestro metodo get() y set () respectivamente
'''

class Coche: 

    def __init__(self, marca, modelo, color):
        self.marca = marca # publico
        self._modelo = modelo # protegido aunque no es estricto como C que no se puede acceder directamente 
        # el denotrarlo con guion bajo hace que nos demos cuenta que es protegido y que no deberíamos accederlo directamente, por lo que
        #solo deberíamos de accederlo con nuestros metodos get() y set () para mantener esta integridad
        self.__color = color #privado

    def conducir(self): 
        #aqui tambien se puede hacer una fdocstring, para introducir mucho más información
        print(f'''Conduciendo el coche: 
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')



#LOS ATRIBUTOS GET() Y SET () SOLO SE USAN AFUERRA DE LA CLASE, ADENTRO SI, PORQUE ESTAMOS DENTRO DE LA MISMA CLASE

if __name__ == '__main__': 

    coche1 = Coche('Toyota', 'Yaris','Azul')
    coche1.conducir()
    #No deberiamos de aaceder a los atributos que no sean publicos
    coche1.marca = 'Toyora 2'
    coche1._modelo = 'Yris 2' #ESTO NO ES UNA BUIENA PRACTICA
    coche1.__color = 'negro' #aqui como esta totalmente privado, python ignora esta asignacion y solo usa la original
    #Forzando el acceder a esa atributo privado
    coche1._Coche__color = 'Negro' #Es una mala practica
    coche1.conducir()


    