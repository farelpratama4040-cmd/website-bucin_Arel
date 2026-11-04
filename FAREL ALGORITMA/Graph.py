class Graph:
    """Representasi Graf menggunakan Adjacency Matrix."""
    
    def __init__(self, size):
        self.size = size
        self.vertex_data = [''] * size
        self.adj_matrix = [[0] * size for _ in range(size)]

    def add_vertex_data(self, vertex, data):
        """Menambahkan nama/data pada vertex tertentu."""
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def add_edge(self, u, v, weight):
        """Menambahkan edge berarah beserta bobotnya."""
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight

    def print_graph(self):
        """Mencetak Adjacency Matrix dan Vertex Data ke terminal."""
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            # Menggunakan generator expression untuk baris yang lebih rapi
            print(' '.join(str(x) if x is not None else '0' for x in row))

        print("\nVertex Data :")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")


def main():
    # Inisialisasi graf dengan 4 node
    g = Graph(4)
    
    # Pengisian data node (kota)
    g.add_vertex_data(0, 'Jakarta')
    g.add_vertex_data(1, 'Surabaya')
    g.add_vertex_data(2, 'Bali')
    g.add_vertex_data(3, 'Medan')

    # Pengisian edge (jarak/bobot antar kota)
    g.add_edge(0, 1, 800)
    g.add_edge(0, 2, 1200)
    g.add_edge(1, 2, 400)
    g.add_edge(2, 0, 1100)
    g.add_edge(3, 0, 900)

    # Cetak hasil
    g.print_graph()


if __name__ == "__main__":
    main()