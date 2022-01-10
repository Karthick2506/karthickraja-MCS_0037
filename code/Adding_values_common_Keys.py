# P09. REQ : Adding values of common keys in a dictionary

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  update
2. STATE      -->  Dictionary 
3. BEHAVIOR   -->  display |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper. 
2. Take two dictionaries with keys and values.
3. Add the values whose keys are common and write down the values.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
dict1 = {'a': 10, 'b': 12, 'c': 14}
dict2 = {'a': 100, 'e': 200, 'c': 300}
dict3 = {}
for i, j in dict1.items():
    for x, y in dict2.items():
        if i == x:
            dict3[i]=(j+y)
print(dict3)





# 2. Algorithm
print("--------2. Algorithm----------")



# 3 Using Functions
print("--------3. Functions----------")



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