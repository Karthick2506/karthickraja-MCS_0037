# P01. REQ : to count occurrences of a substring in a string

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
3. count the substring occurrences and write down in the paper
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")
str1 = "python is a fast growing language python is easy to learn"
result = str1.count("python")
print("The number of times particular word repeats in the sentence is:", result)

# 2. Algorithm

print("--------2. Algorithm----------")
str2 = "python is a fast growing language python is easy to learn"
for i in str2.split():
    count = 0
    for j in str2.split():
        if i == j:
            print(i)
            count += 1
            print(count)









# 3 Using Functions
print("--------3. Functions----------")
def sub_str():
    str3 = "python is a fast growing language python is easy to learn"
    for i in str3.split():
        count = 0
        for j in str3.split():
            if i == j:
                print(i)
                count += 1
                print(count)
sub_str()

















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