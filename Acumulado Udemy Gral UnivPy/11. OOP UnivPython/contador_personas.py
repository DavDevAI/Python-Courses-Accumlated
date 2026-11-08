class Persona: 
    contador_personas = 0

    def __init__(self, nombre, apellido):
        #incrementamos el valor del atributo de la clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self): 
        print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")


if __name__ == "__main__": 
    print("Contador de objetos de tipo persona")
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    persona2 = Persona('Daniel', 'Sanchez')
    persona2. mostrar_persona() 

    #valor de contador de objetos de la clase persona

    print(f"Contador de objetos en la clase persona: {Persona.contador_personas}")

