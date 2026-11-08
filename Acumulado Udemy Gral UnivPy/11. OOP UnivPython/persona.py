class Persona: 
    def iniciar_persona(self, nombre, apellido):#SELF PARA APUNTAR AL OBJETO QUE SE VA A CREAR

        #para agregarle atributos a la clase SIEMPRE USAMOS SELF YA QUE ASÍ ES COMO MANDA EL APUNTADOR, SON METODOS INTRINSECOS DE LA MISMA CLASE
        self.nombre = nombre  #nombre del parametro debe de ser igual al del atributo, le asigno el valor que entra a ESE ATRIBUTO DE LA CLASE
        #SI NO TIENE LA PALABRA SELF NO ESTAMOS ACCEDIENDO O COMO SE DICE NO LE ESTAMOS ASIGNANDO ESE PARAMETRO A ESE ATRIBUTO DE LA CLASE
        self.apellido = apellido 

    #AUNQUE ESTE DENTRO DE LA MISMA CLASE USO EL ATRIBUTO U OPERADOR DE SELF PARA ACCEDER A AQUELLOS PARAMETROS 
    #QUE SON INTRINSECAMENTE DE LA CLASE Y ASI DIFERENCIARLOS DE LOS DE AFUERA O DE LOS GLOBALES Y DEFINIR EL SCOPE DE SOLO AQUI ADENTRO
    def mostrar_persona(self): 
        print (f''' 
        Nombre: {self.nombre}  
        Apellido: {self.apellido}
        ''')

#PARA HACER EL OBJETO UTILIZAMOS 


if __name__ == '__main__': #PARA QUE SE EJECUTE ESTE CODIGO UNICAMENTE SI ESTAMOS TRABAJANDO DENTRO DE ESTE MISMO ARCHIVO
    #SI EJECUTO ESTA PRUEBA DENTRO DE ESTE ARCHIVO SE VA A EJECUTAR


    #aqui abajo empiezo la instanciacion, y al mismo tiempo es un constructor, por eso tiene la igualdad

    persona1 = Persona() # creo este objeto vacio en memoria, alocando este espacio para despues llenarlo, ya sea para acceder o para agregarle
    #el de arriba es como un constructor o inicialziador como el de Python
    persona1.iniciar_persona('Layla', 'Acosta')
    persona1.mostrar_persona()


    #segundo objeto

    persona2 = Persona() 
    persona2.iniciar_persona('Ian', 'Sanchez')
    persona2.mostrar_persona()

