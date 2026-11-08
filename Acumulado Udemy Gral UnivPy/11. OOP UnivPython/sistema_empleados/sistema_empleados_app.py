#DECLARACION EXPLICITA DE UN DIRECTORIO PUEDE FALLAR A SERVER LEVEL Y EL INTERPRETE NO TE LO NOTIFICA
# from sistema_empleados.empleado import Empleado
# from sistema_empleados.empresa import Empresa
from empleado import Empleado
from empresa import Empresa

print("***Sistema de Empleados***")

#Crear una instancia de una empresa

empresa1 = Empresa("Global Mentoring")

#contratar algunos empleados

empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria','Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')

#Obtener el total de objetos de tipo empleado

print(f"Total de empleados: {Empleado.obtener_total_empleados()}")

#obtener el numero de empleados en el departamento de ventas

print(f"El numero total de empleados del departamento de ventas: "
      f"{empresa1.obtener_num_empleados_departamento('Ventas')}")


#mostrar todos los empleados de una empresa
empresa1.obtener_total_empleados()
