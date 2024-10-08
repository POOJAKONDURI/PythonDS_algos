# In-order Traversal: Left, Root, Right.
# Pre-order Traversal: Root, Left, Right.
# Post-order Traversal: Left, Right, Root.


    

'''

    @Author:pooja
    @Date:08-10-2024
    @last modified by:
    @last modified time:
    @title:Tree implementation

'''





class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Example usage tree = BinaryTree()
def main():
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)


        inorder_traversal(tree.root)   # Output: 5 10 15
        preorder_traversal(tree.root)  # Output: 10 5 15
        postorder_traversal(tree.root) # Output: 5 15 10

if __name__ == "__main__":
    main()