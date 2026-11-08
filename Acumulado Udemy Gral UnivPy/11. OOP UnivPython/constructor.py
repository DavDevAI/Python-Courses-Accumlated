'''
Un constructor es un metodo especial y se utiliza para crear un objeto o instanciar una clase, igual nos puede sevir para
crear e inicializar los atributos de un nuevo objeto


el metodo init se le conoce como un metodo magico o metodo 'dunder', debido al double underscore __init__()

es un metodo magico porque hace varias cosas a la vez como constructor e inicializador a la misma

'''

class Persona: 

    '''#tenia iniciar_persona trabajando como inicializador, pero ahora puedo usar init para que no lo haga manualmente como aqui abajo: 

    def iniciar_persona(self, nombre, apellido):#SELF PARA APUNTAR AL OBJETO QUE SE VA A CREAR, y para auto referirse a si misma, y activar o acceder a los atributos que tenfo aqui adentro en la clase

        self.nombre = nombre  
        self.apellido = apellido '''
    
    #EMPIEZO AQUI ABAJO CON MI COSNSTRUCTOR 
    
    #ESTE DE AQUI ABAJO ES EL CONSTRUCTOR
    def __init__(self,nombre, apellido): # va self que siempre va de cajón para autoreferirse e inicializarse asi como los parametros 
        #de las variables que le van a ser pasadas y que son los atributos iniciales de las clases

#LA VENTAJA ES QUE EL CONSTRUCTOR DE LA CLASE SE MANDA A LLAMAR DE MANERA AUTOMATICA, SIN QUE TENGAMOS QUE INIXALIZARLO Y MANDAR 
# A LLAMAR MANULMENTE DE MANERA EXPLICITA, INVOCANDO EL METODO DESDE CLASE ESCRIBIENDOLO EN LA LOGICA

#CUANDO PASA ESTO YA NO MANDO A LLAMAR A UN OBJETO VACIO EN MEMORIA, YA QUE AL INICIALIZARSE O MANDARSE A LLAMAR 
#YA VA PRECARGADA O INICIA DE UNA VEZ LO QUE QUIERO QUE TENGA ADENTRO Y YA NO VA VACIA Y AHORRO LINEAS DE CODIGO EN ESO 

        #Creamos los atributos de la clase
        self.nombre = nombre  
        self.apellido = apellido 

    def mostrar_persona(self): #self esta apuntando al objeto que esta pasando en ese cierto momento, muta de acuerdo al parametro que le 
        #estemos pasando en ese momento
        print (f''' 
        Nombre: {self.nombre}  
        Apellido: {self.apellido}
        ''')
        #AQUI COMO VA A SER A DESEO DEL PARAMETRO QUE LE ESTEMOS PASANDO POR ESE MOMENTO EL PARAMETRO SERA EL SELF
        print(f'Dir de memoria de {self}: {id(self)}') # id, me da la direccion de memoria de esa variable en ese momento
        print(f'Dir de memoria de {self} en hex: {hex(id(self))}') #igual hago el casteo para que me convierta el valor de ese id


if __name__ == '__main__': #PARA QUE SE EJECUTE ESTE CODIGO UNICAMENTE SI ESTAMOS TRABAJANDO DENTRO DE ESTE MISMO ARCHIVO
    #SI EJECUTO ESTA PRUEBA DENTRO DE ESTE ARCHIVO SE VA A EJECUTAR


    persona1 = Persona('Layla', 'Acosta') 
    persona1.mostrar_persona()

    # ESTO LO PASE PARA ARRIBA PARA QUE ME LO HAGA DENTRO DEL METODO DE LA CLASE
    # print(f'Dir de memoria de {persona1}: {id(persona1)}') # id, me da la direccion de memoria de esa variable en ese momento
    # print(f'Dir de memoria de {persona1} en hex: {hex(id(persona1))}') #igual hago el casteo para que me convierta el valor de ese id
    
    #segundo objeto
    persona2 = Persona('Ian', 'Sanchez') 
    persona2.mostrar_persona()
