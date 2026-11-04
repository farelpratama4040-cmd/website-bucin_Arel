# BAGIAN 1: GRAF RUTE PENERBANGAN (Directed & Weighted)

class Graph:
    def __init__(self, size):
        """Inisialisasi graf dengan jumlah vertex tertentu."""
        self.size = size
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.vertex_data = [''] * size  # menyimpan nama kota

    def add_vertex_data(self, vertex, data):
        """Menambahkan label/data untuk vertex tertentu."""
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def add_edge(self, u, v, weight):
        """Menambahkan edge berarah dari u ke v dengan bobot tertentu."""
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight

    def print_graph(self):
        """Menampilkan matriks ketetanggaan beserta label vertex."""
        print("Matriks Ketetanggaan (bobot dalam ribuan rupiah):")
        # Header kolom
        print("     ", end="")
        for i in range(self.size):
            print(f"{self.vertex_data[i]:>10}", end="")
        print()

        # Isi matriks
        for i in range(self.size):
            print(f"{self.vertex_data[i]:>5}", end="")
            for j in range(self.size):
                print(f"{self.adj_matrix[i][j]:>10}", end="")
            print()
        print()


# Membuat graf dengan 4 kota
g = Graph(4)

# data kota (vertex 0..3)
g.add_vertex_data(0, "Jakarta")
g.add_vertex_data(1, "Surabaya")
g.add_vertex_data(2, "Bali")
g.add_vertex_data(3, "Medan")

# rute penerbangan (berarah)
g.add_edge(0, 1, 800)   # Jakarta -> Surabaya
g.add_edge(0, 2, 1200)  # Jakarta -> Bali
g.add_edge(1, 2, 400)   # Surabaya -> Bali
g.add_edge(2, 0, 1100)  # Bali -> Jakarta
g.add_edge(3, 0, 900)   # Medan -> Jakarta

# Menampilkan graf
g.print_graph()

# BAGIAN 2: BINARY SEARCH TREE (BST) dengan Pencarian Rekursif

class TreeNode:
    """Node untuk Binary Search Tree."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_bst(root, val):
    """Menyisipkan nilai ke dalam BST sesuai aturan."""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    elif val > root.val:
        root.right = insert_bst(root.right, val)
    # jika sama, diabaikan
    return root


def search_bst(root, target):
    """
    Mencari target di dalam BST secara rekursif.
    Mengembalikan True jika ditemukan, False jika tidak.
    """
    if root is None:
        return False
    if target == root.val:
        return True
    elif target < root.val:
        return search_bst(root.left, target)
    else:  # target > root.val
        return search_bst(root.right, target)


# Membangun BST sesuai ketentuan
root = None
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    root = insert_bst(root, v)

# Uji coba pencarian
print("Pencarian dalam BST:")
print(f"Apakah 60 ditemukan? {search_bst(root, 60)}") 
print(f"Apakah 100 ditemukan? {search_bst(root, 100)}") 