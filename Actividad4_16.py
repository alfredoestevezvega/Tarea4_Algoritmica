
from Class_Grafos import Grafo, Vertice
from Class_Monticulos import MonticuloBinario 
from Class_mont_cola import ColaPrioridad

def prim(G, inicio):
    cp = ColaPrioridad()
    for v in G:
        v.asignarDistancia(10000)
        v.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in G])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
          nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
          if verticeSiguiente in cp and nuevoCosto<verticeSiguiente.obtenerDistancia():
              verticeSiguiente.asignarPredecesor(verticeActual)
              verticeSiguiente.asignarDistancia(nuevoCosto)
              cp.decrementarClave(verticeSiguiente,nuevoCosto)

def inicializar_grafo():
    g = Grafo()
    g.agregarVertice('A')
    g.agregarVertice('B')
    g.agregarVertice('C')
    g.agregarVertice('D')
    g.agregarVertice('E')
    g.agregarVertice('F')

    g.agregarArista('A', 'B', 2)
    g.agregarArista('A', 'C', 3)
    g.agregarArista('B', 'C', 1)
    g.agregarArista('B', 'D', 1)
    g.agregarArista('B', 'E', 4)
    g.agregarArista('C', 'E', 5)
    g.agregarArista('D', 'F', 3)
    g.agregarArista('E', 'F', 6)

    return g

# Función para imprimir el árbol de expansión mínima
def imprimir_arbol_expansion(arbol):
    for v in arbol.obtenerVertices():
        for vecino in v.obtenerConexiones():
            print(f"{v.obtenerId()} - {vecino.obtenerId()}: {v.obtenerPonderacion(vecino)}")

# Programa principal
def main():
    grafo = inicializar_grafo()
    inicio = grafo.obtenerVertice('A')
    arbol_expansion = prim(grafo, inicio)
    imprimir_arbol_expansion(arbol_expansion)

if __name__ == "__main__":
    main()
