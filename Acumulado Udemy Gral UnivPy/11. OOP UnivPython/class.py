#explicacion de clases del random del VIDEO DE YOUTUBE

class Pet: 
    def __init__(self, name, owner, age): ##init es un metodo especial para inicializar la clase 
    # es llamado automatico cuando el objeto es creado
        self.name = name
        self.owner = owner
        self.age = age
    
    #podemos personalizar el constructor para que haga exactamente lo que queramos que haga al inicializarse con self
    #puede que no haga nada o que siempre cuando la iniciemos le pasemos los valores, y cree los atributos antes definidos
    def print_info(self): #dentro de la clase nunca debemos de omitir el metodo de self
        print(self.name, self.owner, self.age)


#a diferencia de c o c++, para hacer un ojeto de la clase o instancia de la clase se iguala una variable
#y se llama a la clase como si fuera una función 

dog = Pet('jack', 'david', 2) # en este caso dog es una instancia u onjeto de la clase pet, a diferencia de otros lenguajes es diferente, se iguala 
#la variable a la clase llamandola como si se tratara de una función

#ahora voy a agregarle atributos a la clase de pet, accesando a ella por medio del punto como en cualquier otro lenguaje: 

# dog.name = 'jack'
# dog.owner = 'david'

#aqui ya con el objeto accedo al metodo de imprimir que ya está dentro de la clase
dog.print_info()

# cat = Pet()
#si hacemos que estas 2 instancias corran a la vez crashera, lo que necesita es que forcemos a que haga lo que queramos 
# es por eso que se necesita un constructor para la clase
# cat.name = 'russel'
# cat.owner = 'david'
# cat.age = 10 
# print(dog.name, dog.owner, dog.age)

