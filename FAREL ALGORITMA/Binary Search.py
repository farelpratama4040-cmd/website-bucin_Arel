class TreeNode:
    """Representasi node dalam Binary Search Tree."""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search_bst(parameterroot, target):
    """Mencari target data di dalam Binary Search Tree."""
    
    if parameterroot is None:
        return False
    
    if parameterroot.data == target:
        return True
    
    if target < parameterroot.data:
        return search_bst(parameterroot.left, target)

    return search_bst(parameterroot.right, target)


def main():
    # Inisialisasi Root dan cabang-cabangnya
    parameterroot = TreeNode(50)
    parameterroot.left = TreeNode(30)
    parameterroot.right = TreeNode(70)
    
    # Inisialisasi daun (leaf)
    parameterroot.left.left = TreeNode(20)
    parameterroot.left.right = TreeNode(40)
    parameterroot.right.left = TreeNode(60)
    parameterroot.right.right = TreeNode(80)
    
    # Pengujian
    print("Uji coba angka 60 : ", search_bst(parameterroot, 60))
    print("Uji coba angka 100 : ", search_bst(parameterroot, 100))


if __name__ == "__main__":
    main()