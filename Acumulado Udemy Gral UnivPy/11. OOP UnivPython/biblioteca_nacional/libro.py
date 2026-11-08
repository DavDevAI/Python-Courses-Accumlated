class Libro: 
    
    book_counter = 0

    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        Libro.book_counter +=1
        self._id = Libro.book_counter

    @classmethod
    def obtener_total_libros(cls): 
        return cls.book_counter

    @property
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def genero(self):
        return self._genero
    @property
    def id(self):
        return self._id
    

    #COMO VA A SER DE SOLO LECTURA NO NECESITO MI METODO SETTER PORQUE NO LO VOY A MODIFICAR Y SE ENTIENDE QUE SERA UN ATRIBUTO NO MODIFICABLE
    # def set_color(self,color): s
    #     self._color = color
