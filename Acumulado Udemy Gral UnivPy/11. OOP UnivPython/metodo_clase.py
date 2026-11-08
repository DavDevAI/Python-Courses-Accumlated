class Persona: 
    contador_personas = 0

    def __init__(self, nombre, apellido): #contructor
        #incrementamos el valor del atributo de la clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self): 
        print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")

    #existen metodos de clase, fuera de los que usan el parametro self, para eso uso el siguiente decorador, 
    #esto nos puede ayudar para tener un metodo estatico o inmutable y poder acceder a atributos de clase

    @staticmethod
    def get_contador_personas_estatico(): 
        print ('Metodo estático')
        return Persona.contador_personas

    #notacion que es mas Pythonica

    @classmethod
    def get_contador_personas_clase(cls): # el parametro cls que se refiere a que es un methodo de clase
        print("Metodo de Clase")
        #asi como en metodo de instancia, aqui nada mas no yusamos el metodo de clase en si mismo, sino usando cls
        return cls.contador_personas





if __name__ == "__main__": 
    print("Contador de objetos de tipo persona")
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    persona2 = Persona('Daniel', 'Sanchez')
    persona2. mostrar_persona() 

    #valor de contador de objetos de la clase persona

    print(f"Contador de objetos en la clase persona: {Persona.contador_personas}")

    print(f"Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}")

    print(f"Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}") # esta es una forma mas recomendada de Python 

    #accedioendo al contexto estático o atribyuto de clase desde objeto
    print(f"Contador objetos Persona (objeto): {persona1.contador_personas}")
    #el contexto dinamico si puede acceder al estatico, pero no viceversa, el estatico no puede acceder al dinamico

    
