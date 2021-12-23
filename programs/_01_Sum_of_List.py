# P01. REQ : Sum of List

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
3. Add the numbers inside the list and write the result.
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")

list1 = [1,2,3,4,5,6]
result = [sum(list1)]
print(result)

# 2. Algorithm
print("--------2. Algorithm----------")
list1 = [1,2,3,4,5,6]
sum = 0
for i in list1:
    sum = sum + i
print(sum)

"""add_value = 0
for i in range (0, len(list1)):
    add_value = add_value + list1[i]
print("The Sum of List is:", add_value)"""





# 3 Using Functions
print("--------3. Functions----------")

def addition():
    list1 = [1, 2, 3, 4, 5, 6]
    add_value = 0
    for i in range(0, len(list1)):
        add_value = add_value + list1[i]
    print("The Sum of List is:", add_value)
addition()












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