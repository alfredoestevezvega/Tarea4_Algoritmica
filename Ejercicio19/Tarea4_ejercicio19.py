from Class_grafos19 import *
import matplotlib.pyplot as plt
import networkx as nx
from Class_Vertices import Vertice

def mostrar_grafo(grafo,titulo):
    G = nx.DiGraph()

    # Agregar aristas al grafo NetworkX
    for vertice in grafo:
        for vecino in vertice.obtenerConexiones():
            G.add_edge(vertice.obtenerId(), vecino.obtenerId())
    # Definir posiciones fijas para los nodos


    # Dibujar el grafo
    pos = nx.spring_layout(G)  # Asignar posiciones a los nodos
    nx.draw(G, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold', font_color='black', edge_color='gray', arrows=True)

    # Mostrar la distancia encima de las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    # Mostrar el gráfico
    plt.title(titulo)
    plt.show()

def transponer(self):
        # Crear un nuevo grafo para almacenar el grafo transpuesto
        grafo_transpuesto = Grafo()

        # Iterar sobre los vértices del grafo original
        for vertice in self.listaVertices.values():
            # Agregar el vértice al grafo transpuesto si no está presente
            if vertice.obtenerId() not in grafo_transpuesto.listaVertices:
                grafo_transpuesto.agregarVertice(vertice.obtenerId())

            # Iterar sobre los vecinos de este vértice
            for vecino in vertice.obtenerConexiones():
                # Agregar una arista en el grafo transpuesto del vecino al vértice actual
                grafo_transpuesto.agregarArista(vecino.obtenerId(), vertice.obtenerId())

        return grafo_transpuesto

G = Grafo()

G.agregarArista(1, 2, 10);
G.agregarArista(1, 3, 15);
G.agregarArista(1, 6, 5);
G.agregarArista(2, 3, 7);
G.agregarArista(3, 4, 7);
G.agregarArista(3, 6, 10);
G.agregarArista(4, 5, 7);
G.agregarArista(6, 4, 5);
G.agregarArista(5, 6, 13);
  #  grafo_transpuesto = G.transponer()

    # Dibujar el grafo
mostrar_grafo(G,titulo="Grafo base")

grafo = transponer(G)
mostrar_grafo(grafo=grafo,titulo="Grafo transpuesto")