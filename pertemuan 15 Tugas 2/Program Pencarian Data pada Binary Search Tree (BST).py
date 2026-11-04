# Membuat struktur kelas TreeNode untuk merepresentasikan node pohon
class TreeNode: # [cite: 11]
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    """Fungsi bantuan untuk memasukkan node ke dalam BST"""
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)
    return root

# Fungsi pencarian rekursif
def search_bst(root, target): # [cite: 11]
    # Jika root kosong atau target tidak ditemukan di ujung jalur
    if root is None:
        return False # [cite: 12]
    
    # Jika target ditemukan pada root saat ini
    if root.value == target:
        return True # [cite: 12]
    
    # Jika target lebih kecil dari nilai node saat ini, cari di sebelah kiri
    if target < root.value:
        return search_bst(root.left, target) # [cite: 13]
    
    # Jika target lebih besar, cari di sebelah kanan
    return search_bst(root.right, target) # [cite: 13]


# --- Driver Code ---

# Ketentuan Struktur BST yang diuji
root = TreeNode(50) # Root bernilai 50 [cite: 16]

# Subtree/Node lainnya dimasukkan sesuai aturan BST [cite: 17]
nodes_to_insert = [30, 70, 20, 40, 60, 80] # [cite: 17]
for val in nodes_to_insert:
    insert_bst(root, val)

# Lakukan uji coba pencarian [cite: 18]
print("Apakah angka 60 ditemukan? :", search_bst(root, 60))   # Angka yang ada [cite: 18]
print("Apakah angka 100 ditemukan? :", search_bst(root, 100)) # Angka yang tidak ada [cite: 18]