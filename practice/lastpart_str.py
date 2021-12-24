# P01. REQ : Print Last part of a string

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Retrieve
2. STATE      -->  string 
3. BEHAVIOR   -->  print  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. assign or take a string
3. Write down the last part of the string. 
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

str = "Python Programming"
print("The Last Character in the String:", str[-1])





# 2. Algorithm

print("--------2. Algorithm----------")
str = input("Enter a String")
str_rev = str[::-1]
last_char = str_rev[0]
print("The Last Characyter in the String is:", last_char)


# 3 Using Functions

def last_part():
    str = input("Enter a String")
    print("The Last Character in the String:", str[-1])
last_part()

def las_char(str1):
    print("The Last Character in the String:", str1[-1])
las_char("Bangalore")


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