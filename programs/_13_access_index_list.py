# P01. REQ : To access the index of the list

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
2. write a list in paper
3. count the index.
4. write down the index values for the list
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
list1 = ["a", "e", "i", "o", "u"]
print("Normal List is:", list1)
ind = list1.index("i")
ind2 = list1. index("o")
print("The index of i is:", ind)
print("The index of o is:", ind2)


# 2. Algorithm
print("--------2. Algorithm----------")
list1 = ["a", "e", "i", "o", "u"]
for i in range(len(list1)):
    print(i, end = " ")
    print(list1[i])



# 3 Using Functions
print("--------3. Functions----------")
def ind():
    list1 = ["a", "e", "i", "o", "u"]
    for i in range(len(list1)):
        print(i, end=" ")
        print(list1[i])
ind()


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