# P01. REQ : Append a new item to the end of the array.

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
3. Add a new number at the end. 
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

from array import *
num = array('i', [1, 2, 3, 4, 5])
print("Array Before Adding Element:", num)
num.append(6)
print("Array After Adding Element:", num)

# 2. Algorithm

print("--------2. Algorithm----------")
# 3 Using Functions
print("--------3 Using Functions----------")
from array import *
def app():
    num = array('i', [1, 2, 3, 4, 5])
    print("Array Before Adding Element:", num)
    num.append(6)
    print("Array After Adding Element:", num)
app()




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
