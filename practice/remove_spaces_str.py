# P01. REQ : Count the vowels in the string

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
2. write a string in paper.
3. write down the remaining part of the string skipping the vowels.
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")
str1 = "This is Karthick  "
print(str1)
print(str1.strip(" "))
str2 = "k a r t h ic k"
print("Original String:", str2)
out = str2.replace(" ", "")
print("After Removing Spaces:", out)


# 2. Algorithm

print("--------2. Algorithm----------")
str2 = "k a r t h ic k"
li1 = []
print("Original String:", str2)
for i in str2.replace(" ", ""):
    li1.append(i)
output = ''.join(li1)
print("After Removing Spaces:", output)



# 3 Using Functions
print("--------3. Functions----------")
def space():
    str2 = "k a r t h ic k R a j a"
    print("Original String:", str2)
    out = str2.replace(" ", "")
    print("After Removing Spaces:", out)
space()

def space1(str):

    print("Original String:", str)
    out = str.replace(" ", "")
    print("After Removing Spaces:", out)
space1("k a r t h ic k R a j a")












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