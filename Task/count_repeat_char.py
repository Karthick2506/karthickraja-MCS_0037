# P01. REQ : to count repeated characters in a string

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  retrieve
2. STATE      -->  string 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write a string in paper
3. count the repeated characters and write down in the paper
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")
str1 = "karnataka"
result = str1.count("a")
result1 = str1.count("k")
print("The Original String is:", str1)
print("The number of times a occured in the sentence is:", result)
print("The number of times k occured in the sentence is:", result1)

# 2. Algorithm

print("--------2. Algorithm----------")
str1 = "karnataka"
print("The Original String is:", str1)
dummy = []
for char in str1:
    if str1.count(char) > 1:
        if char not in dummy:
            dummy.append(char)
print("The repeated Characters in the given string is:", dummy)


# 3 Using Functions
print("--------3. Functions----------")
def countt():
    str1 = "karnataka"
    print("The Original String is:", str1)
    dummy = []
    for char in str1:
        if str1.count(char) > 1:
            if char not in dummy:
                dummy.append(char)
    print("The repeated Characters in the given string is:", dummy)
countt()

















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