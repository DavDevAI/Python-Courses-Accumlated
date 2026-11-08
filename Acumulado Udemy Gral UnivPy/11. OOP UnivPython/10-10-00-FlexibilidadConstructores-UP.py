class Aritmetica:
    # Python solamente toma el ultimo constructor
    # def __init__(self, operando1):
    #     self.operando1 = operando1
    
    #Python no maneja el concepto de sobrecarga de constructores
    #por lo que siempre tomará el ultimo escrito, en este caso sería el segundo

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado división: {resultado}')


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Artimética ***')
    aritmetica1 = Aritmetica(5, 7)
    print('Primer objeto')
    aritmetica1.sumar()
    aritmetica1.restar()
    # Segundo objeto
    print('Segundo objeto')
    aritmetica2 = Aritmetica(12, 16)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()

    # Tercer objeto, como solo estaría pasando un argumento, podría usar la sobrecarga del constructor, 
    #pero como en este caso no sirve, no me pasaría por el primero, sino al segundo y ahí habría un problema por lo que en vez de eso 
    #podemos jugar con los parametros de la misma clase, dado a su flexibilidad
    print('Tercer objeto')
    #Para este caso en el que quisiera yo crear un objeto con un solo metodo, vuelvo a los parametros de arriba del constructo
    #y le asignaría al constructor en sus parametros: def __init__(self, operando1=None, operando2=None):
    # para que asi no sea obligatoría el pase de 2 parametros forzosamente, asignando el None, para que si una se usa, -> la otra no       
    aritmetica3 = Aritmetica(7)
    #como arriba forze que se adentrara solo un parametro, dada la naturaleza de la funcion yo tendria que agregar otro parametro
    #para que la operacion se pueda realizar, es por eso que aqui del objeto que cree accedo hasta el fondo de uno de sus variables
    #y le asigno desde aqui el valor de 9, (como pasaría en cualquier otro lenguaje, como en C/C++)
    aritmetica3.operando2 = 9
    aritmetica3.sumar()


    # Cuarto objeto
    print('Cuarto objeto')
    #Creo un objeto sin parametros, como sucedería en cualquier caso, en el cual solo se crea el objeto sin nada, para poder utilizarlo despues
    #lo que estabamos realizando anteriormente era hardcodearlo, y solo se haría en caso de que fuera necesario, en este caso no 
    #y como se puede ver posteriormetne de la creacion del objeto se le asignan valores, generalmente se crea vació para que se pueda reutlizar 
    #después
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()


    # Quinto objeto
    print('Quinto objeto')
    aritmetica5 = Aritmetica(operando2=4, operando1=3)
    aritmetica5.sumar()
