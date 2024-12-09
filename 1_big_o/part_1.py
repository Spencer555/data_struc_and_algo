'''
big o the official  term is big o asymptotic analysis - it tells us how well a problem is solved

what is good code?
1 readable -is it clean and others understand it
2 scalable - is your code scalable its what big o allows us to measure
'''


# this example how can we measure the efficiency of this or runtime

'''
we want to make a food we give ingredients our kitchen and food is make 

we want to solve a problem we give code to an interpreter or compiler and problem is solved
'''
# lets measure how long this runs

# when using nemo it takes zero secs but what if we had a big array
import math
from time import  time
nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill',
            'bloat', 'nigel', 'squirt', 'darla', 'hank']

large_array = ['nemo' for nemo in range(10)]

# finding nemo has a big o notation of 0(n) or linear because it speed depends on the number of inputs


def find_nemo(array):
    t1 = time()
    for i in array:
        if i == 'nemo':
            print('found nem0!')
    t2 = time()

    print('time taken to find nemo', t2-t1)


# find_nemo(nemo)
# find_nemo(everyone)
find_nemo(large_array)


# as out input grew out function became smaller and runtime increased
# big o is the language we use to talk about how long an algo takes to run e.g when we grow bigger with input how much does the algo or function slow down , as out elements increases how many algorithmic operations do we have to do this  what we call algorithmic efficiency big o allows us to explain this concept
# different functions have different big o complexity

# scalability as things grow does it sacle

'''another way to think about it is this we have a compressor function if its only  1 item the compressor compresses only once etc if we have multiple we compress the number of times'''


'''
-Big Os-
O(1) Constant- no loops
O(log N) Logarithmic- usually searching algorithms have log n if they are sorted (Binary Search)
O(n) Linear- for loops, while loops through n items
O(n log(n)) Log Liniear- usually sorting operations
O(n^2) Quadratic- every element in a collection needs to be compared to ever other element. Two
nested loops
O(2^n) Exponential- recursive algorithms that solves a problem of size N
O(n!) Factorial- you are adding a loop for every element
Iterating through half a collection is still O(n)
Two separate collections: O(a * b)
-What can cause time in a function?-
Operations (+, -, *, /)
Comparisons (<, >, ==)
Looping (for, while)
Outside Function call (function())
-Rule Book-
Rule 1: Always worst Case
Rule 2: Remove Constants
Rule 3: Different inputs should have different variables. O(a+b). A and B arrays nested would be
O(a*b)
+ for steps in order
* for nested steps
Rule 4: Drop Non-dominant terms
-What causes Space complexity?-
Variables
Data Structures
Function Call
Allocations

'''


# constant 0(1)
# this is 0(1) because no matter the size of input the runtime would still be the same
def compress(boxes):
    print(boxes[0])


# this is still constant because if we measure line by line we get 0(1) for each
# this is 0(2) of of 100 is still round down to 0(1) its a flat lines it always constant
def print_first_two_boxes(boxes):
    print(boxes[0])  # 0(1)
    print(boxes[1])  # 0(1)


# What is the Big O of the below function? (Hint, you may want to go line by line)
def funChallenge(input):
    a = 10  # 0(1)
    a = 50 + 3  # 0(1)

    # anything in a for is o(n) because it depends on input for num of times
    for i in input:  # 0(n)
        # anotherFunction() #0(n) this also depends on our input
        stranger = True  # 0(n)
        a += 1  # 0(n)

    return a  # 0(1)


'''
0(1) + 0(1) + 0(n) + 0(n) 0(n) 0(n) 0(1)

0(3) + 0(4n)
0(n) is the worst time so the big 0 is 0(n)
'''


# what is the big o of this


def anotherFunChallenge(input):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    for i in input:  # O(n)
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in input:  # O(n)
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    whoAmI = "I don't know"  # O(1)

# Big O = 4 + 7n = O(n)


'''
the 4 rules to follow for big o 
1 worst case 
2 remove constants 
3 different terms for inputs 
4 drop non dominats
'''

# rule 1
'''
when calculating big 0 we always think about the worst case 

using the same nemo function again we have alreay found nemo so it not efficient to continue looping
'''


nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill',
            'bloat', 'nigel', 'squirt', 'darla', 'hank']


# finding nemo has a big o notation of 0(n) or linear because it speed depends on the number of inputs the worst case is if nemo is at the end of the list everyone the best case is if nemo is at the first

print('efficient nemo')


def find_nemo(array):
    for i in array:
        if i == 'nemo':
            print('found nem0!')
            return


find_nemo(nemo)
find_nemo(everyone)


# rule two remove constants


# what the big 0 of this


