#ITERANDO SOBRE UN DICCIONARIO
lenguaje = {
    "nombre": "Python", 
    "creador": "Guido van Rossum"
}

for elemento in lenguaje.keys(): #como en C++ solo que no debo de declarar explícitamente
    print (elemento)

for elemento in lenguaje.values(): #como en C++ solo que no debo de declarar explícitamente
    print (elemento)

#ahora para que itere y devuelva 2 valores usamos el metodo items()

for llave, valor in lenguaje.items(): # es decir imprimir la llave y valor o elemento completo,  y lo devuelve como una lista de tuplas, si lo cambiamos a un elemento
    print(llave, valor)


#si queremos que lo concatene a u elemento lo devuelve como lista de tuplas

for concat in lenguaje.items(): 
    print(type(concat))

    