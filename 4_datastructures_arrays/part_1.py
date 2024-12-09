# arrays
# they organize list sequencially meaning one after the other in memory
# lookup 0(1) push 0(1) insert 0(n) delete 0(n)

# if all u need is to store data and iterate over it then arrays are the best choice


strings = ['a', 'b', 'c', 'd']
# we have 4 items and if each item is taking up 4 shelfs on a 32bit sys = 16 byte of storage


strings[2]
# am telling the pc go to the array called strings and grab the 3rd item from where the array is stored on your memory


# append add f to end of list
strings.append('f')  # 0(1)


# pop -remove last item
strings.pop()  # 0(1)


# add item at beginning #0(n)
strings.insert(0, 'g')


print(strings)


# static arrays are fixed inside and no of elements are specified before hand
# but in python we use dynamic arrays which automatically resize the list it expands as u add more element u dont need to determine the size ahead of time

# but dynamic underneath the hood can become 0(n)
# if the python created for 10 items and u give it 11 it copies the 10 items and add it to the new array with 20 spaces and add the 11 th item


# arrays

class Array:

    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def access_data(self, index):
        try:
            return self.data[index]
        except:
            return None

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        item_to_delete = self.data[self.length - 1]
        temp = item_to_delete
        del item_to_delete
        self.length -= 1
        return temp, self.length

    def delete(self, index):
        item_to_delete = self.data[index]

        for i in range(self.length - 1):
            # we are shifting the items to the left by 1
            self.data[i] = self.data[i+1]
        temp = item_to_delete
        del item_to_delete
        self.length -= 1
        return temp, self.length


new_array = Array()


def run_custom_array():
    print(new_array.push('1'))
    print(new_array.push('loved'))
    print(new_array.push('you'))
    print(new_array.push('with'))
    print(new_array.push('all'))
    print(new_array.push('heart'))
    print(new_array.push('but you played me'))
    print(new_array.push('and i became a monster'))
    print(new_array.pop())
    print(new_array.pop())
    print(new_array.pop())
    print(new_array.delete(0))
    print(new_array.delete(1))
    print(new_array.delete(2))
    print(new_array.delete(3))


# run_custom_array()


# u should treat any string questions as an array questions
# strings are an array of characters

'''
so if u get a question like reverse a string
think about converting it to an array do an operation on it or loop e.g split and return it as a string after you have finished with it
'''

# common interview question
'''
can u create a function that reverse a string
so spencer passed in should return recneps
'''

# first solution was 0(n^2)


def reverse_string(str):

    if type(str) != str:
        return 'Argument must be a string'

    lists = []

    for i in str:
        lists.insert(0, i)

    return " ".join(lists)


# print(reverse_string('spencer'))
the_list = []
string = 'spencer'


# second solu is 0(n)
def reverse_st(str):
    the_list = []
    if type(str) != str:
        return 'only arguments allowed are strings'
    for i in range((len(string)-1), -1, -1):
        the_list.append(string[i])

    return ' '.join(the_list)


# or
# or just stri[::-1]


# another exe interview
'''
given two arrays that are sorted can  u merge these two arrays into one big one that is still sorted

mergesorted_arrays([0,3,4,31], [4,6,30]):

[0,3,4,4,6,30,31]
'''


def mergesorted_arrays(arr_1=None, arr_2=None):

    if type(arr_1) == list and type(arr_2) == list:
        if len(arr_1) == 0 or len(arr_2) == 0:
            return arr_1+arr_2

        arr_3 = arr_1 + arr_2
        arr_3.sort()
        return arr_3

    return 'Lists are the only accepted arguments'


print(mergesorted_arrays([0, 3, 4, 31], [4, 6, 30]))
print(mergesorted_arrays([1, 3, 4, 6, 20], [2, 3, 4, 5, 6, 9, 11, 76]))


# arrays are awesome for sorting

'''
arrays are good for 
fast lookups 
fast push/pop 
ordered 


bad for
inserts 
deletes 
fixed size if using static array
'''
