# P01. REQ : Reverse the order of the items in the array.

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Update
2. STATE      -->  Array
3. BEHAVIOR   -->  int  |  =   +=    |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. Take an array with set of numbers
3. reverse the element and store it in another array 
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

from array import *
arr = []
num = array('i', [1, 2, 3, 4])
print("Before Reversing:", num)
num.reverse()
arr.append(num)
print("After Reversing:", arr)



# 2. Algorithm
print("--------2. Algorithm----------")
from array import *
arr = []
num = array('i', [1, 2, 3, 4])
for a in range(len(num)-1,-1,-1):
    arr.append(a)
print(arr)


# 3 Using Functions
print("--------3 Using Functions----------")
from array import *
def rev():
    arr = []
    num = array('i', [1, 2, 3, 4])
    print("Before Reversing:", num)
    num.reverse()
    arr.append(num)
    print("After Reversing:", arr)
rev()


# 4 OOPS
print("--------4 Object Oriented----------")

# 5 Exception handling
print("--------5 Exception handling----------")

# 6 File Handling
print("--------6 File Handling----------")

# 7 Database interaction MVC
print("--------7 Database interaction----------")

# 8 UI Interaction
print("--------8 UI Interaction----------")
