#EMPRESA PARA ALMACENAR Y ADMINISTRAR LOS DIFERENTES TIPOS DE EMPLEADOS, QUE EN SI SON OBJETOS
# from sistema_empleados.empleado import Empleado
from empleado import Empleado
class Empresa: 
    def __init__(self,nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, departamento): 
        #Puedo crear un objeto dentro de esta clase para que asi lo asigne dentro de la funcion de contratar, pero usando la plantilla de la clase anterior
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_num_empleados_departamento(self, departamento): # aqui departamento es dinamico por lo que significa que buscaremos un departamento de un valor en especifico
        contador_empleados_departamento = 0 
        for empleado in self.empleados: 
            if empleado.departamento == departamento: 
                contador_empleados_departamento +=1
        return contador_empleados_departamento

    def obtener_total_empleados(self): #numero total de empleados para esa objeto o empresa dada en especifico, independientemente de que dpto esten
        print(f"\nTotal de Empleados para la empresa: {self.nombre}")
        for empleado in self.empleados: 
            print(f''' Empleado {empleado.id}
            Nombre: {empleado.nombre}
            Departamento: {empleado.departamento}
            ''')

    



