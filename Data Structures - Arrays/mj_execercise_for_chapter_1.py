# one

# strings = ['a', 'b', 'c']
#
# print(strings[2])
#
# strings.append('e')  # O(1)
#
# strings.pop()  # O(1)
# strings.pop()
#
# strings.insert(0, 'x')  # O(n)
#
# strings.insert(2, 'alien')
#
# print(strings)


# two

# class Array_Impl:
#
#     def __int__(self):
#         self.length = 0
#         self.data = {}
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def get(self, index):
#         return self.data[index]
#
#     def push(self, item):
#         self.data[self.length] = item
#         self.length += 1
#
#     def pop(self):
#         lastitem = self.data[self.length - 1]
#         del self.data[self.length - 1]
#         self.length -= 1
#         return lastitem
#
#     def delete(self, index):
#         item_to_delete = self.data[index]
#         for i in range(index, self.length - 1):
#             self.data[i] = self.data[i + 1]
#
#         del self.data[self.length - 1]
#         self.length -= 1
#         return item_to_delete
#
#
# arr_data = Array_Impl()
# print(arr_data)
# arr_data.push(3)
# print(arr)

"""
a = 3

"""



def reverse(str_i):
    myList = []
    for i in range(len(str)-1,-1,-1):
        myList.append(str[i])
    return ''.join(myList)

"""
# list => string
>>> time_list
['10', '34', '17']
>>> ':'.join(time_list)
'10:34:17'
"""


"""
Four
"""

def mergesortarr(a,b):
    if len(a) == 0 or len(b) == 0:
        return a+b
    myList = []
    i =0
    j =0
    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            myList.append(a[i])
            i+=1
        elif b[j] < a[i]:
            myList.append(b[j])
            j +=1
    print(myList)
    return myList + a[i:] + b[j:]

a = [1, 3, 4, 6, 20]
b = [2, 3, 4, 5, 6, 9, 11, 76]
x = mergesortarr(a, b)
print(x)