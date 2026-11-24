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
    def comer(self):
        print('Como muchas veces al día')


    def dormir (self):
        print('Duermo muchas horas')



class Perro (Animal): 

    def __init__(self):
        super().__init__()

    def hacer_sonido(self):
        print('Puedo ladrar')
    
    #sobreescrituura del metodo dormir 
    def dormir(self):
        print('Duermo 15 horas al dia')
        

#main loop
print("Ejemplo de herencia en pythoon")
print("Clase padre soy un animal")
animal1 = Animal()
animal1.comer()
animal1.dormir()

print ("ejemplo de la clase hija")
perro = Perro()
perro.comer() 
perro.dormir() # se manda a llamar el metodo sobre escrito por la clase hija
perro.hacer_sonido()