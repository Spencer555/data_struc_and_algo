'''
stacks and queues they are linear data structures the allow us to traverse sequencially (go thru data elements one by one) where only one data element can be directly reached  they are implemented in similar ways and the only difference is how items get removed - there is no random access operation  u only use stacks and queues to run opearations like push, peek, pop all of which deal with only first or last elements
'''

'''
stacks is a type of datastructure that are thought of as plates stacked on top of each other as vertically lifo(last in first out) 

lookup 0(n)
pop 0(1)
push 0(1)
peek 0(1) last item in a list

usefull ways of stack 
browser history 
text undo or redo

'''


'''
queue 
lookup 0(n)
enqueue (push) 0(1)
dequeue (pop in this case takes out the first person in line) 0(1)
peek 0(1) the first in the list


its like a bus queue first in first out (fifo)

they are used in programming problems or interview questions 

e.g. wait list app to buy tickets for a concert that uses queues 
or a resturant app to check in to see if u can get a table 
uber first book first get the ride
etc


'''


# stacks can be built with arrays or linked list
# exe why would we want to build stack with arrays vs linked list and vice verse
# exe why would we want to build queues with arrays vs linked list and vice verse


# linked list is better than arrays because it allows easy access to first and last element and there is not unshifting to be done
# plus arrays have a fixed amount of memory that when it get to it has to increase


# arrays is better than linked list too because it allows cache locality because items are arranged next to each other in memory

# but overall linked list is the best
# and when removing element with linked list we just redirect the pointers unlike array where we have to unshift


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackUsingLinkedList:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top:
            return self.top.value

    def push(self, data):
        if not self.bottom:
            self.bottom = data
            self.top = self.bottom
            self.length += 1
            return
        else:
            data.next = self.top
            self.top = data
            self.length += 1

    def pop(self):

        if not self.top:
            return 'Stack is empty'

        temp = self.top
        self.top = self.top.next
        return temp.value

    def isEmpty(self):
        return not self.top

    def display(self):
        current = self.top

        while current:
            print(f'{current.value} ->', end=' ')
            current = current.next
        return


myStack = StackUsingLinkedList()


def run_myStack():
    print(myStack.isEmpty())
    myStack.push(Node('Discord'))
    myStack.push(Node('Udemy'))
    myStack.push(Node('Google'))
    myStack.push(Node('Zero to mastery'))
    myStack.push(Node('Gradestone'))
    print(myStack.isEmpty())
    myStack.display()
    print()

    # print(myStack.peek())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())

    myStack.display()


class StackUsingArrays:

    def __init__(self):
        self.array = []
        self.length = 0

    def peek(self):
        return print('peek', self.array[-1])

    def push(self, data):
        self.array.append(data)
        self.length += 1
        return print(self.array)

    def pop(self):

        if len(self.array) < 1:
            return 'Stack is empty'
        self.length -= 1
        return print('pop', self.array.pop())

    def isEmpty(self):
        return print(len(self.array) > 0)

    def display(self):
        return print(self.array)


myStackArrays = StackUsingArrays()


def run_array_stacks():
    print(myStackArrays.isEmpty())
    myStackArrays.push('Discord')
    myStackArrays.push('Udemy')
    myStackArrays.push('Google')
    myStackArrays.push('Zero to mastery')
    myStackArrays.push('Gradestone')
    myStackArrays.isEmpty()
    myStackArrays.display()
    # print()

    myStackArrays.peek()
    myStackArrays.pop()
    myStackArrays.pop()
    myStackArrays.pop()
    myStackArrays.pop()
    print('length', myStackArrays.length)

    myStackArrays.display()


class QNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueWithLinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value

    def enqueue(self, data):

        if self.first is None:
            self.first = data
            self.last = self.first
            self.length += 1
            return

        self.last.next = data
        self.last = data
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return 'queue is empty'

        temp = self.first.value
        self.first = self.first.next
        return temp

    def isEmpty(self):
        return self.first == None

    def display(self):
        current = self.first

        while current:
            print(f'{current.value} ->', end=' ')
            current = current.next
        return


myQueue_ll = QueueWithLinkedList()

print(myQueue_ll.isEmpty())
myQueue_ll.enqueue(QNode('Discord'))
myQueue_ll.enqueue(QNode('Udemy'))
myQueue_ll.enqueue(QNode('Google'))
myQueue_ll.enqueue(QNode('Zero to mastery'))
myQueue_ll.enqueue(QNode('Gradestone'))
myQueue_ll.isEmpty()
myQueue_ll.display()
print()

print('peek', myQueue_ll.peek())
myQueue_ll.dequeue()
myQueue_ll.dequeue()
myQueue_ll.dequeue()
myQueue_ll.dequeue()
print()
myQueue_ll.display()

print()
print('length', myQueue_ll.length)


# common inteview questions
# implement a queue using stacks


class ImplementQueuesUsingStacks:

    def __init__(self):
        self.array = []
        self.length = 0

    def peek(self):
        return print('peek', self.array[0])

    def enqueue(self, data):
        self.array.insert(0, data)
        self.length += 1
        return print(self.array)

    def pop(self):

        if len(self.array) < 1:
            return 'Stack is empty'
        self.length -= 1
        return print('pop', self.array.pop(0))

    def isEmpty(self):
        return print(len(self.array) > 0)

    def display(self):
        return print(self.array)


testing = ImplementQueuesUsingStacks()
