class Persona: 

    atributo_clase = 0 #SE DEFINEN AFUERA DE CUALQUIER METODO Y NO SE USA LA PALABRA CLAVE 'SELF' 

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia  # se asocia con el objeto en si mismo



#Programa principa

if __name__ == '__main__': 

    print("Atributo de clase")
    print(f"El atributo de clase: {Persona.atributo_clase}") # no es necesario crear objetos para acceder a este tipo de atributos

    #modificar el atributo de clase

    Persona.atributo_clase = 10 # la modif se hace sobre la el atributo de la clase sobre la clase misma

    print(f"Nuevo valor de atrib de clase {Persona.atributo_clase}")

    persona1 = Persona(15) #no es recomendado, pero como inicie un objeto este valor se fue al atributo de instancia
    #casi no es recomendado editar el valor del atributo de la clase desde la inicializacion del objeto, mejor accediendo al atributo desde la clase

    print(f"Accedo al atributo de clase desde el objeto de Persona1: {persona1.atributo_clase}")
    #esto de arriba no es lo mejor, pero desde luego que se puede hacer igual accediendo desde el objeto
    #pero recordar que se hace desde la llamada de clase y no desde el objeto

    print(f"Atributo de instancia desde persona1 {persona1.atributo_instancia}")

    #creando objeto para segunda persona

    persona2 = Persona(30) 

    print(f"Accedo al atributo de clase desde el objeto de Persona2: {persona2.atributo_clase}")
    print(f"Atributo de instancia desde persona1 {persona2.atributo_instancia}")
    


        