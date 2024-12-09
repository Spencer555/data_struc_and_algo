'''
Trees are a data structure that have a heirachical structure
 root
 parent
 child
 leaf
 sibling


they can have zero or more children a tree start with one node and every child of the tree descend from this root node

and every child descend from one parent

and leaf nodes are the very end of a node they have no children

and trees can have subtrees a child with children
'''
''''
examples of tree data structres
facebook comments
dom tree
'''


'''
abstract syntax tree
this is how code is being run we write code and it gets broken down in to these

linked list
is a type of tree but with just one single path its linear  there is only one way to go from top to bottom

a node can only point to a child
'''


# binary trees

#         a
#     /       \
#     b        c


# each node can have 0,1 or 2 nodes and each child can only have one parent
'''
each node rep a certain state
'''


class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


'''
perfect binary tree - all leaf nodes are full and no node has only one child a node has 0 children or 2 children and buttom layer of the tree is completely filled
(they are efficient, the number of nodes on each level doubles as we move down the tree,
the num on nodes on the last level is equal to the sum of all the nodes on the other levels + 1)

this means about half of our data in the bottom level so if some how we can avoid visiting every node we can have efficiecies

full binary tree - a node has 0 or two children but never 1 child



big O
lookup 0(log N)
insert 0(log N)
delete 0(log N)


on a binary tree we can calculate the number of nodes we have by
level : 2 ^ level
e.g LEVEL 0: 2^0 so the root level is level zero so we get 1 node
level 1: 2^ 1 = 2

so we can find out nodes of a tree
2^h(height of tree) -1

log of nodes = height

log means
log 100 = 2
means 10log2 = 100

so logN in trees means only one of serveral possibilites have to be chosen we dont check both

0LogN is really fast

'''


# Binary search tree
# this data structute preserves relationships(parent folder subfolder etc)
# all child nodes in the tree to the right must be greater than the current node and the left must be less than the current node
# a node can have only two children
# searching and lookup is easy to do


# why and unbalanced search tree is bad
# with bst we can have balances search trees o(logN) and unbalanced ones  which becomes o(n)

# in interview know there are ways to balance a search tree and the trade offs


'''pros and cons of bst

pros
better than 0(n)
ordered
flexible size


cons
no 0(1)operations or no constant operation

comapred to arrays
inserts and deletes are faster than the array unless the array is adding to the end

compared to hash tables
we have sorted data and structure of parent child relationship u wont get with hash table

on average an array or obj would have faster operations but there a certain conditions they outperform objects and arrays
just make sure u stay away from edge cases and balance ur tree

'''


class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        '''
        pseduo code
        if the root is empty
        make the node the root

        else check if its greater than root send to the right if less send to the left
        recursivelly
        '''
        node = BinaryTreeNode(value)
        if self.root == None:
            self.root = node
            return

        curr_node = self.root
        while curr_node:
            # right
            if value > curr_node.value:
                if curr_node.right is None:
                    curr_node.right = node
                    return
                else:
                    curr_node = curr_node.right
            elif value < curr_node.value:
                # left
                if curr_node.left is None:
                    curr_node.left = node
                    return
                else:
                    curr_node = curr_node.left

    def lookup(self, value):
        curr_node = self.root

        found = False
        while curr_node:
            if curr_node == None:
                return 'Not Found'

            if curr_node.value == value:
                found = True
                return 'Found'
            elif value < curr_node.value:
                curr_node = curr_node.left

            else:
                curr_node = curr_node.right

        if not found:
            return 'Not Found'

    def remove(self, data):
        if self.root == None:
            return False

        cur_node = self.root

        # while cur_node:
           # find node
           if cur_node.value == data:
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

            elif data > cur_node.value:
                # right
                cur_node = cur_node.right
            elif data < cur_node.value:
                # left
                cur_node = cur_node.left

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)


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
bst.remove(12)
# bst.remove(6)
# bst.remove(5)
# bst.remove(8)
# bst.remove(10)
print()
bst.print_tree()
