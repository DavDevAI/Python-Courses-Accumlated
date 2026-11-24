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

#main loop
print("Ejemplo de herencia en pythoon")
print("Clase padre soy un animal")
animal1 = Animal()
animal1.comer()
animal1.dormir()

print ("ejemplo de la clase hija")
perro = Perro()
perro.comer() 
perro.hacer_sonido()