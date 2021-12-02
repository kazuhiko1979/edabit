"""
二本木構造
"""
class BinaryTree:
    def __init__(self, data):
        self.data = data
        # 左二分木
        self.left = None
        # 右二分木
        self.right = None

binaryTree = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)

binaryTree.left = node2
binaryTree.right = node3

print("Root: " + str(binaryTree.data))
print("Left: " + str(binaryTree.left.data))
print("right: " + str(binaryTree.right.data))





