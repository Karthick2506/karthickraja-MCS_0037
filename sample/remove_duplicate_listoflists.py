# P03. REQ : Remove duplicates from list of lists

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
2. write a list that contains sublists.
3. remove the duplicates and write down that list.



'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
num = [[1, 2], [4], [3, 5, 2], [1, 2], [22]]



# 2. Algorithm
print("--------2. Algorithm----------")
num = [[1, 2], [4], [3, 5, 2], [1, 2], [22]]
print("Original List is:", num)
num1 = []
for x in num:
    if x not in num1:
        num1.append(x)
print("Original List is:", num1)


# 3 Using Functions
print("--------3. Functions----------")
def dupp():
    num = [[1, 2], [4], [3, 5, 2], [1, 2], [22]]
    print("Original List is:", num)
    num1 = []
    for x in num:
        if x not in num1:
            num1.append(x)
    print("Original List is:", num1)
dupp()



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