# P03. REQ : Extend a list without append

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  update
2. STATE      -->  List 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write a list.



'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
a = [1, 2, 3, 4]
b = [7, 8, 9, 10]
b[:0] = a
print("List After Extending:", b)

# 2. Algorithm
print("--------2. Algorithm----------")
a = [1, 2, 3, 4]
b = [7, 8, 9, 10]
c = a + b
print("List After Extending:", c)

# 3 Using Functions
print("--------3. Functions----------")
def ext():
    a = [1, 2, 3, 4]
    b = [7, 8, 9, 10]
    c = a + b
    print("List After Extending:", c)
ext()



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