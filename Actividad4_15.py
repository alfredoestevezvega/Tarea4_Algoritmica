import sys
import matplotlib.pyplot as plt
import networkx as nx

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if (self.graph[x][y] > 0 and not sptSet[y] and 
                        dist[y] > dist[x] + self.graph[x][y]):
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)

        # Convertir matriz de adyacencia a lista de conexiones
        connections = []
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != 0:
                    connections.append((i, j, self.graph[i][j]))

        # Crear grafo dirigido
        G = nx.DiGraph()

        # Agregar nodos
        for i in range(self.V):
            G.add_node(i)

        # Agregar conexiones
        G.add_weighted_edges_from(connections)

        # Visualizar el grafo
        pos = nx.spring_layout(G)  # Layout del grafo
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black', arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

# Driver's code
if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)

