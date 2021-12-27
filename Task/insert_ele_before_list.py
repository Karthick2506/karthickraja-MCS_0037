# P02. REQ : Insert an element before each element of a list

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  retrieve
2. STATE      -->  List 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write a list 
3. Add the Element before the list.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")

list1 = [1, 2, 3, 4, 77]
list1.insert(0, 1222)
print("The List After adding the element", list1)






# 2. Algorithm
print("--------2. Algorithm----------")
list1 = ["bat", "ball", "stumps"]
list1 = [i for item in list1 for i in ('cricket', item)]
print("The List After adding the element", list1)




# 3 Using Functions
print("--------3. Functions----------")

def ddd():
    list1 = ["bat", "ball", "stumps"]
    list1 = [i for item in list1 for i in ('cricket', item)]
    print("The List After adding the element", list1)
ddd()













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