# ==========================================
# Nama: Farel Ilyasa Habbi Pratama 
# NIM: 25041450138 
# Kelas: 2583E
# Deskripsi: Modul Graph dengan deteksi siklus (Cycle Detection) menggunakan Union-Find
# ==========================================

class Graph:
    def __init__(self, size):
        # Inisialisasi Adjacency Matrix 2D dengan nilai 0
        self.adj_matrix = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        
        # Parent array untuk memantau subset dalam Union-Find
        self.parent = [i for i in range(size)]

    # Menambahkan edge (undirected/tak berarah)
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    # Menambahkan label/data pada vertex
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    # Menampilkan graf dalam format matriks
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    # Fungsi Find untuk mencari akar (root) dari sebuah subset
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    # Fungsi Union untuk menggabungkan dua subset
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        print(f'Union: {self.vertex_data[x]} + {self.vertex_data[y]}')
        self.parent[x_root] = y_root
        print(f'Parent state: {self.parent}\n')

    # Mengecek apakah graf mengandung siklus
    def is_cyclic(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.adj_matrix[i][j]:
                    x = self.find(i)
                    y = self.find(j)
                    
                    # Jika keduanya punya root yang sama, berarti ada siklus
                    if x == y:
                        return True
                    
                    self.union(x, y)
        return False