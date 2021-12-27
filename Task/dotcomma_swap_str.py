# P01. REQ : Swap comma dot in a string

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  update
2. STATE      -->  string 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write a string in paper with dot and comma seperator inside it 
3. write down the string skipping the dot comma.
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")
str1 = "hai,this.is.karthick"
print("Original string:", str1)
str2 = str1.replace(',', ' ')
str3 = str2.replace('.', ' ')
print("String after removing dot and comma:", str3)



# 2. Algorithm

print("--------2. Algorithm----------")
str1 = "python,easy.to.learn"
print("Original string:", str1)
str2 = str1.replace(',', ' ')
str3 = str2.replace('.', ' ')
print("String after removing dot and comma:", str3)




# 3 Using Functions
print("--------3. Functions----------")
def swap():
    str1 = "This,is.new.world"
    print("Original string:", str1)
    str2 = str1.replace(',', ' ')
    str3 = str2.replace('.', ' ')
    print("String after removing dot and comma:", str3)
swap()




















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