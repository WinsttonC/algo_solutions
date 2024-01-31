class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.size = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def update_height(self, root):
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else: 
            return root

        self.update_height(root)
        self.update_size(root)
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.min_value_node(root.left)

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        self.update_height(root)
        self.update_size(root)
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def exists(self, root, key):
        if root is None:
            return 'false'
        if key == root.key:
            return 'true'
        elif key < root.key:
            return self.exists(root.left, key)
        else:
            return self.exists(root.right, key)

    def next(self, root, key):
        successor = None
        while root:
            if root.key > key:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor.key if successor else "none"

    def prev(self, root, key):
        predecessor = None
        while root:
            if root.key < key:
                predecessor = root
                root = root.right
            else:
                root = root.left
        return predecessor.key if predecessor else "none"
    
    def get_size(self, root):
        if not root:
            return 0
        return root.size

    def update_size(self, root):
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)

    def kth_max(self, root, k):
        if not root:
            return None
        right_size = self.get_size(root.right)
        if k == right_size + 1:
            return root.key
        elif k <= right_size:
            return self.kth_max(root.right, k)
        else:
            return self.kth_max(root.left, k - right_size - 1)
    
tree = AVLTree()
root = None


for i in range(int(input())):
    operation, num = input().split()
    num = int(num)
    if operation == '1':
        root = tree.insert(root, num)
    if operation == '-1':
        root = tree.delete(root, num)
    if operation == '0':
        print(tree.kth_max(root, num))


