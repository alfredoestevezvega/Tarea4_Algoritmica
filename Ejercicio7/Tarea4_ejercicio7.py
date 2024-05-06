from Class_monticulos import *

# Creamos un objeto MonticuloMaximo
monticulo = MonticuloMaximo()

# Insertamos elementos en el montículo
monticulo.insertar(5)
monticulo.insertar(10)
monticulo.insertar(3)
monticulo.insertar(8)
monticulo.insertar(1)

# Mostramos el montículo
print("Montículo después de insertar elementos:", monticulo)

# Eliminamos el máximo elemento del montículo
maximo = monticulo.eliminarMax()
print("Elemento máximo eliminado:", maximo)

# Mostramos el montículo después de eliminar el máximo elemento
print("Montículo después de eliminar el máximo elemento:", monticulo)

# Construimos un montículo a partir de una lista desordenada
lista_desordenada = [9, 4, 7, 2, 6]
monticulo.construirMonticulo(lista_desordenada)
print("Montículo construido a partir de una lista desordenada:", monticulo)