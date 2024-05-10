# Tema5_09
"""Modifica la implementación de árbol binario de búsqueda para que maneje correctamente claves
duplicadas. Es decir, si una clave ya está en el árbol, entonces la nueva carga útil debería sustituir a la
antigua en lugar de agregar otro nodo con la misma clave."""


from Class_ArbolesBinariosBusqueda import ArbolBinarioBusqueda
#Creamos el arobl

miArbol = ArbolBinarioBusqueda()
miArbol[2] ="azul"
miArbol[3] = "amarillo"
miArbol[4] = "clavo"
miArbol[6] = "rinoceronte"

print(f"El valor que aparace con la clave {3} ahora mismo es:* {miArbol[3]} *y el que aparece con la clave {6} es:* {miArbol[6]} *")

#cambiamos las claves
miArbol[3] = "perro"
miArbol[6] = "gato"
print("")
print(f"Ahora con la clave {3} aparece es:* {miArbol[3]} *y con la clave {6} el valor que aparece es:* {miArbol[6]} *")