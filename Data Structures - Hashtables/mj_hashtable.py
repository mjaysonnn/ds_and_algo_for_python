"""
Hash Table Implementation
"""


def hashtable(mylist):
    mydict = {}
    for i in range(0, len(mylist)):
        print(mydict)
        if mylist[i] in mydict:
            return mydict[i]
        else:
            mydict[mylist[i]] = i
    return 0


mylist = [2, 1, 1, 2, 3, 4, 5]
x = hashtable(mylist)
print(x)

"""

Implementation
"""


class HashTable:
    def __init__(self):
        self.bucket = 16
        self.hashmap = [[] for _ in range(self.bucket)]

    def __str__(self):
        return str(self.__dir__)

    def hash(self, key):
        return len(key) % self.bucket

    def put(self, key, value):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]

        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] = value
                return None
        reference.append([key, value])
        return None

    def get(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return -1

    def remove(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return
        return None
