# Nama : Farel Ilyasa Habi Pratama
# NIM : 25041450138
# Kelas : E

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search_bst(parameterroot, target):

    if parameterroot is None:
        return False
    
    elif parameterroot.data == target:
        return True
    
    elif target < parameterroot.data:
        return search_bst(parameterroot.left, target)

    else:
        return search_bst(parameterroot.right, target)


parameterroot = TreeNode(50)
parameterroot.left = TreeNode(30)
parameterroot.right = TreeNode(70)
parameterroot.left.left = TreeNode(20)
parameterroot.left.right = TreeNode(40)
parameterroot.right.left = TreeNode(60)
parameterroot.right.right = TreeNode(80)
print("Uji coba angka 60 : ", search_bst(parameterroot, 60))
print("Uji coba angka 100 : ", search_bst(parameterroot, 100))
    
