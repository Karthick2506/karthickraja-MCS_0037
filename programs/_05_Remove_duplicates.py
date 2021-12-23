# P01. REQ : Remove duplicates in the list

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
2. write a list 
3. remove the duplicate numbers.
4. write down the new list
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
list1 = [1,2,3,4,5,6,1,3,4]
print("Original list:", list1)
a = set(list1)
list2 = list(a)
print("List after removing Duplicates:", list2)

# 2. Algorithm
print("--------2. Algorithm----------")

list1 = [1,2,3,4,5,6,1,3,4]
print("Original list:", list1)
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("List after removing Duplicates:", list2)





# 3 Using Functions
print("--------3. Functions----------")





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