def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0])  # 0(1)

    middleIndex = math.floor(len(items) / 2)  # 0(1)
    index = 0  # 0(1)

    while index < middleIndex:
        print(items[index])  # 0(n)
        index += 1  # 0(n)

    for _ in range(100):  # 0(1)
        print('hi')  # 0(1)


# so we remove constants that why we get 0(n) instead of 0(6n)
# we wont see numbers in big or
'''
(0(1) + 0(1) + 0(1)) + ((0(n) + 0(n) + 0(n) + (0(1) + 0(1)))
(0(3)) + ((0(3n) + (0(2n))
0(3) + 0(6n)
0(n)
'''

# rule 3 different terms diffent terms for input

# this i o(n)


def compressBoxesTwice(boxes):

    for i in boxes:
        print(boxes)

    for j in boxes:
        print(boxes)


print(compressBoxesTwice([1, 2, 3, 4]))


# if there are two params the first for loop depends on how big the boxes is and the second for loop depends on how big boxes2 is  so it becomes 0(a + b) since they are not looping over the same items if they were looping over the same items it would be o(n)
def compressBoxesTwice1(boxes, boxes2):

    for i in boxes:
        print(boxes)

    for j in boxes2:
        print(boxes2)


# common interview question
# what is the big o of this
# if u see nested loops we used multiplication so this becomes  0(n) * 0(n)
# 0(n^2)
# log all pairs of array
# log all pairs means we want to log 12,13, 14,15 the 21, 23, 24, 25
# 31,32,34,35 41, 42, 43, 45 51,52,53,54
boxes = [1, 2, 3, 4, 5]


def logAllPairsOfArray(array):
    for i in array:
        for j in array:
            print(i, j)


logAllPairsOfArray(boxes)

# a lot of interview ques are 0(n^2) then you are to make it better
# any step that happens in the same indentation you add any one thats different indentation you multiply
# different inputs equal diff variables


# rule 4 drop non dominat terms

def printAllNumbersThenAllPairSums(numbers):
    print("these are the numbers:")
    for num in numbers:  # 0(n)
        print(num)

    print("and these are their sums:")

    for firstNumber in numbers:  # 0(n^2)
        for secondNumber in numbers:
            print(firstNumber + secondNumber)


# 0(n) + 0(n^2)
# 0(n^2)
# we drop the non dominant 0(n) and keep 0(n^2)
# we only care about the most important dominant term
printAllNumbersThenAllPairSums([1, 2, 3, 4, 5])  # O(n^2)

# 0(x^2+3x+1000+x/2)
# simplified to become after dropping non dominant term
# 0(x^2)

# right data struc + right algo = good program


# the most expensive big o notation and if u are writing code that has this you are doing something wrong 0(n!) factorial time it means adding a nested loop for every input you have


# 3 pillars of programming
# 1 readable
# 2 scalable
#     speed(time complexity)
#     memory(space)


'''
there is usally a trade off between speed and memory

when a program execute it has two ways to remember things the heap and the stack the heap is where we store variables, a stack is where we keep track of our function 

causes of space complexity 

variables 
data structures 
function call 
allocations 

'''
# space complexity
print('space complexity')

# this is o(1) because we are not adding anymore memory since we are adding only i


def booooo(n):
    for i in n:
        print('boooooo!')


booooo([1, 2, 3, 4, 5])


# with this we add hi for the num of times it loops so its o(n)
def arrayOfHiNTimes(n):
    hiArray = []
    for i in hiArray:
        hiArray[i] = "hi"

    return hiArray


arrayOfHiNTimes(6)


# exercise
'''
u are working at twitter and  your boss allows you to build a feature  that allows anybody to click a button next to thier name and retrieve their most recent tweet and thier oldest tweet 
based on big o notation what can we assume about this problem 
'''

'''
without coding we know we have to find first and find last 

we know if tweets are stored in an array it would take us o(1)
'''
array_of_tweets = [
    {
        'tweet': 'hi',
        'date': 2012
    },
    {
        'tweet': 'my',
        'date': 2014
    },
    {
        'tweet': 'teddy',
        'date': 2018
    }
]

array_of_tweets[0]  # 0(1)
array_of_tweets[-1]  # 0(1)


# now our boss come back and say i want you to compare the dates of tweets what is the big o
# 0(n^2) this since we have to do nested loops and this might cost us a lot of money so u have to tell your boss this is not feastible


# whats the big o of
# 0(1)
# it depends on the language u are using  we need to know how the method works
# python keeps the length of each string internally so it just returning it so 0(1)
len('helwoshejhekhiujudsh')


# premature optimization can be the root of all evil
# and optimization sometimes can negetively optimize the readabilty of code e.g working at a young startup it might be important to write code thats easy to ship and understand later
