# P01. REQ : Convert string into list

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
2. write a string in paper
3. write down each characters by comma seperator within square brackets
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")
str1 = "Python is interesting Language"
list1 = list(str1)
print(list1)
list2 = list(str1.split(" "))
print(list2)


# 2. Algorithm

print("--------2. Algorithm----------")
str1 = "Python"
list4 = []
"""list4[:0] = str1
print(list4)"""
for i in str1:
    list4.append(i)
print(list4)



# 3 Using Functions
print("--------3. Functions----------")
def new_li():
    str1 = "Python"
    list4 = []
    list4[:0] = str1
    print(list4)
    """for i in str1:
        list4.append(i)
    print(list4)"""



















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