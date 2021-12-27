# P03. REQ : Print Nested List in a newline

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
2. write a list inside the list.
3. Add the Element before the list.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")

list1 = []
for i in range(5):
    list1.append([])
for j in range(5):
    list1[i].append(j)
print(list1)


# 2. Algorithm
print("--------2. Algorithm----------")
list1 = [[1, 2, 3], [7, 8, 9], [4, 5]]
list2 = []
for i in list1:
    for x in i:
        list2.append(x)
print(list2)




# 3 Using Functions
print("--------3. Functions----------")
def li1():
    list1 = [[1, 2, 3], [7, 8, 9], [4, 5]]
    list2 = []
    for i in list1:
        for x in i:
            list2.append(x)
    print(list2)
li1()













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