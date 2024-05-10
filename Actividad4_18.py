
import sys
import matplotlib.pylab as plt
import networkx as nx

class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# A utility function to print 
	# the constructed MST stored in parent[]
	def printMST(self, parent):
		print("Edge \tWeight")
		for i in range(1, self.V):
			print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minKey(self, key, mstSet):

		# Initialize min value
		min = sys.maxsize

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index

	# Function to construct and print MST for a graph
	# represented using adjacency matrix representation
	def primMST(self):

		# Key values used to pick minimum weight edge in cut
		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array to store constructed MST
		# Make key 0 so that this vertex is picked as first vertex
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 # First node is always the root of

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minKey(key, mstSet)

			# Put the minimum distance vertex in
			# the shortest path tree
			mstSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for v in range(self.V):

				# graph[u][v] is non zero only for adjacent vertices of m
				# mstSet[v] is false for vertices not yet included in MST
				# Update the key only if graph[u][v] is smaller than key[v]
				if self.graph[u][v] > 0 and mstSet[v] == False \
				and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u

		self.printMST(parent)

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
if __name__ == '__main__':
	g = Graph(9)
	g.graph = [[0, 2, 0, 6, 0, 0, 0, 0, 0],
			[2, 0, 3, 8, 5, 0, 0, 0, 0, 0],
			[0, 3, 0, 0, 7, 0, 0, 0, 0, 0],
			[6, 8, 0, 0, 9, 0, 0, 0, 0, 0],
			[2, 0, 3, 8, 5, 0, 0, 0, 0, 0],
			[0, 3, 0, 0, 7, 0, 0, 0, 0, 0],
			[6, 8, 0, 0, 9, 0, 0, 0, 0, 0],
			[0, 5, 7, 9, 0, 0, 0, 0, 0, 0]]

	g.primMST()


