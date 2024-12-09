# same as linked list but has a pointer to both next and previous node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

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
            new_node.prev = self.tail
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
            self.length += 1
            return

        # if node is not the first item
        while stopper.next:
            if count == (index - 1):
                # we subtract 1 from index to be able to get the node before the one we want so we can shift
                # we set the node we want to insert next value to the node we just found
                new_node.next = stopper.next
                new_node.prev = stopper

                stopper.next = new_node

                found = True

                self.length += 1

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
            self.length -= 1
            return

        # if node is not the first item
        while stopper.next:
            if count == (index - 1):
                # we subtract 1 from index to be able to get the node before the one we want so we can shift and remove
                stopper.next = stopper.next.next
                stopper.next.prev = stopper
                found = True
                self.length -= 1
                break

            else:
                count += 1
                stopper = stopper.next

        if not found:
            return print('index out of range')

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return

    def display(self):
        stopper = self.head
        while stopper:
            print(f'<<-  {stopper.data} ->>', end=' ')
            stopper = stopper.next

    def len(self):
        print(self.length)
        return self.length


dl = DoublyLinkedList()


dl.append(10)
dl.append(20)
dl.append(30)
dl.append(40)
dl.append(50)
dl.prepend(1)
dl.prepend(2)
dl.prepend(5)
dl.insert(4, 3)
dl.display()

dl.remove(3)
dl.remove(0)
print()
dl.display()
print()

dl.len()


'''
singly vs doubly linked list
singly 
simple compared to doubly 
it requires less memory so delete and insert are faster than double 

cons 
it cant be interated in reverse
if we loose reverse to head the list can be lost forever
it apporitate to use when memory is expensive and do fast insertion and deleteion and u dont have much searching 


pros of doubly 
can be traversed forward or backwards
if u want to delete a node u dont need to traverse from the head u just use prev

good when u dont have much limitation on memory and have searching
'''
