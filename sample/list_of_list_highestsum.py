# P03. REQ : Find the list in a list of lists whose sum of elements is the highest

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
2. write a list that contains many lists inside that.
3. calculate the highest sum within that list that contains many sub list


'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")

list1 = [[1,2,3,4], [20,30], [2,4,6,7]]
li2= max(list1)
print("Highest in the list is:", li2)
print("Sum of highest in the list is:", sum(li2))

# 2. Algorithm
print("--------2. Algorithm----------")
list1 = [[1,2,3,4], [20,30], [2,4,6,7]]
su = 0
for x in list1:
    su = max(sum(x), su)
    print(su)

# 3 Using Functions
print("--------3. Functions----------")

def ad():
    list1 = [[1, 2, 3, 4], [20, 30], [2, 4, 6, 7]]
    li2 = max(list1)
    print("Highest in the list is:", li2)
    print("Sum of highest in the list is:", sum(li2))
ad()


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