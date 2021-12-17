# P08. REQ : Remove Duplicates in dictionary

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  update
2. STATE      -->  Dictionary 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper. 
2. write down the dictionary with keys and duplicate values.
3. Write down the dictionary without the duplicate values.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
# 2. Algorithm
print("--------2. Algorithm----------")
dict1 = {'emp1': {'name': "karthick", 'role': 'developer'}, 'emp2': {'name': "kumar", 'role': 'developer'},
         'emp3': {'name': "karthick", 'role': 'developer'}}
print("Dictionary with duplicates:", dict1)
res = {}

for key,value in dict1.items():
    if value not in res.values():
        res[key] = value
print("Dictionary after removing duplicates:", res)



# 3 Using Functions
print("--------3. Functions----------")
def duplicate():
    dict1 = {'emp1': {'name': "karthick", 'role': 'developer'}, 'emp2': {'name': "kumar", 'role': 'developer'},
             'emp3': {'name': "karthick", 'role': 'developer'}}
    print("Dictionary with duplicates:", dict1)
    res = {}

    for key, value in dict1.items():
        if value not in res.values():
            res[key] = value
    print("Dictionary after removing duplicates:", res)
duplicate()


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