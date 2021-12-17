# P05. REQ : Sum of all items in a dictionaries

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  retrieve
2. STATE      -->  Dictionary 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper. 
2. write down the dictionary with keys and values.
3. sum all the items in a dictionary and write down the result.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
a = {"A": 100, "B": 200, "C": 300, "D": 400}
b = sum(a.values())
print("The sum of items in a dictionary is:", b)


# 2. Algorithm
print("--------2. Algorithm----------")
a = {"A": 100, "B": 200, "C": 300, "D": 400}
li1 = []
for i in a.values():
    li1.append(i)
print("Total Values present in the dictionary", li1)
sum = 0
for j in li1:
    sum = sum + j
print("sum of all values present in the dictionary is:", sum)


# 3 Using Functions
print("--------3. Functions----------")
def addd():
    a = {"A": 100, "B": 200, "C": 300, "D": 400}
    li1 = []
    for i in a.values():
        li1.append(i)
    print("Total Values present in the dictionary", li1)
    sum = 0
    for j in li1:
        sum = sum + j
    print("sum of all values present in the dictionary is:", sum)
addd()



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