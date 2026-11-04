# Membuat struktur kelas TreeNode
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_node(root, key):
    """Fungsi bantuan untuk memasukkan node baru sesuai aturan BST"""
    if root is None:
        return TreeNode(key)
    
    if key < root.val:
        root.left = insert_node(root.left, key)
    elif key > root.val:
        root.right = insert_node(root.right, key)
        
    return root

# Membuat fungsi rekursif pencarian data
def search_bst(root, target):
    """Mencari target di dalam BST. Mengembalikan True jika ada, False jika tidak"""
    # Base case: jika root kosong (node tidak ditemukan)
    if root is None:
        return False
    
    # Jika node ditemukan
    if root.val == target:
        return True
    
    # Prinsip rekursif (mengeliminasi setengah jalur pencarian)
    if target < root.val:
        # Jika target lebih kecil, cari di subtree kiri
        return search_bst(root.left, target)
    else:
        # Jika target lebih besar, cari di subtree kanan
        return search_bst(root.right, target)

# --- Driver Code Soal 2 ---
if __name__ == "__main__":
    print("--- Pengujian Binary Search Tree (BST) ---")
    
    # Root bernilai 50
    root = TreeNode(50)

    # Memasukkan node lainnya sesuai aturan BST
    values_to_insert = [30, 70, 20, 40, 60, 80]
    for val in values_to_insert:
        insert_node(root, val)
        
    # Lakukan uji coba pencarian
    target_1 = 60
    target_2 = 100
    
    # Mencari data yang ada (60)
    result_1 = search_bst(root, target_1)
    print(f"Apakah node {target_1} ditemukan? : {result_1}")
    
    # Mencari data yang tidak ada (100)
    result_2 = search_bst(root, target_2)
    print(f"Apakah node {target_2} ditemukan? : {result_2}")