from libro import Libro
from biblioteca import Biblioteca

biblio1 = Biblioteca("Vasconcelos")

#contratar algunos empleados

biblio1.agregar_libro('Cien Años de Soledad', 'Garcia Marquez', 'Ficcion')
biblio1.agregar_libro('Don Quijote', 'Cervantes', 'Comedia')
biblio1.agregar_libro('Amor en tiempos de colera', 'Garcia Marquez', 'Ficcion')
biblio1.agregar_libro('Pedro Páramo', 'Juan Rulfo', 'Ficcion')
biblio1.agregar_libro('Pantaleon y las visitadoras', 'Vargas Llosa', 'Comedia')


print("Libros de Garcia Marquez: ")
biblio1.buscar_por_autor('Garcia Marquez')
print("Libros de ficcion: ")
biblio1.buscar_por_genero('Ficcion')

print(f"todos los libros de la Biblioteca: {biblio1.nombre}")
biblio1.mostrar_todos()


#TODO ESTO LO PUEDO METER A UN LOOP A UN BANCO Y AHORRARME ESTE RETRABAJO