class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                elif data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right


    def lookup(self, data):
        current_node = self.root
        while True:
            if current_node == None:
                return False
            if current_node.data == data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self, cur_node):
        if cur_node != None:
            self.printt(cur_node.left)
            print(str(cur_node.data))
            self.printt(cur_node.right)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()

# left -> root -> right



