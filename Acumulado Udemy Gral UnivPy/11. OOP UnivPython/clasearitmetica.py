class Aritmetica: 
#CLASE SIEMPRE INICIA EN MAYUSCULA 

    def __init__(self, x, y):
        self.op1 = x
        self.op2 = y 

    def sumar (self): 
        print(self.op1 + self.op2)

    def restar (self): 
        return self.op1 - self.op2

    def multiplicar (self): 
        return self.op1 * self.op2

    def dividir (self):
        return self.op1 / self.op2



if __name__ == '__main__': 

    x = int(input("Define tu operador uno: \n"))
    y = int(input("Define tu operador dos: \n"))

    choice = input('''Elije tu operacion: s - para suma, 
     r - para resta, m -  para multiplicacion, 
      d - para division:  ''')

    if choice == 's': 
        suma = Aritmetica(x,y)
        suma.sumar()
    '''usar if, para caer en una de las condiciones en especifico, entoneces 
     si quiero utilizarlo de la manera tradicional solo if, if, if, pero si quiero que funcione 
      como funcionaría en un SWITCH CASE DE C/C++, ahi si se usa if, elif, elif, else, el cual continua medio ciclandose hasta que caiga el caso
       deseado, mientras no, como sucede aqui solo se usara if, if, if, else '''

    
    if choice == 'r': 
            resta = Aritmetica(x,y)
            r2 = resta.restar() # EN ESTE CASO DEBO DE CREAR EL OBJETO PERO LLAMANDOLO COMO OBJETO PARA QUE HAGA LO QUE QUIERO SI 
            #ES QUE RETORNA ALGO, ES DECIR SI HAGO r2 = resta.restar, pues solo crea el objeto o instanciacion nada mas, guardarlo como variable
            #pero no ejecuta o realiza lo que existe dentro de, en camibo si llamo r2 = resta.restar (), ahi si realiza lo que yo quiero
            print(r2)
    if choice == 'm': 
            multi = Aritmetica(x,y)
            r3 = multi.multiplicar()
            print(r3) 
    if choice == 'd': 
            div = Aritmetica(x,y)
            r4 = div.dividir()
            print(r4)

         

