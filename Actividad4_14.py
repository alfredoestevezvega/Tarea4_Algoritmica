from Class_Grafos import Grafo, Vertice
from Class_Vertices import *
from Class_mont_cola import *
from Class_Estructuras_lineales import ColaPrioridad


def dijkstra(unGrafo,inicio):
    cp = MonticuloBinario() #Realmente se implementa con un Montículo binario
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)

grafo = Grafo()
a = Vertice('A')
b = Vertice('B')
c = Vertice('C')
d = Vertice('D')
e = Vertice('E')

grafo.agregarVertice(a)
grafo.agregarVertice(b)
grafo.agregarVertice(c)
grafo.agregarVertice(d)
grafo.agregarVertice(e)

grafo.agregarArista(a, b, 10)
grafo.agregarArista(a, c, 15)
grafo.agregarArista(b, d, 12)
grafo.agregarArista(b, e, 15)
grafo.agregarArista(c, d, 10)
grafo.agregarArista(c, e, 5)
grafo.agregarArista(d, e, 10)

    # Ejecutar algoritmo de Dijkstra desde el vértice 'A'
dijkstra(grafo, a)

    # Mostrar las distancias más cortas desde 'A' hasta todos los demás vértices
for vertice in grafo:
    print(f'Distancia más corta desde A hasta {vertice.obtenerId()}: {vertice.obtenerDistancia()}')