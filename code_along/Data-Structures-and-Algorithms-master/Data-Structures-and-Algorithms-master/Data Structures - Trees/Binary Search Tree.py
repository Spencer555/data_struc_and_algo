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

        curr_node = self.root
        while True:
            if data < curr_node.data:
                # Left
                if curr_node.left == None:
                    curr_node.left = new_node
                    return
                else:
                    curr_node = curr_node.left
            elif data > curr_node.data:
                # Right
                if curr_node.right == None:
                    curr_node.right = new_node
                    return
                else:
                    curr_node = curr_node.right

    def lookup(self, data):
        curr_node = self.root
        while True:
            if curr_node == None:
                return False
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
# Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)

    # If Intrested
    # code for remove

    def remove(self, data):
        if self.root == None:
            return False

        cur_node = self.root

        while cur_node:
            # find node
            if cur_node.data == data:
                # found
                # is a leaf node
                if cur_node.right is None and cur_node.left is None:
                    cur_node = None
                    return
                # has both nodes
                if cur_node.right and cur_node.left:
                    temp = cur_node.right
                    temp_left = cur_node.left
                    cur_node = temp
                    cur_node.left = temp_left
                    return
                # has only right node
                if cur_node.right:
                    temp = cur_node.right
                    cur_node = temp
                    return
                # has only left node
                if cur_node.left:
                    temp = cur_node.left
                    cur_node = temp
                    return

            elif data > cur_node.data:
                # right
                cur_node = cur_node.right
            elif data < cur_node.data:
                # left
                cur_node = cur_node.left


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
bst.remove(6)
