class Graph:
    def __init__(self, size):
        # Inisialisasi matriks dengan nilai 0 (menandakan tidak ada rute)
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.vertex_data = [''] * size

    def add_vertex_data(self, vertex, data):
        # Menambahkan nama kota ke dalam indeks vertex
        if 0 <= vertex < len(self.vertex_data):
            self.vertex_data[vertex] = data

    def add_edge(self, u, v, weight):
        # Menambahkan bobot (harga) pada edge berarah u -> v
        if 0 <= u < len(self.vertex_data) and 0 <= v < len(self.vertex_data):
            self.adj_matrix[u][v] = weight

    def print_graph(self):
        print("Adjacency Matrix (Rute Penerbangan & Harga Tiket):")
        print(f"{'':>10}", end=" ")
        for city in self.vertex_data:
            print(f"{city:>10}", end=" ")
        print()
        
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertex_data[i]:>10}", end=" ")
            for weight in row:
                print(f"{weight:>10}", end=" ")
            print()


# --- Driver Code ---
g = Graph(4)

# Ketentuan Kota (Vertex)
g.add_vertex_data(0, "Jakarta")   # [cite: 4]
g.add_vertex_data(1, "Surabaya")  # [cite: 5]
g.add_vertex_data(2, "Bali")      # [cite: 6]
g.add_vertex_data(3, "Medan")     # [cite: 7]

# Ketentuan Rute Penerbangan (Edge dan Bobot dalam ribuan rupiah)
g.add_edge(0, 1, 800)  # Jakarta ke Surabaya dengan harga 800 [cite: 8]
g.add_edge(0, 2, 1200) # Jakarta ke Bali dengan harga 1200 [cite: 8]
g.add_edge(1, 2, 400)  # Surabaya ke Bali dengan harga 400 [cite: 8]
g.add_edge(2, 0, 1100) # Bali ke Jakarta dengan harga 1100 [cite: 8]
g.add_edge(3, 0, 900)  # Medan ke Jakarta dengan harga 900 [cite: 8]

# Menampilkan graf
g.print_graph()        #