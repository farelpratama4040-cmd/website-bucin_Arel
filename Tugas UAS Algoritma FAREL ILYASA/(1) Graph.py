# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            # self.adj_matrix[v][u] = weight



    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))

        print("\nVertex Data :")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

g = Graph(4)
g.add_vertex_data(0, 'Jakarta')
g.add_vertex_data(1, 'Surabaya')
g.add_vertex_data(2, 'Bali')
g.add_vertex_data(3, 'Medan')

g.add_edge(0, 1, 800)
g.add_edge(0, 2, 1200)
g.add_edge(1, 2, 400)
g.add_edge(2, 0, 1100)
g.add_edge(3, 0, 900)

g.print_graph()