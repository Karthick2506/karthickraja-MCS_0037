# P01. REQ : Upper lower case of a string

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Update
2. STATE      -->  string 
3. BEHAVIOR   -->  changing  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. assign or take a string
3. Write down the upper case of the string. 

'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")
str = "Python and Pycharm"
print("The Upper case of the string is:", str.upper())





# 2. Algorithm

print("--------2. Algorithm----------")
print("Convert into Uppercase")
str1 = input("Enter a String:")
output_upper = ''
for i in str1:
    if i not in "abcdefghijklmnopqrstuvwxyz":
        output_upper = output_upper + i
    else:
        k = ord(i)
        l = k - 32
        output_upper = output_upper + chr(l)

print(output_upper)






# 3 Using Functions
def upper_char(str):
    print("The Upper case of the string is:", str.upper())
upper_char("programming")


def up_char():
    str = "welcome"
    print("The upper case of the string is:", str.upper())
up_char()













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