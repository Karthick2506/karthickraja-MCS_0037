# P03. REQ : Print a list of space-separated elements

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
2. write a list with elements.
3. Remove those comma between each element.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")

list1 = [1,2,3,4]
print("Original List is", list1)
print("List with spaced Elements", *list1)


# 2. Algorithm
print("--------2. Algorithm----------")

list1 = [1,2,3,4]
print("original List is", list1)
for i in list1:
    print(i, end=' ')




# 3 Using Functions
print("--------3. Functions----------")

def spaced():
    list1 = [1, 2, 3, 4]
    print("original List is", list1)
    for i in list1:
        print(i, end=' ')
spaced()












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