'''
el polimorfismo es multiples compoortamientos en distintas clases, recordar la jerarquia de clases y el concepto de clase padre e hija, asi como 
el de sobre escritura

ejemplo ya dentro de la jerarquia de clases, pueden haber muchas clases entremedio de una clase padre de la hija, en este caso de la clase padre animal y la hija perro
puede que arriba de perro haya otra, que le responda a otra asi sucesivamente hasta llegar a la clase padre que es animal

el metodo que se manda a llamar en un tipo de la clase hija, siempre es de la clase de menor jerarquía, para el ejemplo de ahorita la clase de menor jerarquía es 
la clase hija perro, se manda a llamar la clase de la clase hija y no la del padre, siempre la de menor jerarquia y no la de la clase hija

cuando hay una clase padre y 2 hijas, y estas comparten un mismo metodo, por tanto un mismo comportamiento a esto se le conoce como 'INTERFACE'

POLIMORFISMO: Multiples comportamientos segun con el tipo de datos que estemos trabajando, igual yo lo conozco como que una clase puede tomar 
varias formas segun se manipule mediante sus hijas

'''

class Animal: 

    def __init__(self):
        pass

    def hacer_sonido(self): 
        print("hago un pitido")

    def comer(self):
        print('Como muchas veces al día')


    def dormir (self):
        print('Duermo muchas horas')



class Perro (Animal): 
    # pass
    def __init__(self):
        super().__init__()

    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato (Animal): 
     def hacer_sonido(self):
            print('Puedo maullarr')
        

#main loop
print("Ejemplo de polimorfismo")
print("Clase padre soy un animal")
animal1 = Animal()
animal1.hacer_sonido() # el definido en la clase padre

print ("ejemplo de la clase hija perro")
perro = Perro()
perro.hacer_sonido() # el metodo de la clase hija pero del tipo perro, si quito la sobre escritura y NOO HAY OTRA CLASE, se va directo a llamar 
#A LA DE LA CLASE PADRE, SI NO HAY OTRA HIJA, si si lo hay como abajo que es otra de menor jerarquía se iría con la del  gato que tambien esta sobreescribiendo
# el mismo metodo de la clase padre, aqui es donde se aplica el POLIMORFISMO, que estipula que la clase se va a comportar de multiples maneras
#dependiendo del tipo de dato con el que estamos trabajando y si eciste o no sobreescritura, si existe el que se manda a llamar en el de la clase 
#hija o de menor jerarquia

print("ejemplo de la clase hija gato")
gato = Gato ()
gato.hacer_sonido() # en este caso el que se manda a llamar es el sobre escrito en la clase hija, en este caso el ultiomo que es la de gato