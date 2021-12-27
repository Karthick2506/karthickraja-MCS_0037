# P01. REQ : print the index of the character in string

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
3. count the index of the characters in the string
4. write down the index value for each character
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")
str1 = "Bangalore"
ind_value = str1.index("a")
print("The index value of a is:", ind_value)
for char, index in enumerate(str1):
    print(f"The index position of {index} is {char}")




# 2. Algorithm

print("--------2. Algorithm----------")
str1 = "Bangalore"
for char, index in enumerate(str1):
    print(f"The index position of {index} is {char}")



# 3 Using Functions
print("--------3. Functions----------")
def ind_position():
    for char, index in enumerate(str1):
        print(f"The index position of {index} is {char}")
ind_position()


















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