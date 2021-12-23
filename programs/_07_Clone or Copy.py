# P01. REQ : clone or copy of the list

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
2. write a list a in paper 
3. write the same list again with different name.
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
li1 = [1,2,3,4,5,6]
print("Original list:", li1)
li2 = li1.copy()
print("Copy of the list:", li2)


# 2. Algorithm
print("--------2. Algorithm----------")
li1 = [1,2,3,4,5,6]
print("Original list:", li1)
li2 = list(li1)
print("Copy of the list:", li2)
a = li1[:]
print("The Copy of the list is:", a)



# 3 Using Functions
print("--------3. Functions----------")
def copy():
    li1 = [1, 2, 3, 4, 5, 6]
    print("Original list:", li1)
    li2 = list(li1)
    print("Copy of the list:", li2)
copy()





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