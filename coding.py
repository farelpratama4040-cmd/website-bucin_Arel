import networkx as nx

# BAGIAN 1

g = nx.DiGraph()

# Data kota (nodes)
cities = ["Jakarta", "Surabaya", "Bali", "Medan"]
g.add_nodes_from(cities)

# Rute penerbangan dan bobotnya
g.add_edge("Jakarta", "Surabaya", weight=800)
g.add_edge("Jakarta", "Bali", weight=1200)
g.add_edge("Surabaya", "Bali", weight=400)
g.add_edge("Bali", "Jakarta", weight=1100)
g.add_edge("Medan", "Jakarta", weight=900)

print("Matriks Ketetanggaan (bobot dalam ribuan rupiah):")

# kolom
print("          ", end="")
for city in cities:
    print(f"{city:>10}", end="")
print()

# Isi matriks
for u in cities:
    print(f"{u:>10}", end="")
    for v in cities:
        # Mengambil nilai bobot jika edge tersedia, jika tidak maka 0
        weight = g[u][v]['weight'] if g.has_edge(u, v) else 0
        print(f"{weight:>10}", end="")
    print()
print()

# BAGIAN 2

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