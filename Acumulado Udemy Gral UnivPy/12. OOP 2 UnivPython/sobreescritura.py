'''
podemos agarrar un metodo definido que esta en la clase padre, despues agarrarlo en la clase hija y cambiarle el comportamiento de lo que hace
a eso se le conoce como sobreescritura, ahorra si agarramos ese metodo de la clase hija, este metodo se jalara con el comportamiento antes
modificado, accediendo al metodo que estaba en la clase padre por medio de la herencia que sucedio dentro de la clase hija

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