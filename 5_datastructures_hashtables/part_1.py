'''
hash tables or hash map , maps, unorded maps , dictionaries , objects and many more names 
a dict in python are kind of hash table

arrays and hash tables are the most common interview question and you are going to use them in almost every question they are a must 

in python they are dictionary 
javascript is object 

there is a key and value 
assumming grapes = 1000
the key is the index this is done with a hash function we pass grapes to the function and it stores both key and value in this case grapes and value

we need the hash function to be fast because its used to assing and retrieve 

time complexity is 0(1)

insert 0(1)
lookkup 0(1)
delete 0(1)
search 0(1)
'''


user = {
    'age': 54,
    'name': 'kylie',
    'magic': True,
    'scream': print('arrrrhhhh')
}

user['age']  # o(1)
user['spell'] = 'abra kadabra'  # o(1)


# hashing collision
# when the hashing fucntion stores two or more user at one address forming a linked list with hash table we cant avoid these collion because there is limited space this slows down accessing info
# collision slows down reading and writing with 0(n/k)  where k is the size of hash table


# exercise

class HashTable:

    def __str__(self):
        return str(self.__dict__)

    def __init__(self, size):
        self.size = 50
        self.array = [[] for i in range(self.size)]
        # implementing our hash tables using arrays instead of objects
        # [['grapes',10000]]

    # we want set to be able to set grapes and 10000 in the array as the above

    def set_items(self, key, value):
        hash_value = self.hash(key)
        reference = self.array[hash_value]
        if len(reference) == 0:
            reference.append([hash_value, key, value])
            self.size -= 1
            return None
        elif reference[0] == key and reference[1] == value:

            return 'item already exists'
        # if there is something already in that slot simply add on
        reference.append([hash_value, key, value])
        return None

    # we want get grapes and it returns 1000

    def get_item(self, key):
        '''
        we pass the key thru the hash value to get the hash 
        we check if the hash has only one array if so then we check we return that if it has multiple we loop till we find our key  
        '''

        hash_value = self.hash(key)
        reference = self.array[hash_value]
        # we loop thru each home to find if it is there
        if len(reference) > 0:
            for i in reference:
                if i[1] == key:
                    return i[1:]
            return 'not Found'
        return 'not Found'

    def remove_item(self, key):
        '''
        we pass the key thru the hash value to get the hash 
        we check if the hash has only one array if so then we check we remove that if it has multiple we loop till we find our key  
        '''

        hash_value = self.hash(key)
        reference = self.array[hash_value]
        # we loop thru each home to find if it is there
        if len(reference) > 0:
            for i, item in enumerate(reference):
                if item[1] == key:
                    return reference.pop(i)
            return 'does not exist in hash map'
        return 'does not exist in hash map'

    def keys(self):
        # return only the keys in the list
        keys = []
        for i in self.array:
            if len(i) > 0:
                if len(i) > 1:
                    for l in i:
                        keys.append(l[1])

                elif len(i) == 1:
                    keys.append(i[0][1])

        return keys

    def get_array(self):
        return self.array

    def hash(self, key):
        return len(key) % self.size


def run_mimic_dict():

    mimic_dict = HashTable(10)

    mimic_dict.set_items('grapes', 10000)
    mimic_dict.set_items('apples', 20000)
    mimic_dict.set_items('lettuce', 30)
    mimic_dict.set_items('oranges', 40)
    mimic_dict.set_items('mangoes', 20)
    mimic_dict.set_items('cherries', 10)
    mimic_dict.set_items('cabbages', 60)
    mimic_dict.set_items('sugarcane', 700)
    mimic_dict.set_items('lemons', 70)
    mimic_dict.set_items('onions', 7)
    mimic_dict.set_items('peppers', 2)

    print(mimic_dict.get_item('oranges'))
    print(mimic_dict.get_item('sugarcane'))
    print(mimic_dict.get_item('pineapples'))

    # print(mimic_dict.remove_item('oranges'))
    # print(mimic_dict.remove_item('sugarcane'))
    # print(mimic_dict.remove_item('pineapples'))

    # print(mimic_dict.get_array())
    print('keys', mimic_dict.keys())


# interview question
'''
//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return undefined


function firstRecurringCharacter(input) 
}

//Bonus... What if we had this:
// [2,5,5,2,3,5,1,2,4]
// return 5 because the pairs are before 2,2
'''

'''
looking at this question i chose to use a dictionary for the data type and a loop
'''


def firstRecurringCharacter(input=None):

    if type(input) == list:
        first_reoccuring = {}

        for i in input:
            if i in first_reoccuring:
                first_reoccuring[i] += 1
                return i

            else:
                first_reoccuring[i] = 1

        return None

    return 'Arguments must be a list'


print(firstRecurringCharacter([2, 5, 5, 2, 3, 5, 1, 2, 4]))
print(firstRecurringCharacter([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(firstRecurringCharacter([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(firstRecurringCharacter([2, 3, 4, 5]))


'''
hash tables 

faster lookups 
fast insets 
flexible keys 


downside 
unordered 
slow key iteration
'''
