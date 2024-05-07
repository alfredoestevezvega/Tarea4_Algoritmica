"""Utilizando el método encontrarSucesor, escribe un recorrido inorden no recursivo para un árbol
binario de búsqueda.
"""
from Class_arbolbinariobusqueda import *

# Crear un árbol binario de búsqueda
arbol = ArbolBinarioBusqueda()

# Agregar elementos al árbol
arbol.agregar(50, "A")
arbol.agregar(30, "B")
arbol.agregar(70, "C")
arbol.agregar(20, "D")
arbol.agregar(40, "E")
arbol.agregar(60, "F")
arbol.agregar(80, "G")

# Verificar la longitud del árbol
print("Longitud del árbol:", len(arbol))

# Comprobar si una clave está presente en el árbol
print("¿La clave 30 está en el árbol?", 30 in arbol)
print("¿La clave 90 está en el árbol?", 90 in arbol)

# Obtener el valor asociado a una clave
print("Valor asociado a la clave 40:", arbol.obtener(40))

# Eliminar un elemento del árbol
del arbol[30]

# Verificar la longitud del árbol después de eliminar un elemento
print("Longitud del árbol después de eliminar un elemento:", len(arbol))

# Comprobar si una clave está presente en el árbol después de eliminar un elemento
print("¿La clave 30 está en el árbol después de eliminarla?", 30 in arbol)

print("El recorrido inorden no recursivo se ve de la siguiente manera: ")
arbol.recorrido_inorden_no_recursivo()