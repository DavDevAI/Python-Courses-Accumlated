from libro import Libro 

class Biblioteca: 
    def __init__(self, nombre):
        self._nombre = nombre 
        self._libros = []

    def agregar_libro(self, titulo, autor, genero): 
        libro = Libro(titulo, autor, genero)
        self._libros.append(libro)

    def buscar_por_autor(self, autor): 
        for libro in self._libros: 
            if libro.autor == autor: 
                print(f"Libro -> Titulo: {libro.titulo}, Autor: {libro._autor}, Genero: {libro.genero}")
    
    def buscar_por_genero(self, genero): 
        for libro in self._libros: 
            if libro.genero == genero:
                print(f"Libro -> Titulo: {libro.titulo}, Autor: {libro._autor}, Genero: {libro.genero}")

    def mostrar_todos(self):
        print(f"\nTodos los libros de la Biblioteca")
        for libro in self._libros: 
            print(f''' Libro {libro.id}
            Nombre: {libro.titulo}
            Autor: {libro.autor}
            Genero: {libro.genero}
            ''')

    def mostar_libro(self): 
        print(f"El libro actual es: {self.titulo}")

    @property
    def nombre(self):
        return self._nombre

    @property
    def libros(self):
        return self._libros

    