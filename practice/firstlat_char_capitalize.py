# P01. REQ : Capitalize first and last char in each letter in the string

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Update
2. STATE      -->  string 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write a string in paper.
3. write the taken string with change in case at start and end of each word.
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

# 2. Algorithm

print("--------2. Algorithm----------")
str = input("Enter the String:")
str = result = str.title()
result = ""
for i in str.split():
    result = result +  i[:-1] + i[-1].upper() + " "
print(result[:-1])




# 3 Using Functions
print("--------3. Functions----------")
def convert():
    str = input("Enter the String:")
    str = result = str.title()
    result = ""
    for i in str.split():
        result = result + i[:-1] + i[-1].upper() + " "
    print(result[:-1])
convert()












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