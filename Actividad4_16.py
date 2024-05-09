
from Class_Grafos import Grafo, Vertice
from Class_Monticulos import MonticuloBinario 
from Class_Estructuras_lineales import ColaPrioridad

def prim(G,):
    cp = ColaPrioridad()
    for v in G:
        v.asignarDistancia(10000)
        v.asignarPredecesor(None)

    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in G])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
          nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
          if verticeSiguiente in cp and nuevoCosto<verticeSiguiente.obtenerDistancia():
              verticeSiguiente.asignarPredecesor(verticeActual)
              verticeSiguiente.asignarDistancia(nuevoCosto)
              cp.decrementarClave(verticeSiguiente,nuevoCosto)

grafo_ejemplo = Grafo()
grafo_ejemplo.agregarArista('A', 'B', 2)
grafo_ejemplo.agregarArista('A', 'C', 3)
grafo_ejemplo.agregarArista('B', 'C', 4)
grafo_ejemplo.agregarArista('B', 'D', 5)
grafo_ejemplo.agregarArista('C', 'D', 1)

arbol_expansion_minima = prim(grafo_ejemplo)
print("Árbol de expansión mínima:")
for vertice in arbol_expansion_minima:
    for vecino in vertice.obtenerConexiones():
        print(vertice.obtenerId(), "--", vecino[0].obtenerId(), ": Peso", vecino[1])