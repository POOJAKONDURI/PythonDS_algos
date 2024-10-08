
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

def main():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)

if __name__ == "__main__":
    main()

