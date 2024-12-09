'''
linked list 
a list that is linked 
one item has reference to another item in memory 
a linked list has a node 
which is a value u want to store and a pointer to another node 

the head is the first item in the linked list and tail is the last item in the linked list 

a linked list are null terminated which signifies it is the end of the list if a node points to null


advantages of linked list 
they can be traversed forward and backwards easily
and they can be stored anywhere in memory
easy inserting and deleting anywhere because of loose structure we just change the pointer to point to the value we want  not the entire array and there is no shifting and unshifting indexed 



cons 
there is not random access u must traverse the list 


it is ordered this is the advantage it has over hash table 


preprend 0(1)
append 0(1)
lookup 0(n)
insert 0(n)
delete 0(n)


we chose ll over arrays is simplicity and ablility to grow in strength 
'''

# pointer - a reference to another place in memory or object or node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        # if it is empty
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return

    def insert(self, value, index):
        new_node = Node(value)

        stopper = self.head
        count = 0
        found = False

        # if node is the first item
        if index == 0:
            self.prepend(new_node)

        # if node is not the first item
        while stopper.next:
            if count == (index - 1):
                # we subtract 1 from index to be able to get the node before the one we want so we can shift
                # we set the node we want to insert next value to the node we just found
                new_node.next = stopper.next

                stopper.next = new_node

                found = True

                break
            else:
                count += 1
                stopper = stopper.next

        if not found:
            return print('index out of range')

    def remove(self, index):

        stopper = self.head
        count = 0
        found = False

        # if node is the first item
        if index == 0:
            self.head = self.head.next
            return


# 5 -> > 2 -> > 1 -> > 4 -> > 10 -> > 20 -> > 30 -> >
        # if node is not the first item
        while stopper.next:
            if count == (index - 1):
                # we subtract 1 from index to be able to get the node before the one we want so we can shift and remove
                stopper.next = stopper.next.next
                found = True
                break

            else:
                count += 1
                stopper = stopper.next

        if not found:
            return print('index out of range')

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        stopper = self.head
        while stopper:
            print(f'{stopper.data} ->>', end=' ')
            stopper = stopper.next

    def reverse(self):
        '''learn how to do it and understand it'''
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

        return

    def len(self):
        return self.length


ll = LinkedList()


ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(1)
ll.prepend(2)
ll.prepend(5)
ll.insert(4, 3)
ll.remove(6)
print()
ll.display()
print()
print('reverse', ll.reverse())
