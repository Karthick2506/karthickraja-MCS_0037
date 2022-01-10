# P01. REQ : Create an array of 5 integers and display the array items.
# Access individual element through indexes.

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Retrieval
2. STATE      -->  Array
3. BEHAVIOR   -->  int  |  =   +=    |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. Take an array with set of numbers
3. Start writing the elements using indexes. 
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

import array as aaa
arr = []
num = aaa.array('i', [3,1,3,2])
print(num[0])
print(num[1])
print(num[2])
print(num[3])



# 2. Algorithm

print("--------2. Algorithm----------")
# 3 Using Functions
print("--------3 Using Functions----------")
import array as aaa
def fun():
    arr = []
    num = aaa.array('i', [3, 1, 3, 2])
    print(num[0])
    print(num[1])
    print(num[2])
    print(num[3])

fun()


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
