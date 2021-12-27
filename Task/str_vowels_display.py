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
str1 = "hai all hello everybody"
print("A Occured", str1.count("a"), "times in the sentence")
print("E Occured", str1.count("e"), "times in the sentence")
print("I Occured", str1.count("i"), "times in the sentence")
print("O Occured", str1.count("o"), "times in the sentence")
print("U Occured", str1.count("u"), "times in the sentence")


# 2. Algorithm

print("--------2. Algorithm----------")

str1 = str(input("Enter a String:"))
a = 0
e = 0
i = 0
o = 0
u = 0
for x in str1:
    if x == "a":
        a = a+1
    elif x == "e":
        e = e+1
    elif x == "i":
        i = i+1
    elif x == "o":
        o = 0+1
    elif x == "u":
        u = u+1
total_vowels = a+e+i+o+u
print("The Total Number of vowels in the sentence:", total_vowels)

# 3 Using Functions
print("--------3. Functions----------")
def vowels():
    str1 = str(input("Enter a String:"))
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for x in str1:
        if x == "a":
            a = a + 1
        elif x == "e":
            e = e + 1
        elif x == "i":
            i = i + 1
        elif x == "o":
            o = 0 + 1
        elif x == "u":
            u = u + 1
    total_vowels = a + e + i + o + u
    print("The Total Number of vowels in the sentence:", total_vowels)
vowels()






















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