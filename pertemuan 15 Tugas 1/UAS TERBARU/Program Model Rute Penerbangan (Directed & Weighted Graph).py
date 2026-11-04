class Graph:
    def __init__(self, size):
        # Inisialisasi matriks dengan nilai 0
        self.adj_matrix = [[0] * size for _ in range(size)]
        # Menyimpan nama kota (vertex)
        self.vertex_data = [''] * size

    def add_vertex_data(self, vertex, data):
        """Menambahkan nama kota ke index vertex tertentu"""
        if 0 <= vertex < len(self.vertex_data):
            self.vertex_data[vertex] = data

    def add_edge(self, u, v, weight):
        """Menambahkan rute berbobot dari kota u ke kota v"""
        if 0 <= u < len(self.adj_matrix) and 0 <= v < len(self.adj_matrix):
            self.adj_matrix[u][v] = weight

    def print_graph(self):
        """Menampilkan matriks ketetanggaan beserta nama kotanya"""
        print("Matriks Rute Penerbangan (dalam ribuan rupiah):")
        
        # Header kolom
        print(f"{'':>10}", end=" ")
        for v in self.vertex_data:
            print(f"{v[:4]:>8}", end=" ") # Menampilkan 4 huruf pertama kota agar rapi
        print("\n" + "-"*50)
        
        # Baris matriks
        for i in range(len(self.adj_matrix)):
            print(f"{self.vertex_data[i][:8]:>10} |", end=" ")
            for j in range(len(self.adj_matrix[i])):
                print(f"{self.adj_matrix[i][j]:>7}", end=" ")
            print()

# --- Driver Code Soal 1 ---
if __name__ == "__main__":
    # Membuat graf dengan 4 Vertex
    g = Graph(4)

    # Ketentuan kota (Vertex)
    g.add_vertex_data(0, "Jakarta")
    g.add_vertex_data(1, "Surabaya")
    g.add_vertex_data(2, "Bali")
    g.add_vertex_data(3, "Medan")

    # Ketentuan rute penerbangan (Edge dan Bobot)
    g.add_edge(0, 1, 800)   # Jakarta ke Surabaya
    g.add_edge(0, 2, 1200)  # Jakarta ke Bali
    g.add_edge(1, 2, 400)   # Surabaya ke Bali
    g.add_edge(2, 0, 1100)  # Bali ke Jakarta
    g.add_edge(3, 0, 900)   # Medan ke Jakarta

    # Tampilkan matriks
    g.print_graph()
    print("\n")