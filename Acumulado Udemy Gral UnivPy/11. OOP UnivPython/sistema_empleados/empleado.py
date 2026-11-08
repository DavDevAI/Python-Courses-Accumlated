#RELACION DE AGREGACION DE UNA CLASE MAS PEQUEÑA A UNA MAS GRANDE QUE LA OTRA TENDREMOS CLASE EMPLEADO Y EMPRESA

class Empleado: 
    #primer atributo de clase, contador de cuantos empleados tendremos o habremos creado
    #sabemos que es un atributo de clase porque esta afuera de cualquier metodo perteneciente o creado dentro de la clase o esta afuera 
    #del metodo dunder de constructor de clase 
    contador_empleados = 0
    # RECUERDA para que se encapsule todo dentro de un objeto creado a PARTIR DE LA CLASE USO METODOS DE INSTANCIA O METODOS DE OBJETO
    # AL IGUAL QUE ATRIBUTOS DE OBJETO Y ESO HACE QUE NO TRASPACE A LA CLASE Y ASI SE GUARDE COMO PASARIA EN OTRO LENGUAJE
    # EN ESTE CASO HARE UNA COMBINACION DE AMBOS PARA QUE ALGUNOS PARAMETROS Y METODOS SE QUEDEN DENTRO DE LA INSTANCIA U OBJETO Y OTROS DENTRO DE LA CLASE
    
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleados +=1
        #no agregar ID pero podria agregarse
        self.id = Empleado.contador_empleados

    #USO EL DECORADOR PARA DEFINIR QUE ES UN METODO DE CLASE
    @classmethod
    def obtener_total_empleados(cls): #aqui le paso cls en vez de self porque me estoy refiriendo a la clase en si misma es un metodo de clase y el decorador de arriba me lo indica 
        #nos va a permitir acceder a los atributos de clase
        #con cls sabemos se refiere a la clase en si misma y no a la de objetos
        return cls.contador_empleados